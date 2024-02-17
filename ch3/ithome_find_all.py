import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}

html_doc = requests.get(
    "https://ithelp.ithome.com.tw/articles?tab=tech", headers=headers
).text
soup = BeautifulSoup(html_doc, "lxml")

article_tags = soup.find_all("div", class_="qa-list")

for article_tag in article_tags:
    title_tag = article_tag.find("a", class_="qa-list__title-link")
    print(title_tag.text)
