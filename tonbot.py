import time
import requests

BOT_TOKEN = "8570005871:AAEQTrjuSrBGQCsJW81oqKHSvfjgez03tXE"  
CHANNEL_ID = "@priceton2"

def get_ton_price_usd():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd"
    data = requests.get(url, timeout=10).json()
    return data["the-open-network"]["usd"]

def get_usd_to_irt():
    url = "https://api.tgju.org/v1/market/gold/sana/data"
    data = requests.get(url, timeout=10).json()
    price = int(data["data"]["price"])
    return price

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload, timeout=10)

while True:
    try:
        ton_usd = get_ton_price_usd()
        dollar_toman = get_usd_to_irt()
        ton_toman = ton_usd * dollar_toman

        msg = f"""
💎 <b>TON Price Update</b>

🇺🇸 قیمت دلاری: {ton_usd} $
🇮🇷 قیمت تومانی: {int(ton_toman):,} تومان

(آپدیت خودکار هر ۳ دقیقه)
"""

        send_message(msg)
        print("Sent:", msg)

    except Exception as e:
        print("Error:", e)

    time.sleep(180)
