from bs4 import BeautifulSoup
import requests
import pprint

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get("https://ithelp.ithome.com.tw/", headers=headers)
html_content = response.text

# 使用 BeautifulSoup 解析 HTML 內容
soup = BeautifulSoup(html_content, "html.parser")

# 找到名為 "_token" 的元素
token_element = soup.find("input", {"name": "_token"})

playload = {
    "_token": token_element["value"],
    "search": "python",
    "tab": "question",
}

response = requests.get("https://ithelp.ithome.com.tw/search", params=playload)
print(response.url)

playload = {
    "name": "Rex",
    "topic": "python",
}

response = requests.post("https://httpbin.org/post", data=playload)
pprint.pprint(response.json())
