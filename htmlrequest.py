import requests as req

# def getHtml(url):
# 	try:
# 		res = req.get(url)
# 		res.raise_for_status()
# 		res.encoding = res.apparent_encoding
# 		return res.text
# 	except Exception as e:
# 		print(e.text)
# 		return "爬取失败"
# def getHtml(url,kv):
# 	try:
# 		res = req.get(url,params=kv)
# 		res.raise_for_status()
# 		res.encoding = res.apparent_encoding
# 		return res.text
# 	except Exception as e:
# 		print(e.text)
# 		return "爬取失败"
# def getHtml(url,headers):
# 	try:
# 		res = req.get(url,headers=headers)
# 		res.raise_for_status()
# 		res.encoding = res.apparent_encoding
# 		return res.text
# 	except Exception as e:
# 		print(e.text)
# 		return "爬取失败"
def getHtml(url,**kwargs):
	try:
		res = req.get(url,**kwargs)
		res.raise_for_status()
		res.encoding = res.apparent_encoding
		return res.text
	except Exception as e:
		print(e.text)
		return "爬取失败"
	pass