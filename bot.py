import requests
import time
import os
from datetime import datetime

# Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8293571628:AAE4...")
CHAT_ID = os.getenv("CHAT_ID", "5428245719")
CRICKET_API_KEY = os.getenv("CRICKET_API_KEY", "18d2a487-62de-4571-afa6-2609e1ba5ae0")

def get_cricket_scores():
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={CRICKET_API_KEY}&offset=0"
    response = requests.get(url)
    return response.json()

def format_message(data):
    message = "🏏 *LIVE CRICKET SCORES* 🏏\n\n"
    
    live_matches = [m for m in data['data'] if not m['matchEnded']]
    
    if live_matches:
        for match in live_matches[:3]:
            message += f"🔴 *{match['name']}*\n"
            message += f"📍 {match['venue']}\n"
            message += f"📊 {match['status']}\n"
            
            if 'score' in match and match['score']:
                for score in match['score']:
                    message += f"   {score['inning']}: {score['r']}/{score['w']} ({score['o']} ov)\n"
            message += "\n"
    else:
        message += "No live matches currently 🏏\n"
    
    message += f"\n⏰ Updated: {datetime.now().strftime('%I:%M %p')}"
    return message

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def main():
    print("🏏 Cricket Bot Started!")
    while True:
        try:
            data = get_cricket_scores()
            message = format_message(data)
            send_telegram_message(message)
            print(f"✅ Update sent at {datetime.now()}")
            time.sleep(600)
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
