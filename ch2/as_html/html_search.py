from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>爬蟲在手、資料我有</title>
</head>

<body>
    <p class="title"><b>爬蟲在手、資料我有</b></p>
    <p class="chapter">基礎知識
        <a href="http://example.com/environment" class="page" id="link1">準備環境</a>、
        <a href="http://example.com/csv" class="page" id="link2">CSV</a>、
        <a href="http://example.com/json" class="page" id="link3">JSON</a>
    </p>
    <p class="chapter">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, "lxml")

print('搜尋標籤"b":')
print(soup.find_all("b"))

# 搜尋以"b"開頭的標籤
import re

for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

print('搜尋標籤 "a" 和 "b":')
print(soup.find_all(["a", "b"]))


def has_class_but_no_id(tag):
    """判斷標籤是否定義 class 屬性且無定義 id 屬性"""
    return tag.has_attr("class") and not tag.has_attr("id")


print(soup.find_all(has_class_but_no_id))

print("找 html 標籤下的所有標籤:")
print(soup.html.find_all("title"))

print(
    """只找 html 的「下一層」標籤
因為一般 html 下一層只有 head 和 body
所以找不到結果"""
)
print(soup.html.find_all("title", recursive=False))
