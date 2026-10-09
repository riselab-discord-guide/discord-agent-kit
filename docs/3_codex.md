# Step 2b: Codex + Discord

Codex has no official Discord plugin, so this repo includes a tiny bridge, [`codex/bridge.py`](../codex/bridge.py). It works like this:

1. You @mention the bot in Discord.
2. The bridge runs `codex exec "<your message>"` in your project folder.
3. The bridge posts Codex's final answer back as a reply.

Each channel or thread keeps its own Codex session, so you can keep talking in the same thread.

## 1. Install the requirements

```bash
npm install -g @openai/codex   # Codex CLI
codex login                    # sign in once

git clone <this-repo-url> discord-agent-kit
cd discord-agent-kit
pip install -r codex/requirements.txt
```

## 2. Fill in your settings

```bash
cp codex/.env.example codex/.env
nano codex/.env
```

| Setting | What to put |
|---|---|
| `DISCORD_BOT_TOKEN` | The token from [step 1](1_discord_bot.md) |
| `ALLOWED_USER_IDS` | Your Discord user ID. Only these people can use the bot. |
| `CODEX_WORKDIR` | The folder Codex should work in |

## 3. Run it

Run it inside `tmux` so it keeps running after you disconnect:

```bash
tmux new -s codex-bot
./codex/run.sh
```

You should see `Logged in as ...`. Detach with `Ctrl-b` then `d`.

## 4. Use it

In any channel the bot can see, type:

```
@my-codex what files are in this project?
```

The bot shows "typing..." while Codex works, then replies.

## Good to know

- Codex can **edit files inside `CODEX_WORKDIR`**, but cannot touch anything outside it.
- The bridge remembers sessions only while it is running. If you restart it, the next message starts a new conversation.
- To continue a conversation in your terminal, run `codex resume` and pick the session.
- Want more, such as attachments or a `!new` command? `bridge.py` is short, so just edit it, or ask your agent to.
