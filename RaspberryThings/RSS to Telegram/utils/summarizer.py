from bs4 import BeautifulSoup

def summarize(text, max_chars=300):
    soup = BeautifulSoup(text, "html.parser")
    clean = soup.get_text().strip()

    clean = " ".join(clean.split())

    if len(clean) <= max_chars:
        return clean

    short = clean[:max_chars]
    short = short.rsplit(" ", 1)[0]

    return short + "..."

