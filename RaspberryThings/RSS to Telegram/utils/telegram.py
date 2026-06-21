import requests

def send_message(token, chat_id, text, parse_mode="HTML"):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": False
    }
    return requests.get(url, params=params)

def send_photo(token, chat_id, photo_url, caption, parse_mode="HTML"):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    data = {
        "chat_id": chat_id,
        "caption": caption,
        "parse_mode": parse_mode
    }
    try:
        photo = requests.get(photo_url, timeout=5).content
        files = {"photo": photo}
        return requests.post(url, data=data, files=files)
    except:
        return send_message(token, chat_id, caption)
