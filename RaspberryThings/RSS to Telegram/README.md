RSS to Telegram

Tired of opening a web browser, or even worse, an application, to read your feeds ?? 
Fear not, peasant.

A few small python scripts will help us to retrive the URLs, and send via Telegram, making use of a bot a a chat group.


-Prerequisites
.Python3
.Python modules: python3-feedparser, python3-requests, python3-bs4

Folder structure
Main
|
|--rss-bot.py
|--feeds.json
|--state.json
|--logs
    |
    |--bot.log
    |--cron.log
|
|--utils
    |
    |--helpers.py
    |--parser.py
    |--telegram.py
    |--summarizer.py


Rss-bot. 
Main script that holds the telegram configuration and the logic for retrieving the data from the URL listed in feeds.json

Helpers.py
Holds the loggin function

Parser.py
Parse the data, fetch the image, ..

Summarizer.py
Extract a little summary from the feed

Telegram.py
Build two URL to send, the main text ( with the summary ) and the picture ( if any )

State.json
The simple solution to kep track of the feeds sent, just one line per url parsed.

feeds.json
list of URL to consult

