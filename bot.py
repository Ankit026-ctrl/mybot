import telegram
import time
import config
import requests

bot = telegram.Bot(token=config.TELEGRAM_API_TOKEN)

def send_message(text):
    bot.send_message(chat_id=config.CHANNEL_ID, text=text)

def get_subscribers_count():
    url = f"https://api.telegram.org/bot{config.TELEGRAM_API_TOKEN}/getChatMembersCount?chat_id={config.CHANNEL_ID}"
    response = requests.get(url)
    return response.json()['result']

while True:
    subscribers_count = get_subscribers_count()
    if subscribers_count % 100 == 0:
        message = f"Hurray!! , We've reached {subscribers_count} subscribers!"
        send_message(message)
    time.sleep(100)

