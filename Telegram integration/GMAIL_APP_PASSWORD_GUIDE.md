# How to Get Gmail App Password - Step by Step Guide

## Prerequisites
- You must have **2-Step Verification** enabled on your Google account
- If you don't have it enabled, you'll need to set it up first

## Step-by-Step Instructions

### Step 1: Enable 2-Step Verification (if not already enabled)

1. Go to your Google Account: https://myaccount.google.com/
2. Click on **Security** (left sidebar)
3. Under "Signing in to Google", find **2-Step Verification**
4. Click on it and follow the prompts to enable it
   - You'll need your phone number
   - Google will send you a verification code

### Step 2: Create App Password

1. **Go directly to App Passwords page:**
   - Visit: https://myaccount.google.com/apppasswords
   - Or navigate: Google Account → Security → 2-Step Verification → App passwords

2. **If prompted, sign in to your Google account**

3. **Select App:**
   - Click the dropdown under "Select app"
   - Choose **"Mail"**

4. **Select Device:**
   - Click the dropdown under "Select device"
   - Choose **"Other (Custom name)"**
   - Type: **"Agent Bot"** (or any name you prefer)
   - Click **"Generate"**

5. **Copy the Password:**
   - Google will show you a **16-character password**
   - It will look like: `abcd efgh ijkl mnop`
   - **Important:** Copy it exactly as shown (you can remove spaces when using it)
   - Click **"Done"**

### Step 3: Add to .env File

1. Open the `.env` file in the `S8 Share` folder
2. Find the line: `GMAIL_PASSWORD=`
3. Add your 16-character password (remove spaces):
   ```
   GMAIL_PASSWORD=abcdefghijklmnop
   ```
4. Save the file

## Quick Method (Direct Link)

**Fastest way:** Just click this link and follow steps 3-5 above:
👉 https://myaccount.google.com/apppasswords

## Troubleshooting

### "App passwords" option not showing?
- Make sure 2-Step Verification is enabled
- Wait a few minutes after enabling 2-Step Verification
- Try refreshing the page

### "This feature is not available for your account"?
- Your Google account might be a work/school account
- Some organizations disable App Passwords
- Contact your IT administrator

### Password not working?
- Make sure you copied the entire 16-character password
- Remove any spaces when pasting
- Make sure you're using the App Password, not your regular Gmail password

## Security Note

- App Passwords are more secure than using your regular password
- You can revoke App Passwords anytime from the same page
- Each App Password is unique and can be used for one application

## After Adding the Password

Once you've added the password to `.env`, you can:
1. Test the configuration: `python test_telegram_bot.py`
2. Start the bot: `python telegram_bot.py`
3. The bot will now send Excel files to your email!

