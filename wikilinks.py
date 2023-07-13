import requests
from bs4 import BeautifulSoup
import json


wikipedia_url = "https://en.wikipedia.org/wiki/Special:Random"

num_links = 100
links = []

for _ in range(num_links):
    response = requests.get(wikipedia_url)
    soup = BeautifulSoup(response.text, "html.parser")
    article_link = soup.find("link", {"rel": "canonical"})["href"]
    links.append(article_link)

with open("wikipedia_links.json", "w") as file:
    json.dump(links, file)