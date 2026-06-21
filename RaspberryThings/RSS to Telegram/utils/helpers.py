import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(
        filename="logs/bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log(msg):
    logging.info(msg)

def clean_text(text):
    return text.replace("\n", " ").strip()

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
