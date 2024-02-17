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

title_tags_1 = soup.select(
    "html > body > div.container.index-top > div > div > div.leftside > div.board.tabs-content > div.qa-list > div.qa-list__content > h3.qa-list__title > a.qa-list__title-link"
)
titles_1 = [tag.text for tag in title_tags_1]

title_tags_2 = soup.select(
    "div.qa-list > div.qa-list__content > h3.qa-list__title > a.qa-list__title-link"
)
titles_2 = [tag.text for tag in title_tags_2]

title_tags_3 = soup.select("a.qa-list__title-link")
titles_3 = [tag.text for tag in title_tags_3]

print(titles_1 == titles_2 == titles_3)
