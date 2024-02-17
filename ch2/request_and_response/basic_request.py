import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get("https://ithelp.ithome.com.tw/", headers=headers)

print("回應狀態", end="\n")
print(response.status_code, end="\n")

print("回應標頭", end="\n")
print(response.headers["content-type"], end="\n")

print("回應的內容，是 bytes 類型", end="\n")
print(response.content[:200], end="\n")

print("回應的內容，是 unicode 字元，以 response.encoding 解碼", end="\n")
print(response.text[:200], end="\n")
