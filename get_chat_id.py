from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(f"\n{'='*50}")
    print(f"Your Chat ID is: {chat_id}")
    print(f"{'='*50}")
    print(f"Add this to your .env file:")
    print(f"CHAT_ID={chat_id}")
    print(f"{'='*50}\n")
    await update.message.reply_text(f"Your Chat ID is: {chat_id}")

app = ApplicationBuilder().token("8427903396:AAEXuezJCx-U41YXo0_RgvVNWMhl86zDj-M").build()
app.add_handler(MessageHandler(filters.ALL, get_chat_id))
app.run_polling()
