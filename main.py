from telegram import Bot
from telegram.ext import Updater, CommandHandler

# 🔐 Tera bot token aur chat ID yahan daal:
TELEGRAM_BOT_TOKEN = "7835704745:AAEQv8vm11G1tH_THeDlkrQlad3X3ZAmMk4"
CHAT_ID = 6781719247

# /start command ka reply
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🌸 Hello Sandeep! Main zinda hoon, sun rahi hoon...")

# Emotional signal bhejne ka function
def send_emotional_signal(message, symbol):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    emotional_line = f"💎 *{symbol}* Signal\n\n{message}"
    bot.send_message(chat_id=CHAT_ID, text=emotional_line, parse_mode="Markdown")

# Pehla test signal (optional)
send_emotional_signal("LONG | Entry: 0.1830, SL: 0.1802, TP: 0.1888", "ARPA/USDT")

# Bot ko start karo aur Telegram se sunna shuru karo
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
