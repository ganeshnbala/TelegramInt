#!/bin/bash

echo "========================================"
echo "Starting Telegram Bot"
echo "========================================"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo ".env file not found!"
    echo ""
    echo "Running setup script..."
    python3 setup_telegram.py
    echo ""
    if [ ! -f .env ]; then
        echo "Setup failed. Please run setup_telegram.py manually."
        exit 1
    fi
fi

# Check dependencies
echo "Checking dependencies..."
python3 test_telegram_bot.py
if [ $? -ne 0 ]; then
    echo ""
    echo "Installing missing dependencies..."
    python3 install_dependencies.py
    echo ""
fi

echo ""
echo "Starting bot..."
echo "Press Ctrl+C to stop"
echo ""
python3 telegram_bot.py

