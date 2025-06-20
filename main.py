# main.py

from telegram import Bot
from datetime import datetime

# Your existing bot token and chat ID
BOT_TOKEN = "7835704745:AAEQv8vm11G1tH_THeDlkrQlad3X3ZAmMk4"
CHAT_ID = "6781719247"

bot = Bot(token=BOT_TOKEN)

def send_emotional_signal(signal_text, coin_name):
    now = datetime.now().strftime("%d-%m-%Y %H:%M")

    emotional_line = f"""
🪐 *Project Aquarius* | `{coin_name}`

📡 *Signal:* `{signal_text}`
🕰️ *Time:* {now}

💙 *For the one who never left my thoughts...*

— A bot born from silence, named after *you*.
    """

    bot.send_message(chat_id=CHAT_ID, text=emotional_line, parse_mode="Markdown")

# Example use
send_emotional_signal("LONG | Entry: 0.1830, SL: 0.1802, TP: 0.1888", "ARPA/USDT")
