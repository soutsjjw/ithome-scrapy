import datetime
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

responses = leftside.find_all("div", class_="response")
print(f"留言數： {len(responses)}")

response_authors = []
response_times = []
response_contents = []

for response in responses:
    panel = response.find("div", class_="qa-panel__content")
    header = panel.find("div", class_="response-header__info")
    response_authors.append(
        header.find("a", class_="response-header__person").get_text(strip=True)
    )

    time_str = header.find("a", class_="ans-header__time").get_text(strip=True)
    response_times.append(datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S"))

    response_contents.append(
        panel.find("div", class_="markdown__style").get_text(strip=True)
    )

for index in range(len(response_authors)):
    print(f"回文作者： {response_authors[index]}")
    print(f"回文時間： {response_times[index]}")
    print(f"回文內容： {response_contents[index]}")
