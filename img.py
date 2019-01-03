import requests as req
import os

def getNetImg(url,root):
	path = root+url.split("/")[-1]
	try:

		if not os.path.exists(root):
			os.mkdir(root)
		if not os.path.exists(path):
			res = req.get(url)
			res.raise_for_status()
			with open(path,"wb") as f:
				f.write(res.content)
				f.close()
				print("文件保存成功")
		else:
			print("文件已存在")
	except Exception as e:
		print(e.text)
		print("爬取失败")