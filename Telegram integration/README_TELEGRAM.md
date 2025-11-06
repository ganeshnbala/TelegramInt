# Telegram Bot Integration - Setup Guide

This project integrates a Telegram bot with an AI agent that processes messages, saves results to Excel, and emails them via Gmail.

## Features

- 🤖 Telegram bot integration
- 🧠 AI agent processing
- 📊 Excel export functionality
- 📧 Automatic Gmail email delivery

## Quick Start

### 1. Install Dependencies

```bash
pip install python-telegram-bot openpyxl pandas python-dotenv pyyaml requests beautifulsoup4 google-generativeai faiss-cpu numpy
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the project root:

```env
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# Gmail Configuration
GMAIL_SENDER=your_email@gmail.com
GMAIL_PASSWORD=your_gmail_app_password_here
GMAIL_RECIPIENT=recipient@gmail.com

# Excel Export Configuration
EXCEL_FILE_PATH=exports/agent_results.xlsx
USE_APPEND_MODE=true

# Optional: Google API Key for agent processing
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Get Credentials

**Telegram Bot Token:**
1. Open Telegram and search for @BotFather
2. Send `/newbot` and follow instructions
3. Copy the token

**Gmail App Password:**
1. Go to https://myaccount.google.com/apppasswords
2. Create App Password for "Mail"
3. Copy the 16-character password

**Google API Key (Optional):**
1. Go to https://makersuite.google.com/app/apikey
2. Create API key
3. Add to .env as GOOGLE_API_KEY

### 4. Run the Bot

```bash
python telegram_bot.py
```

Or use the batch file (Windows):
```bash
start_bot.bat
```

## Project Structure

```
Telegram integration/
├── telegram_bot.py          # Main bot application
├── agent.py                 # Agent CLI interface
├── config/
│   ├── profiles.yaml        # Agent configuration
│   └── models.json          # Model configurations
├── core/
│   ├── loop.py             # Agent execution loop
│   ├── session.py          # MCP session management
│   ├── context.py           # Agent context
│   └── strategy.py         # Decision strategy
├── modules/
│   ├── excel_export.py     # Excel export utilities
│   ├── gmail_sender.py     # Gmail sending utilities
│   ├── action.py           # Tool execution
│   ├── decision.py         # Planning logic
│   ├── memory.py           # Memory management
│   ├── perception.py       # Input perception
│   ├── model_manager.py    # Model management
│   └── tools.py            # Tool utilities
├── mcp_server_1.py         # Math operations server
├── mcp_server_2.py         # Document processing server
├── mcp_server_3.py         # Web search server
├── exports/                # Excel files output directory
└── documents/              # Document storage
```

## Usage

### Telegram Bot

1. Start the bot: `python telegram_bot.py`
2. Find your bot on Telegram
3. Send `/start` to begin
4. Send any message - bot will process, save to Excel, and email results

### Helper Scripts

- `setup_telegram.py` - Interactive setup wizard
- `test_telegram_bot.py` - Test configuration
- `test_email.py` - Test email functionality
- `fetch_cities_direct.py` - Example: Fetch data and email
- `send_latest_results.py` - Manually send latest Excel file

## Commands

- `/start` - Welcome message
- `/help` - Show help
- `/status` - Check bot status

## Troubleshooting

**Bot not responding?**
- Check TELEGRAM_BOT_TOKEN in .env
- Make sure bot is running
- Check for error messages in console

**Email not sending?**
- Verify Gmail credentials in .env
- Use App Password, not regular password
- Check spam folder

**Agent not processing?**
- Add GOOGLE_API_KEY to .env
- Check MCP server paths in config/profiles.yaml
- Verify all dependencies are installed

## License

[Add your license here]

