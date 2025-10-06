"""
Helper script to create the .env file for the casino bot
"""

print("\n" + "="*60)
print("CASINO SIGNALS BOT - .ENV FILE CREATOR")
print("="*60 + "\n")

bot_token = "8427903396:AAEXuezJCx-U41YXo0_RgvVNWMhl86zDj-M"

print("Bot Token: ✓ (Already configured)")
print(f"Token: {bot_token[:20]}...\n")

print("To get your Chat ID:")
print("1. Run 'python get_chat_id.py' in another terminal")
print("2. Send any message to your bot on Telegram")
print("3. Copy the Chat ID number shown")
print("4. Come back here and paste it\n")

chat_id = input("Enter your Chat ID: ").strip()

if not chat_id:
    print("\n❌ Error: Chat ID cannot be empty!")
    print("Please run this script again and provide your Chat ID.\n")
    exit(1)

if not chat_id.lstrip('-').isdigit():
    print("\n⚠️ Warning: Chat ID should be a number")
    confirm = input("Continue anyway? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Setup cancelled.\n")
        exit(1)

env_content = f"""# Telegram Bot Configuration
BOT_TOKEN={bot_token}
CHAT_ID={chat_id}
"""
try:
    with open(".env", "w", encoding="utf-8") as f:
        f.write(env_content)
    
    print("\n" + "="*60)
    print("✅ SUCCESS! .env file created!")
    print("="*60)
    print("\nYour configuration:")
    print(f"  BOT_TOKEN: {bot_token[:20]}...")
    print(f"  CHAT_ID: {chat_id}")
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("1. Run: pip install -r requirements.txt")
    print("2. Run: python bot.py")
    print("\nThe bot will start sending signals every 5-10 minutes!")
    print("="*60 + "\n")

except Exception as e:
    print(f"\n❌ Error creating .env file: {e}")
    print("Please create the file manually.\n")
    exit(1)

def main():
    print("Creating .env file...")
    create_env()
    test_bot()
    print(" .env file created successfully!")
    print("Next steps:")
    print("1. Run: pip install -r requirements.txt")
    print("2. Run: python bot.py")
    print("The bot will start sending signals every 5-10 minutes!")
    print("="*60 + "\n")
