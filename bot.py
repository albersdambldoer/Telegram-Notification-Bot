import asyncio
import random
from datetime import datetime
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=BOT_TOKEN)

CASINO_LINK = "https://track.intrklnkmain.com/visit/?bta=52152&brand=bdmbet"

# Messages in Portuguese as requested by client
MSG_ANALYZING = "O HACKER ESTÁ A ANALISAR UMA POSSÍVEL ENTRADA…🧑‍💻"
MSG_ENTRY = "A.I DO TIO XICO\nENTRADA CONFIRMADA\nJOGA NA COR: {color}\nPROTEGE NO EMPATE: 🟡"
MSG_GALE_1 = "🎲 Faça o 1º GALE"
MSG_GALE_2 = "🎲 Faça o 2º GALE"
MSG_VICTORY = "VITÓRIA ✅\nBATESTE A TUA META? RETIRA O TEU LUCRO E VOLTA AMANHÃ 🙏🏻🧠"
MSG_LOSS = "INFELIZMENTE NÃO SE GANHA SEMPRE❌"
MSG_CASINO = f"💰🤖 [JOGUE AGORA]({CASINO_LINK}) 🤖💰"

# Colors
COLORS = ["🔴", "🔵"]

async def send_message(text, parse_mode='Markdown'):
    """Send a message to the Telegram chat"""
    try:
        await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode=parse_mode)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Sent: {text[:50]}...")
        with open("log.txt", "a", encoding="utf-8") as log:
            log.write(f"[{timestamp}] {text}\n")
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False

async def simulate_game_result():
    """Simulate a game result (win or loss)"""
    # 40% chance to win (realistic casino odds)
    return random.random() < 0.40

async def run_betting_cycle():
    """Run one complete betting cycle with analysis, entry, and result"""
    
    # Step 1: Send analyzing message
    await send_message(MSG_ANALYZING)
    await asyncio.sleep(random.randint(30, 60))  # Wait 30-60 seconds while "analyzing"
    
    # Step 2: Send entry signal with random color
    selected_color = random.choice(COLORS)
    entry_msg = MSG_ENTRY.format(color=selected_color)
    await send_message(entry_msg)
    await asyncio.sleep(5)
    
    # Step 3: Send casino link
    await send_message(MSG_CASINO)
    await asyncio.sleep(random.randint(20, 40))  # Wait for "game result" 20-40 seconds
    
    # Step 4: Check result and handle Gales (max 2)
    max_gales = 2
    gale_count = 0
    won = False
    
    # First attempt
    if await simulate_game_result():
        won = True
    else:
        # Try Gales
        for gale in range(1, max_gales + 1):
            gale_count = gale
            if gale == 1:
                await send_message(MSG_GALE_1)
            elif gale == 2:
                await send_message(MSG_GALE_2)
            
            await asyncio.sleep(random.randint(20, 40))  # Wait for game result
            
            if await simulate_game_result():
                won = True
                break
    
    # Step 5: Send final result
    await asyncio.sleep(3)
    if won:
        await send_message(MSG_VICTORY)
    else:
        await send_message(MSG_LOSS)
    
    # Log the cycle
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = "WIN" if won else "LOSS"
    log_msg = f"[{timestamp}] Cycle complete: {result} (Color: {selected_color}, Gales: {gale_count})\n"
    print(log_msg.strip())
    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(log_msg)

async def run_bot_forever():
    """Main loop - runs the bot 24/7"""
    print("🤖 Bot started! Running 24/7...")
    print(f"Bot Token: {BOT_TOKEN[:20]}...")
    print(f"Chat ID: {CHAT_ID}")
    print("-" * 50)
    
    cycle_number = 0
    
    while True:
        try:
            cycle_number += 1
            print(f"\n{'='*50}")
            print(f"Starting cycle #{cycle_number}")
            print(f"{'='*50}")
            
            await run_betting_cycle()
            
            # Wait before next cycle (5-10 minutes)
            wait_time = random.randint(300, 600)  # 5-10 minutes
            print(f"\n⏳ Waiting {wait_time//60} minutes before next signal...")
            await asyncio.sleep(wait_time)
            
        except Exception as e:
            print(f"❌ Error in cycle: {e}")
            await asyncio.sleep(60)  # Wait 1 minute before retrying

if __name__ == "__main__":
    asyncio.run(run_bot_forever())
