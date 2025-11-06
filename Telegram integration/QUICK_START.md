# Quick Start Guide - Telegram Bot

## Step 1: Get Your Telegram Bot Token

1. Open Telegram app (mobile or web)
2. Search for **@BotFather** (official Telegram bot creator)
3. Send `/newbot` command
4. Follow the prompts:
   - Choose a name for your bot (e.g., "My AI Agent")
   - Choose a username (must end with 'bot', e.g., "my_ai_agent_bot")
5. **Copy the token** BotFather gives you (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Step 2: Get Gmail App Password

1. Go to https://myaccount.google.com/security
2. Enable **2-Step Verification** if not already enabled
3. Go to **App Passwords**: https://myaccount.google.com/apppasswords
4. Select:
   - App: **Mail**
   - Device: **Other (Custom name)**
   - Name: "Agent Bot"
5. Click **Generate**
6. **Copy the 16-character password** (remove spaces when using it)

## Step 3: Create .env File

Create a file named `.env` in the `S8 Share` directory with this content:

```env
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
GMAIL_SENDER=your_email@gmail.com
GMAIL_PASSWORD=abcdefghijklmnop
GMAIL_RECIPIENT=recipient@gmail.com
EXCEL_FILE_PATH=exports/agent_results.xlsx
USE_APPEND_MODE=true
```

**Replace with your actual values:**
- `TELEGRAM_BOT_TOKEN`: The token from Step 1
- `GMAIL_SENDER`: Your Gmail address
- `GMAIL_PASSWORD`: The 16-character app password from Step 2 (no spaces)
- `GMAIL_RECIPIENT`: Where you want to receive the Excel files

## Step 4: Install Dependencies

```bash
cd "S8 Share"
pip install python-telegram-bot openpyxl pandas python-dotenv
```

Or if using uv:
```bash
uv sync
```

## Step 5: Start the Bot

```bash
python telegram_bot.py
```

You should see:
```
INFO - Starting Telegram bot...
INFO - Application started
```

## Step 6: Use the Bot on Telegram

1. Open Telegram app
2. Search for your bot by its username (the one you created in Step 1)
3. Click **Start** or send `/start`
4. Send any message/question, for example:
   - "What is the capital of India?"
   - "Find information about cricket"
   - "Calculate 5 + 3"

The bot will:
- ✅ Process your message
- ✅ Show you the result
- ✅ Save to Excel file
- ✅ Email the Excel file to the recipient

## Commands

- `/start` - Welcome message
- `/help` - Show help
- `/status` - Check bot configuration

## Troubleshooting

**Bot not responding?**
- Check that `TELEGRAM_BOT_TOKEN` is correct in `.env`
- Make sure the bot script is running
- Verify you're messaging the correct bot

**Email not sending?**
- Verify Gmail credentials in `.env`
- Make sure you're using App Password, not regular password
- Check that 2-Step Verification is enabled

**Excel file not created?**
- Check that the `exports` directory can be created
- Verify file permissions

