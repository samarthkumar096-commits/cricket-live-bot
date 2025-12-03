# 🏏 Cricket Live Score Bot

24/7 Telegram bot that sends live cricket scores automatically every 10 minutes.

## Features
- ✅ Live cricket scores from all matches
- ✅ Automatic updates every 10 minutes
- ✅ Formatted messages with emojis
- ✅ 24/7 uptime on Railway

## Deploy on Railway

1. Fork this repository
2. Go to [Railway](https://railway.app)
3. Create new project from GitHub repo
4. Add environment variables:
   - `TELEGRAM_BOT_TOKEN`
   - `CHAT_ID`
   - `CRICKET_API_KEY`
5. Deploy!

## Environment Variables

```
TELEGRAM_BOT_TOKEN=your_bot_token
CHAT_ID=your_chat_id
CRICKET_API_KEY=your_cricket_api_key
```

## Local Testing

```bash
pip install -r requirements.txt
python bot.py
```

## API Credits
- Cricket API: [CricAPI](https://cricapi.com)
- Telegram Bot API

---
Made with ❤️ for cricket fans
