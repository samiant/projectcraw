import requests
from bs4 import BeautifulSoup

url = 'https://scholar.google.com/citations?user=p4-7UvwAAAAJ&hl=en&oi=ao'

# membuat request
text = requests.get(detail_path).text
r = requests.get(url)
# hasil response
requests = r.content

soup = BeautifulSoup(requests, 'html.parser')
# extract elemen
title = soup.findAll('a', attrs={'class': 'gsc_a_t'})
sitasi = soup.findAll('a', attrs={'class': 'gsc_a_c'})
tahun = soup.findAll('a', attrs={'class': 'gsc_a_y'})

count = 0
for x in range(0, len(title)):
    count += 1
    print("{0}. {1}\n -{2}"
          .format(count, title[x].text.strip(), sitasi[x].text.strip(), sitasi[x].text.strip()))
