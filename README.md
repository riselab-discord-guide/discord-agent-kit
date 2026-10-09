# discord-agent-kit

Talk to your AI coding agent (**Claude Code** or **Codex**) from Discord.

```
you, in Discord ──@mention──▶ bot ──▶ agent running on your machine
                ◀──── reply ─────────┘
```

Why Discord?

- **One place for all agents.** You don't have to open terminals and switch between sessions. Just message the agent.
- **A log you can search.** Every conversation stays in Discord. Weeks later you can search "where did I save that result?", open the thread, and ask the agent again.
- **Works from your phone.**

## Setup (about 15 minutes)

1. **[Create a Discord bot](docs/1_discord_bot.md).** You need one bot per agent.
2. Connect an agent:
   - **[Claude Code](docs/2_claude.md)**, using the official Discord plugin. You don't need any code from this repo.
   - **[Codex](docs/3_codex.md)**, using the small bridge script in [`codex/bridge.py`](codex/bridge.py) (~80 lines).

## Tips

- **Use one Discord thread per task.** Each thread keeps its own conversation, so related work stays together and is easy to find later.
- **Keep the agent running in `tmux`.** Then it stays up after you close your terminal or laptop.
- **Keep your bot token secret.** Anyone who has it controls your bot. If it leaks, click "Reset Token" in the developer portal.
- **Only allow your own user ID.** The bot can run commands on your machine.
