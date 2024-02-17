from lxml import etree

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

# 載入 HTML 原始資料
html = etree.HTML(html_doc)

print("取得 html 標籤", end="\n")
print(html.xpath("/html"), end="\n")

print("取得 body 下所有 a 標籤", end="\n")
print(html.xpath("/html/body/a"), end="\n")

print("取得所有 a 標籤", end="\n")
print(html.xpath("//a"), end="\n")

print("取得 body 下所有 a 標籤", end="\n")
print(html.xpath("/html/body//a"), end="\n")

print("取得所有 a 標籤的 href 屬性", end="\n")
print(html.xpath("//a/@href"), end="\n")

print("取得 body 下第一個 a 標籤", end="\n")
print(html.xpath("/html/body//a[1]"))

print("取得 body 下最後一個 a 標籤", end="\n")
print(html.xpath("/html/body//a[last() - 1]"))

print("取得 body 下前兩個 a 標籤", end="\n")
print(html.xpath("/html/body//a[position() < 3]"))

print("取得有定義 class 屬性的 p 標籤", end="\n")
print(html.xpath("//p[@class]"))

print("取得 class 屬性值為 title 的 p 標籤", end="\n")
print(html.xpath("//p[@class='title']"))

print("取得 body 標籤的全部子元素", end="\n")
print(html.xpath("/html/body/*"))

print("取得 body 下全部元素", end="\n")
print(html.xpath("/html/body//*"))

print("取得至少有定義一個屬性的 p 標籤", end="\n")
print(html.xpath("//p[@*]"))

print("一次取得全部 p 標籤和 a 標籤", end="\n")
print(html.xpath("//p|//a"))
