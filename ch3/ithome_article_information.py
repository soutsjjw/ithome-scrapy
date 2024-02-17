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

leftside = soup.find("div", class_="leftside")
original_post = leftside.find("div", class_="qa-panel")

print("內文", end="\n")
print(original_post.text.strip()[:50], end="\n")

article_header = original_post.find("div", class_="qa-header")
article_info = article_header.find("div", class_="ir-article-info__content")
article_author = article_info.find("a", class_="ir-article-info__name")

print("作者", end="\n")
print(article_author.get_text().strip(), end="\n")

from datetime import datetime

published_time_str = article_info.find("a", class_="ir-article-info__time").get_text(
    strip=True
)
published_time = datetime.strptime(published_time_str, "%Y-%m-%d %H:%M:%S")

print("發文時間", end="\n")
print(published_time, end="\n")

tag_group = article_header.find("div", class_="qa-header__tagGroup")
tags_element = tag_group.find_all("a", class_="tag")

tags = [tag_element.get_text(strip=True) for tag_element in tags_element]

print("文章標籤", end="\n")
print(tags, end="\n")

view_count_str = article_info.find("div", class_="ir-article-info__view").get_text(
    strip=True
)
# view_count = int(view_count_str.replace("瀏覽", "").strip())

# 用正則式將數字抓出來
import re

view_count = int(re.search(r"(\d+).*", view_count_str).group(1))

print("瀏覽數", end="\n")
print(view_count, end="\n")
