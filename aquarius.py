import os
import ccxt
import pandas as pd
import pandas_ta as ta
import requests
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Connect Binance
exchange = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_API_SECRET
})

def fetch_data(symbol='FET/USDT', timeframe='15m', limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def analyze(df):
    df['EMA20'] = ta.ema(df['close'], length=20)
    df['RSI'] = ta.rsi(df['close'], length=14)

    last = df.iloc[-1]
    previous = df.iloc[-2]

    if last['close'] > last['EMA20'] and last['RSI'] < 70 and previous['close'] < previous['EMA20']:
        return "BUY", last
    elif last['close'] < last['EMA20'] and last['RSI'] > 30 and previous['close'] > previous['EMA20']:
        return "SELL", last
    else:
        return "HOLD", last

def send_signal(signal, last):
    message = f"""
📈 FET/USDT Signal Alert 🔔

Signal: {signal}
Close Price: {last['close']:.4f}
EMA20: {last['EMA20']:.4f}
RSI: {last['RSI']:.2f}
Timeframe: 15m

Reason: Auto analysis via Aquarius 🤖
"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

def main():
    df = fetch_data()
    signal, last = analyze(df)
    if signal != "HOLD":
        send_signal(signal, last)

if __name__ == "__main__":
    main()
