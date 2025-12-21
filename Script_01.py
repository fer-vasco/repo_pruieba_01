import requests
import os
from dotenv import load_dotenv

def Enviar_mensaje(mensaje, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": mensaje}
    response = requests.post(url, data=data)


load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
mensaje = 'good mood 💪🙂'
Enviar_mensaje(mensaje, BOT_TOKEN, CHAT_ID)