import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Aquarius is alive 🌊✨")

def send_signal(update, context):
    message = "📈 Buy ETH/USDT\n💰 Entry: 3300\n🎯 Target: 3450\n🛑 SL: 3240"
    context.bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    bot = Bot(token=BOT_TOKEN)
    updater = Updater(bot=bot, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("signal", send_signal))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
