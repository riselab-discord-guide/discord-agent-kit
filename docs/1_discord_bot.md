# Step 1: Create a Discord bot

You need a Discord server and a bot for your agent to log in as.

## 1. Make a server

In Discord, click **+** on the left sidebar, then **Create My Own**. A private server just for you and your agents works well.

## 2. Create the bot

1. Go to <https://discord.com/developers/applications> and click **New Application**. Name it, e.g. `my-claude`.
2. Open the **Bot** tab:
   - Click **Reset Token** and copy the token. **It is shown only once.** Keep it secret.
   - Under **Privileged Gateway Intents**, turn on **Message Content Intent**. Without it, the bot sees empty messages.

## 3. Invite the bot to your server

1. Open the **OAuth2** tab and scroll to **OAuth2 URL Generator**.
2. Under Scopes, check **`bot`**.
3. Under Bot Permissions, check:
   - View Channels
   - Send Messages
   - Send Messages in Threads
   - Read Message History
   - Attach Files
   - Add Reactions
4. Set Integration Type to **Guild Install**.
5. Open the generated URL, pick your server, and click **Authorize**.

The bot now appears in your server's member list. It shows as offline until you start the agent.

## 4. Find your IDs

Turn on **Developer Mode** in Discord: User Settings → Advanced → Developer Mode.

Now you can right-click to copy IDs:

- **Your user ID:** right-click your name → Copy User ID.
- **Channel ID:** right-click a channel → Copy Channel ID.

Next: [Claude Code](2_claude.md) or [Codex](3_codex.md).
