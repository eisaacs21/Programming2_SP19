import bs4

import requests


url = "http://quotes.toscrape.com/"

page = requests.get(url)
print(page)
print(page.text)
import bs4

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())
title = soup.findAll("title")
print("title")

inspirational = soup.findAll(content="be-yourself.inspirational")