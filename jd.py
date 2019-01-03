import requests as req
url = "https://item.jd.com/2967929.html"
try:
	res = req.get(url)
	res.raise_for_status()
	res.encoding = res.apparent_encoding
	print(res.text)
except Exception as e:
	print("爬取失败")

