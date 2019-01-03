# Beautiful Soup库的使用
from htmlrequest import getHtml
from bs4 import BeautifulSoup
import bs4
bsUrl = "http://python123.io/ws/demo.html"
html = getHtml(bsUrl)
soup = BeautifulSoup(html,"html.parser")
# print(soup.prettify())

# print(soup.title.parent)
# print(soup.a)
# tag_a = soup.a
# print(tag_a.attrs)

# attrs_href = tag_a.attrs["href"]
# print(attrs_href)
for parent in soup.a.parents:
	if parent is None:
		print('parent:',parent)
	else:
		print('name',parent.name)

for sibling in soup.find('body').children:
	if isinstance(sibling,bs4.element.Tag):
		for s in soup.a.next_sibling:
			print(s)

