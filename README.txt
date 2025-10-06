================================================================================
                        CASINO SIGNALS TELEGRAM BOT
                              Bac Bo Game Signals
================================================================================

DESCRIPTION
-----------
This is an automated Telegram bot that sends betting signals for the Bac Bo 
casino game 24/7. The bot analyzes patterns and sends recommendations for 
which color to bet on (Red or Blue), with tie protection (Yellow).

The bot includes a Gale (martingale) system with up to 2 attempts per signal,
and sends all messages in Portuguese.


FEATURES
--------
✓ 24/7 Automated Operation - Runs continuously without manual intervention
✓ Smart Analysis - Simulates game analysis before sending signals
✓ Random Color Prediction - Recommends Red (🔴) or Blue (🔵) betting
✓ Tie Protection - Always protects with Yellow (🟡)
✓ Gale System - Supports up to 2 Gales (martingale retry strategy)
✓ Result Tracking - Shows win/loss with motivational messages
✓ Casino Integration - Includes affiliate casino link
✓ Activity Logging - All signals and results logged to log.txt
✓ Portuguese Language - All messages in Portuguese


HOW IT WORKS
------------
1. ANALYSIS PHASE (30-60 seconds)
   Bot sends: "O HACKER ESTÁ A ANALISAR UMA POSSÍVEL ENTRADA…🧑‍💻"

2. SIGNAL ENTRY
   Bot sends betting signal with color and tie protection
   Includes casino link for players

3. RESULT TRACKING (20-40 seconds per attempt)
   - First attempt result checked
   - If loss: Bot suggests 1st Gale
   - If loss again: Bot suggests 2nd Gale
   - Final result: Victory or Loss message

4. WAIT PERIOD (5-10 minutes)
   Bot waits before sending next signal

5. REPEAT
   Cycle continues indefinitely (24/7)


INSTALLATION
------------
1. Install Python 3.7 or higher
2. Install dependencies:
   
   pip install -r requirements.txt


CONFIGURATION
-------------
1. Get your Telegram Chat ID:
   
   python get_chat_id.py
   
   Then send any message to your bot on Telegram.
   Copy the Chat ID number displayed.

2. Create a file named ".env" in the project folder with:
   
   BOT_TOKEN=8427903396:AAEXuezJCx-U41YXo0_RgvVNWMhl86zDj-M
   CHAT_ID=your_chat_id_here
   
   Replace "your_chat_id_here" with the Chat ID from step 1.

   (OR run "python create_env.py" for guided setup)


TESTING
-------
Before running the main bot, test your configuration:

python test_bot.py

This will verify:
- .env file exists
- Bot token and Chat ID are valid
- Bot can connect to Telegram
- Messages can be sent successfully


RUNNING THE BOT
---------------
Start the bot with:

python bot.py

The bot will run continuously and send signals every 5-10 minutes.
Press Ctrl+C to stop the bot.


BOT MESSAGES
------------
The bot sends these messages in Portuguese:

• "O HACKER ESTÁ A ANALISAR UMA POSSÍVEL ENTRADA…🧑‍💻"
  (Analyzing the next signal)

• "A.I DO TIO XICO\nENTRADA CONFIRMADA\nJOGA NA COR: [color]\nPROTEGE NO EMPATE: 🟡"
  (Entry confirmed with color recommendation)

• "🎲 Faça o 1º GALE" / "🎲 Faça o 2º GALE"
  (Gale suggestions)

• "VITÓRIA ✅\nBATESTE A TUA META? RETIRA O TEU LUCRO E VOLTA AMANHÃ 🙏🏻🧠"
  (Victory message)

• "INFELIZMENTE NÃO SE GANHA SEMPRE❌"
  (Loss message)

• Casino link with each signal


PROJECT FILES
-------------
bot.py              - Main bot application (run this)
config.py           - Configuration loader (loads .env file)
get_chat_id.py      - Helper script to get your Telegram Chat ID
create_env.py       - Interactive .env file creator
test_bot.py         - Configuration and connectivity tester
requirements.txt    - Python package dependencies
.env                - Your configuration (create this)
.gitignore          - Git ignore rules (protects sensitive data)
log.txt             - Activity log (created when bot runs)


TECHNICAL DETAILS
-----------------
• Language: Python 3.7+
• Framework: python-telegram-bot
• Win Rate: ~40% (realistic casino simulation)
• Signal Frequency: Every 5-10 minutes
• Max Gales: 2 per signal
• Casino: https://track.intrklnkmain.com/visit/?bta=52152&brand=bdmbet


TROUBLESHOOTING
---------------
Problem: Bot doesn't send messages
Solution: 
  - Verify .env file exists with BOT_TOKEN and CHAT_ID
  - Make sure you've sent at least one message to your bot first
  - Run test_bot.py to diagnose issues

Problem: "Chat not found" error
Solution:
  - Open Telegram and send any message to your bot first
  - Then run the bot again

Problem: Import errors
Solution:
  - Run: pip install -r requirements.txt

Problem: Bot crashes
Solution:
  - Check log.txt for error details
  - Verify internet connection is stable
  - Restart with: python bot.py


DEPLOYMENT FOR 24/7 OPERATION
------------------------------
For true 24/7 operation, deploy to a server:

Option 1: VPS/Cloud Server (DigitalOcean, AWS, etc.)
  - Upload project files
  - Install Python and dependencies
  - Run bot in screen/tmux session

Option 2: Heroku (Free/Paid)
  - Create Procfile: worker: python bot.py
  - Add environment variables (BOT_TOKEN, CHAT_ID)
  - Deploy and scale worker dyno

Option 3: Your Computer (24/7)
  - Keep computer running
  - Run bot in background
  - Ensure no sleep/hibernate


NOTES
-----
• Bot simulates game results (cannot connect to real casino without API)
• Uses 40% win rate to simulate realistic casino odds
• Colors are selected randomly (50/50 Red or Blue)
• All activity is logged to log.txt with timestamps
• Bot must stay running for 24/7 operation


SUPPORT
-------
For issues or questions, check:
1. log.txt for error messages
2. Verify .env configuration is correct
3. Test connection with test_bot.py
4. Ensure bot token and chat ID are valid


================================================================================
                      Bot ready to send casino signals 24/7!
================================================================================

