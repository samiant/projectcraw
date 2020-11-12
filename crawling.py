import requests
from bs4 import BeautifulSoup

url = "https://scholar.google.com/citations?user=p4-7UvwAAAAJ&hl=en&oi=ao"
page  = requests.get(url).text
soup_expatistan = BeautifulSoup(page)

expatistan_table = soup_expatistan.find("table", class_="comparison")
expatistan_titles = expatistan_table.find_all("tr", class_="expandable")

for expatistan_title in expatistan_titles:
    published_date = expatistan_title.find("th", class_="percent")
    print(published_date.span.string)