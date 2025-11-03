# TaiiwoBot v5 - Replit Setup

## Overview
This is TaiiwoBot v5, a cross-platform chat bot framework that supports Discord and IRC. The bot is currently configured to run on Discord with a Flask web server for health monitoring on Replit.

## Project Structure
- `discord_main.py` - Discord bot entry point with Flask web server
- `irc_main.py` - IRC bot entry point
- `taiiwobot/` - Core bot framework
  - `discord.py` - Discord server implementation
  - `irc.py` - IRC server implementation
  - `config.py` - Configuration management
  - `plugin.py` - Plugin base class
  - `server.py` - Server base class
  - `taiiwobot.py` - Main bot class
  - `util.py` - Utility functions
- `plugins/` - Plugin directory with various bot commands
- `lib/` - Libraries (including Cicada 3301 library)
- `config.json` - Bot configuration file

## Current Configuration
- **Platform**: Discord
- **Port**: 5000 (required for Replit webview)
- **Host**: 0.0.0.0 (allows Replit proxy access)
- **API Key**: Retrieved from `DISCORD_API_KEY` environment variable

## Setup Instructions

### 1. Set Discord API Key
The bot requires a Discord bot token to function. You need to:
1. Create a Discord bot at https://discord.com/developers/applications
2. Copy the bot token
3. In Replit, go to the Secrets tab (lock icon in the left sidebar)
4. Add a new secret:
   - Key: `DISCORD_API_KEY`
   - Value: Your Discord bot token

### 2. Configure Bot (Optional)
Edit `config.json` to add optional configuration:
- `owner`: Your Discord user ID (for admin commands)

### 3. Start the Bot
The bot will start automatically when you run the repl. The workflow "Discord Bot" runs `python discord_main.py`.

## Features
- Plugin system with automatic loading
- Cross-platform support (Discord and IRC)
- Command parsing with flags and subcommands
- Rich embeds and interactive menus (Discord)
- Web server for health monitoring on port 5000

## Available Plugins
- Gematria - Cicada 3301 cipher tools
- LiberPrimus - Cicada 3301 Liber Primus decoder
- help - Bot command help
- code - Code execution
- meme - Meme generation
- movie - Movie information
- Moderator - Moderation tools
- And many more in the `plugins/` directory

## Development
To create new plugins, see the README.md for detailed instructions on the plugin system.

## Recent Changes (Nov 3, 2025)
- Updated for Replit environment
- Fixed discord.py 2.6.4 compatibility (removed deprecated `discord.Embed.Empty`)
- Configured Flask web server on port 5000 for Replit webview
- Set up environment variable support for API key
- Created proper Python .gitignore

## Architecture
The bot uses a platform-independent architecture where:
1. Server wrappers (`discord.py`, `irc.py`) handle platform-specific communication
2. Core bot (`taiiwobot.py`) manages plugins and events
3. Plugins implement commands using the Interface system
4. All platform differences are abstracted in the server wrapper layer
