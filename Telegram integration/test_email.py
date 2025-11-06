# test_email.py
# Test Gmail sending functionality

import os
from dotenv import load_dotenv
from modules.gmail_sender import send_excel_to_gmail
from modules.excel_export import create_excel_from_result

load_dotenv()

print("=" * 60)
print("Testing Email Functionality")
print("=" * 60)
print()

# Check configuration
sender = os.getenv("GMAIL_SENDER")
password = os.getenv("GMAIL_PASSWORD")
recipient = os.getenv("GMAIL_RECIPIENT")

print(f"Gmail Sender: {sender}")
print(f"Gmail Recipient: {recipient}")
print(f"Password configured: {'Yes' if password else 'No'}")
print()

# Create a test Excel file
print("Creating test Excel file...")
test_excel = create_excel_from_result(
    user_message="Test message from bot",
    agent_response="This is a test response to verify email functionality",
    metadata={"Test": "Email Test", "Status": "Working"}
)
print(f"✅ Excel file created: {test_excel}")
print()

# Try sending email
print("Attempting to send email...")
try:
    success = send_excel_to_gmail(
        excel_path=test_excel,
        recipient_email=recipient,
        subject="Test Email from Telegram Bot",
        body="This is a test email to verify the bot's email functionality is working correctly."
    )
    
    if success:
        print("✅ Email sent successfully!")
        print(f"📧 Check your inbox at: {recipient}")
        print("   (Also check spam/junk folder if not in inbox)")
    else:
        print("❌ Email sending failed")
        print("   Check the error messages above for details")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nPossible issues:")
    print("1. Gmail App Password might be incorrect")
    print("2. 2-Step Verification might not be enabled")
    print("3. Network/firewall issues")
    print("4. Gmail account restrictions")

print()
print("=" * 60)

