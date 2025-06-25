import json
import os
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def lambda_handler(event, context):
    try:
        logger.info("SNS Event received:")
        logger.info(json.dumps(event))

        # Leer el mensaje del SNS
        message = event['Records'][0]['Sns']['Message']

        # Enviar a Telegram
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }

        response = requests.post(TELEGRAM_URL, json=payload)
        logger.info(f"Telegram response: {response.text}")

    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise e