import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}

html_doc = requests.get(
    "https://ithelp.ithome.com.tw/articles/10228719", headers=headers
).text
soup = BeautifulSoup(html_doc, "lxml")

# 內文元素
content = soup.find("div", class_="markdown__style")

print(content.text)
