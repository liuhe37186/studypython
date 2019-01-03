import requests as req
url = "http://www.baidu.com/s"
try:
	kv = {'wd':'Python'}
	res = req.get(url,params=kv)
	res.raise_for_status()
	res.encoding = res.apparent_encoding
	print(res.request.url)
	print(len(res.text))
	print(res.text[:5000])
except Exception as e:
	print(e.text)
	print("爬取失败")