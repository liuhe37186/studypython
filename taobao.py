import requests
import re

def getHtmlText(url):
	try:
		rusult = requests.get(url,timeout=30)
		rusult.raise_for_status()
		rusult.encoding = rusult.apparent_encoding
		return rusult.text
	except Exception as e:
		return e
	


def parserText(infoList,html):
	try:
		pList = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tList = re.findall(r'\"raw_title\"\:\".*?\"',html)
		# print(len(pList))
		for i in range(len(pList)):
			price = eval(pList[i].split(':')[1])
			title = eval(tList[i].split(':')[1])
			# print(title)
			infoList.append([price,title])
	except Exception as e:
		print("parserError",e)

def printInfo(infoList):
	tplt = '{:4}\t{:8}\t{:32}'
	print(tplt.format('序号','价格','标题'))
	# print(infoList)
	count = 0
	for g in infoList:
		count += 1
		print(tplt.format(count,g[0],g[1]))

def main():
	goods = '书包'
	page = 3
	start_url =  'https://s.taobao.com/search?q=' + goods
	infoList = []
	for i in range(page):
		try:
			url = start_url + '&s=' + str(44*i)
			html = getHtmlText(url)
			# print(html)
			parserText(infoList,html)
		except:
			continue
	printInfo(infoList)
main()

	