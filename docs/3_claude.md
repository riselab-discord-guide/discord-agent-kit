# Step 3a: Claude Code + Discord

Claude Code has an official Discord plugin, so you don't need any code from this repo.

## 1. Install the requirements

```bash
# Claude Code (skip if you already have it)
curl -fsSL https://claude.ai/install.sh | bash

# Bun, which the Discord plugin runs on
curl -fsSL https://bun.sh/install | bash
```

## 2. Install the plugin and add your token

Start `claude` in your project folder and run:

```
/plugin install discord@claude-plugins-official
/reload-plugins
/discord:configure <paste-your-bot-token>
```

Then exit Claude (`/exit`).

## 3. Start Claude with Discord turned on

Run it inside `tmux` so it keeps running after you disconnect:

```bash
tmux new -s claude
cd ~/my-project
claude --channels plugin:discord@claude-plugins-official
```

To leave it running, detach with `Ctrl-b` then `d`. Come back later with `tmux attach -t claude`.

## 4. Pair your Discord account

1. In Discord, send your bot a **direct message**, e.g. "hi". It replies with a pairing code.
2. In the Claude terminal, run:
   ```
   /discord:access pair <code>
   ```
3. Lock it down so only you can use the bot:
   ```
   /discord:access policy allowlist
   ```

You can now DM the bot and Claude will reply.

## 5. (Optional) Use it in a server channel

DMs work right away. To talk to the bot in a server channel, allow that channel first:

```
/discord:access group add <channel-id>
```

In that channel, **@mention** the bot to talk to it. Threads inside the channel work too.

## Troubleshooting

- **The bot is offline.** Claude isn't running with `--channels`. Start it as in step 3.
- **The bot doesn't reply in a channel.** Run `/discord:access group add <channel-id>`, and make sure you @mentioned the bot.
- **The bot stops halfway.** Claude may be waiting for permission to run a command. Check the tmux window (`tmux attach -t claude`).
- **Full plugin docs:** <https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/discord>
