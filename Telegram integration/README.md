# S8 Share - AI Agent with Telegram Integration

An AI agent system that processes queries through multiple MCP (Model Context Protocol) servers and can be accessed via Telegram.

## Features

- 🤖 AI Agent with reasoning capabilities
- 🔧 Multiple MCP server support (Math, Documents, Web Search)
- 📱 Telegram bot integration
- 📊 Excel export of results
- 📧 Automatic email delivery via Gmail

## Project Structure

```
S8 Share/
├── agent.py              # Main agent entry point (CLI)
├── telegram_bot.py       # Telegram bot entry point
├── config/
│   ├── profiles.yaml     # Agent configuration
│   └── models.json       # Model configurations
├── core/
│   ├── loop.py           # Agent execution loop
│   ├── session.py        # MCP session management
│   ├── context.py        # Agent context
│   └── strategy.py       # Decision strategy
├── modules/
│   ├── excel_export.py   # Excel export utilities
│   ├── gmail_sender.py   # Gmail sending utilities
│   ├── action.py         # Tool execution
│   ├── decision.py       # Planning logic
│   ├── memory.py         # Memory management
│   ├── perception.py     # Input perception
│   └── tools.py          # Tool utilities
├── mcp_server_1.py        # Math operations server
├── mcp_server_2.py       # Document processing server
├── mcp_server_3.py       # Web search server
└── documents/            # Document storage
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
# or
uv sync
```

2. Set up environment variables (see `TELEGRAM_SETUP.md` for details):
   - Create a `.env` file with your Telegram bot token and Gmail credentials

## Usage

### CLI Mode

Run the agent interactively:
```bash
python agent.py
```

### Telegram Bot Mode

Start the Telegram bot:
```bash
python telegram_bot.py
```

Then interact with your bot on Telegram. The bot will:
1. Process your messages through the AI agent
2. Save results to an Excel file
3. Email the results to the configured Gmail address

## Configuration

See `TELEGRAM_SETUP.md` for detailed setup instructions for:
- Creating a Telegram bot
- Setting up Gmail App Password
- Configuring environment variables

## MCP Servers

The agent uses three MCP servers:

1. **Math Server** (`mcp_server_1.py`): Mathematical operations
2. **Documents Server** (`mcp_server_2.py`): Document search and processing
3. **Web Search Server** (`mcp_server_3.py`): Web search capabilities

Configure these in `config/profiles.yaml`.

## License

[Add your license here]

