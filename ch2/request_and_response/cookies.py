import requests

url = "https://httpbin.org/cookies"
cookies = {
    "ithome": "scrapy",
}

response = requests.get(url, cookies=cookies)
print(response.text)
