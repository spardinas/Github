import feedparser
from bs4 import BeautifulSoup

def extract_image(entry):
    
    media = entry.get("media_content", [])
    if media and "url" in media[0]:
        return media[0]["url"]

    enclosure = entry.get("enclosures", [])
    if enclosure and "href" in enclosure[0]:
        return enclosure[0]["href"]

    summary = entry.get("summary", "")
    soup = BeautifulSoup(summary, "html.parser")
    img = soup.find("img")
    if img and img.get("src"):
        return img.get("src")

    return None

def parse_feed(url):
    feed = feedparser.parse(url)
    items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")
        summary = entry.get("summary", "")
        published = entry.get("published", "")

        items.append({
            "title": title,
            "link": link,
            "summary": summary,
            "published": published,
            "image": extract_image(entry)
        })

    return items
