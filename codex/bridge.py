#!/usr/bin/env python3
"""A very small Discord <-> Codex bridge.

Mention the bot in Discord -> the message goes to `codex exec` ->
Codex's final answer is posted back as a reply.

Each Discord channel/thread keeps its own Codex session, so follow-up
messages in the same thread continue the same conversation.
"""

import json
import os
import subprocess
import tempfile

import discord

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
ALLOWED_USER_IDS = [int(x) for x in os.environ["ALLOWED_USER_IDS"].split(",")]
WORKDIR = os.path.expanduser(os.environ.get("CODEX_WORKDIR", "~"))

sessions = {}  # Discord channel/thread id -> Codex session id


def ask_codex(prompt, session_id):
    """Run one Codex turn and return (answer, session_id)."""
    answer_file = tempfile.mktemp(suffix=".txt")
    # workspace-write: Codex may edit files inside WORKDIR (default is read-only).
    options = ["--json", "--skip-git-repo-check", "-o", answer_file,
               "-c", 'sandbox_mode="workspace-write"']
    if session_id:
        cmd = ["codex", "exec", "resume", *options, session_id, prompt]
    else:
        cmd = ["codex", "exec", *options, prompt]
    result = subprocess.run(cmd, cwd=WORKDIR, capture_output=True, text=True)

    # Codex prints JSON events; the first one tells us the session id.
    for line in result.stdout.splitlines():
        if '"thread.started"' in line:
            session_id = json.loads(line)["thread_id"]

    if os.path.exists(answer_file):
        answer = open(answer_file).read().strip()
        os.remove(answer_file)
    else:
        answer = "Codex failed:\n" + result.stderr[-1500:]
    return answer or "(Codex gave an empty answer)", session_id


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author.id not in ALLOWED_USER_IDS:
        return
    if client.user not in message.mentions:
        return

    prompt = message.content.replace(f"<@{client.user.id}>", "").strip()
    key = message.channel.id

    async with message.channel.typing():
        # Run Codex in a background thread so the bot stays connected.
        answer, sessions[key] = await client.loop.run_in_executor(
            None, ask_codex, prompt, sessions.get(key))

    # Discord messages are limited to 2000 characters.
    for i in range(0, len(answer), 1900):
        await message.reply(answer[i:i + 1900])


client.run(TOKEN)
