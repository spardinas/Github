import json
from utils.parser import parse_feed
from utils.summarizer import summarize
from utils.telegram import send_message, send_photo
from utils.helpers import log, setup_logger

# Set timeout to avoid broken feeds to hang the bot
import socket
socket.setdefaulttimeout(10)

# Telegram bot configuration
TOKEN = "XXXXXXXX:YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
CHAT_ID = "-ZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

# Load feeds and state from JSON files
def load_feeds():
    with open("feeds.json") as f:
        return json.load(f)["feeds"]

def load_state():
    try:
        with open("state.json") as f:
            return json.load(f)
    except:
        return {}

def save_state(state):
    with open("state.json", "w") as f:
        json.dump(state, f, indent=2)

def build_message(item):
    title = item["title"]
    summary = summarize(item["summary"])
    link = item["link"]

    msg = f"<b>{title}</b>\n"
    msg += f"{summary}\n\n"
    msg += f'<a href="{link}">Open article</a>'

    return msg

def main():
    setup_logger()
    log("Bot started")

    feeds = load_feeds()
    state = load_state()
    total_new = 0

    for feed_url in feeds:
        log(f"Processing feed: {feed_url}")
        items = parse_feed(feed_url)

        seen = state.get(feed_url, [])
        new_items = [i for i in items if i["link"] not in seen]

        if not new_items:
            log("No new articles (silent mode)")
            continue

        total_new += len(new_items)

