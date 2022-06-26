import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://www.lovereading.co.uk/genres/lrtop/lovereadings-10-most-popular-books-of-the-week")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("h2 a")
titles_texts = [title_tag.getText() for title_tag in titles]

formats = soup.find_all(name="p", class_="author")
details = [tag.getText() for tag in formats]
author_texts = [item.split(" \n")[0].split(": ")[1] for item in details]
formats_texts = [item.split("Format: ")[1].split(" ")[0] for item in details]
date_texts = [item.split("Date: ")[1] for item in details]

df = pd.DataFrame(list(zip(titles_texts, author_texts, formats_texts, date_texts)),
                  columns=['Title', 'Authors', 'Format', 'Date'])
df.to_csv("books.csv", encoding="utf-8-sig")
