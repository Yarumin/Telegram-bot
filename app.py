from flask import Flask, request
from telegram import Bot, Update
import os

app = Flask(__name__)
bot = Bot(token=os.environ["TELEGRAM_TOKEN"])

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    if update.message:  # فقط پیام‌های متنی رو پردازش کن
        chat_id = update.message.chat.id
        message_id = update.message.message_id
        bot.send_message(chat_id=chat_id, text="سلام", reply_to_message_id=message_id)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
