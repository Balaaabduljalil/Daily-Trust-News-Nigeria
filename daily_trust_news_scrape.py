#daily trust news Nigeria scrapping.
import requests
from bs4 import BeautifulSoup
response = requests.get('https://dailytrust.com')
soup = BeautifulSoup(response.text, 'lxml')
title = soup.find('title')
print(response.status_code)
print(response.text)
print(title.get_text())
headlines = soup.find_all(itemprop = 'text')
for headline in headlines:
    print(headline.get_text())