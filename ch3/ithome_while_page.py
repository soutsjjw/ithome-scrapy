import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}

# 抓取 1 ~ 5頁
current_page = 1
end_page = 5

# 起始頁面網址
target_url = "https://ithelp.ithome.com.tw/articles?tab=tech"

while current_page <= end_page:
    html_doc = requests.get(target_url, headers=headers).text
    soup = BeautifulSoup(html_doc, "lxml")

    # 取得下一頁標籤
    next_page_tag = soup.select_one("a[rel=next]")

    # 如果抓不到會得到 None，跳出迴圈
    if not next_page_tag:
        break
    target_url = next_page_tag["href"]

    print(target_url)

    current_page = current_page + 1
