# 🚀 START HERE - Telegram Bot Setup

Follow these steps in order to get your Telegram bot running:

## Step 1: Install Dependencies

Run this command to install all required packages:

```bash
python install_dependencies.py
```

Or manually:
```bash
pip install python-telegram-bot openpyxl pandas python-dotenv
```

## Step 2: Configure Your Bot

Run the interactive setup script:

```bash
python setup_telegram.py
```

This will guide you through:
- Getting your Telegram bot token from @BotFather
- Setting up Gmail App Password
- Configuring email recipient
- Setting Excel file path

**What you'll need:**
1. **Telegram Bot Token**: 
   - Open Telegram → Search @BotFather
   - Send `/newbot` and follow instructions
   - Copy the token

2. **Gmail App Password**:
   - Go to https://myaccount.google.com/apppasswords
   - Create App Password for "Mail"
   - Copy the 16-character password (no spaces)

## Step 3: Test Your Configuration

Verify everything is set up correctly:

```bash
python test_telegram_bot.py
```

This will check:
- ✅ All environment variables are set
- ✅ All dependencies are installed
- ✅ Excel directory can be created

## Step 4: Start the Bot

```bash
python telegram_bot.py
```

You should see:
```
INFO - Starting Telegram bot...
INFO - Application started
```

## Step 5: Use Your Bot on Telegram

1. Open Telegram app
2. Search for your bot (the username you created)
3. Click **Start** or send `/start`
4. Send any message to test it!

## Quick Commands

- `/start` - Welcome message
- `/help` - Show help
- `/status` - Check bot status

## Troubleshooting

**Bot not responding?**
- Check that the bot script is running
- Verify TELEGRAM_BOT_TOKEN in .env file
- Make sure you're messaging the correct bot

**Email not sending?**
- Verify Gmail credentials in .env
- Make sure you're using App Password (not regular password)
- Check that 2-Step Verification is enabled

**Need help?**
- Check `QUICK_START.md` for detailed instructions
- Check `TELEGRAM_SETUP.md` for advanced configuration

