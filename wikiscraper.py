import requests
from bs4 import BeautifulSoup
import sys

def scrape_wiki_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    content_div = soup.find(id='mw-content-text')
    paragraphs = content_div.find_all('p')
    
    main_body = '\n'.join([p.get_text() for p in paragraphs])
    return main_body


sys.stdout.reconfigure(encoding='utf-8')
