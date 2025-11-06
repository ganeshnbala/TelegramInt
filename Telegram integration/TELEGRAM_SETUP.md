# Telegram Bot Setup Guide

This guide will help you set up the Telegram bot integration for the Agent.

## Prerequisites

1. Python 3.11 or higher
2. A Telegram account
3. A Gmail account with App Password enabled

## Step 1: Install Dependencies

```bash
# Install the new dependencies
pip install python-telegram-bot openpyxl pandas python-dotenv
```

Or if using uv:
```bash
uv sync
```

## Step 2: Create a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token you receive (it will look like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Step 3: Get Gmail App Password

1. Go to your Google Account settings: https://myaccount.google.com/
2. Navigate to Security → 2-Step Verification (enable it if not already enabled)
3. Go to App Passwords: https://myaccount.google.com/apppasswords
4. Select "Mail" and "Other (Custom name)" 
5. Enter a name like "Agent Bot"
6. Copy the 16-character app password (it will look like: `abcd efgh ijkl mnop`)

## Step 4: Create Environment File

Create a `.env` file in the project root with the following content:

```env
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# Gmail Configuration
GMAIL_SENDER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password_here
GMAIL_RECIPIENT=recipient@gmail.com

# Excel Export Configuration
EXCEL_FILE_PATH=exports/agent_results.xlsx
USE_APPEND_MODE=true
```

Replace the placeholder values with your actual credentials.

## Step 5: Run the Bot

```bash
python telegram_bot.py
```

Or if you're in the S8 Share directory:
```bash
cd "S8 Share"
python telegram_bot.py
```

## Usage

1. Open Telegram and search for your bot (the username you gave it)
2. Send `/start` to begin
3. Send any message/question to the bot
4. The bot will:
   - Process your message through the agent
   - Save results to an Excel file
   - Email the Excel file to the configured Gmail address

## Commands

- `/start` - Start the bot and see welcome message
- `/help` - Show help message
- `/status` - Check bot status and configuration

## Configuration Options

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token from BotFather
- `GMAIL_SENDER`: Your Gmail address
- `GMAIL_PASSWORD`: Your Gmail app password (16 characters, no spaces)
- `GMAIL_RECIPIENT`: Email address to receive the Excel files
- `EXCEL_FILE_PATH`: Path where Excel files will be saved
- `USE_APPEND_MODE`: Set to `true` to append all results to one file, `false` to create separate files

## Troubleshooting

### Bot not responding
- Check that `TELEGRAM_BOT_TOKEN` is correct
- Make sure the bot is running

### Email not sending
- Verify Gmail credentials are correct
- Make sure you're using an App Password, not your regular password
- Check that 2-Step Verification is enabled on your Google account

### Excel file not created
- Check that the `exports` directory exists or can be created
- Verify file permissions

### Agent not processing
- Ensure all MCP servers are properly configured in `config/profiles.yaml`
- Check that the agent dependencies are installed

