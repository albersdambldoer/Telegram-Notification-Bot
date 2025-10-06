"""
Quick test script to verify the bot configuration and connectivity
Run this before running the main bot to check if everything is set up correctly
"""

import asyncio
import os
from telegram import Bot

def check_env_file():
    """Check if .env file exists"""
    print("\n[1/4] Checking .env file...")
    if not os.path.exists(".env"):
        print("    ❌ .env file not found!")
        print("    → Run 'python create_env.py' to create it")
        return False
    print("    ✓ .env file exists")
    return True

def check_env_variables():
    """Check if environment variables are loaded"""
    print("\n[2/4] Checking environment variables...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    if not bot_token:
        print("    ❌ BOT_TOKEN not found in .env")
        return False
    if not chat_id:
        print("    ❌ CHAT_ID not found in .env")
        print("    → Run 'python get_chat_id.py' to get your Chat ID")
        return False
    
    print(f"    ✓ BOT_TOKEN: {bot_token[:20]}...{bot_token[-5:]}")
    print(f"    ✓ CHAT_ID: {chat_id}")
    return True

async def test_bot_connection():
    """Test if bot can connect to Telegram"""
    print("\n[3/4] Testing bot connection...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv("BOT_TOKEN")
    
    try:
        bot = Bot(token=bot_token)
        bot_info = await bot.get_me()
        print(f"    ✓ Bot connected: @{bot_info.username}")
        print(f"    ✓ Bot name: {bot_info.first_name}")
        return True
    except Exception as e:
        print(f"    ❌ Connection failed: {e}")
        return False

async def test_send_message():
    """Test sending a message"""
    print("\n[4/4] Testing message sending...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    try:
        bot = Bot(token=bot_token)
        test_msg = "🧪 TEST MESSAGE\n\nBot configuration is working!\n\nYou can now run: python bot.py"
        await bot.send_message(chat_id=chat_id, text=test_msg)
        print("    ✓ Test message sent successfully!")
        print("    → Check your Telegram to see the test message")
        return True
    except Exception as e:
        print(f"    ❌ Failed to send message: {e}")
        if "chat not found" in str(e).lower():
            print("    → Make sure you've sent a message to the bot first")
        return False

async def run_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("CASINO SIGNALS BOT - CONFIGURATION TEST")
    print("="*60)
    
    # Check .env file
    if not check_env_file():
        print("\n" + "="*60)
        print("❌ TESTS FAILED - Please create .env file")
        print("="*60)
        return False
    
    # Check environment variables
    if not check_env_variables():
        print("\n" + "="*60)
        print("❌ TESTS FAILED - Please check .env configuration")
        print("="*60)
        return False
    
    # Test bot connection
    if not await test_bot_connection():
        print("\n" + "="*60)
        print("❌ TESTS FAILED - Cannot connect to Telegram")
        print("="*60)
        return False
    
    # Test sending message
    if not await test_send_message():
        print("\n" + "="*60)
        print("❌ TESTS FAILED - Cannot send messages")
        print("="*60)
        return False
    
    # All tests passed!
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED!")
    print("="*60)
    print("\nYour bot is configured correctly and ready to run!")
    print("\nNext step: Run the bot with 'python bot.py'")
    print("="*60 + "\n")
    return True

if __name__ == "__main__":
    try:
        asyncio.run(run_tests())
    except KeyboardInterrupt:
        print("\n\nTest cancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

