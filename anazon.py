import requests as req
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
	header = {'user-agent':'Mozilla/5.0'}
	res = req.get(url,headers=header)
	res.raise_for_status()
	res.encoding = res.apparent_encoding
	print(res.text[:1000])
except Exception as e:
	print("爬取失败")