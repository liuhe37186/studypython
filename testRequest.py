from htmlrequest import getHtml
from img import getNetImg

url = "https://item.jd.com/2967929.html"
url1 = "http://www.baidu.com/s"
url2 = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
kv = {'wd':'Python'}
headers = {'user-agent':'Mozilla/5.0'}

url3 = "http://04.imgmini.eastday.com/mobile/20180816/20180816093312_90ca9484e168384f9c06f06b28e8738d_1.jpeg"
img_url = "https://edu-image.nosdn.127.net/5B8826377EE623C7B6328E8F8B8D2871.png";
root="/Users/liuhe/Documents/img/"
bsUrl = "http://python123.io/ws/demo.html"

html = getHtml(bsUrl)

print(html)

# html = getHtml(url2,headers=headers,params=kv)
# print(html[:1000])
# getNetImg(img_url,root)

