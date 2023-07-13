from bs4 import BeautifulSoup
import requests

url = 'https://m.dailyhunt.in/news/india/english/news18-epaper-newseigh/article+370+back+in+sc+after+3+yrs+hearing+to+begin+on+aug+2+activist+shehla+rashid+exits+case-newsid-n517313978'

response = requests.get(url)

html_content = response.text
print(html_content)
soup = BeautifulSoup(html_content, "html.parser")

text_elements = soup.find_all("p")

article_text = " ".join([element.text for element in text_elements])

print(article_text)