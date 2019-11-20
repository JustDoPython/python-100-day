from bs4 import BeautifulSoup

html_doc = """
<html><head><title>index</title></head>
<body>
<p class="title"><b>首页</b></p>
<p class="main">我常用的网站
<a href="https://www.google.com" class="website" id="google">Google</a>
<a href="https://www.baidu.com" class="website" id="baidu">Baidu</a>
<a href="https://cn.bing.com" class="website" id="bing">Bing</a>
</p>
<div><!--这是注释内容--></div>
<p class="content1">...</p>
<p class="content2">...</p>
</body>
"""

# demo 1
soup = BeautifulSoup(html_doc, "lxml")
tags = soup.find_all('b')
print(tags)


# demo 2
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)


# demo 3
for tag in soup.find_all(['a', 'b']):
    print(tag)


# demo 4
for tag in soup.find_all(True):
    print(tag.name, end=', ')


# demo 5
def has_id_class(tag):
    return tag.has_attr('id') and tag.has_attr('class')

tags = soup.find_all(has_id_class)
for tag in tags:
	print(tag)


# demo 6
tags = soup.find_all(id='google')
print(tags[0]['href'])

for tag in soup.find_all(id=True):
	print(tag['href'])


# demo 7
tags = soup.find_all("a", class_="website")
for tag in tags:
	print(tag['href'])

def has_seven_characters(css_class):
    return css_class is not None and len(css_class) == 7

for tag in soup.find_all(class_=has_seven_characters):
	print(tag['id'])


# demo 8
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
tags = css_soup.find_all("p", class_="strikeout")
print(tags)


# demo 9
tags = soup.find_all(text="Google")
print("google : ", tags)

tags = soup.find_all(text=["Baidu", "Bing"])
print("baidu & bing : ", tags)

tags = soup.find_all('a', text="Google")
print("a[text=google] : ", tags)


# demo 10
tag = soup.find_all("a", limit=1)
print(tag)

tags = soup.find_all("p", recursive=False)
print(tags)


# demo 11
tags = soup.select("body a")
for tag in tags:
	print(tag['href'])


# demo 12
tags = soup.select("p > a")
print(tags)

tags = soup.select("p > #google")
print(tags)


# demo 13
tags = soup.select(".website")
for tag in tags:
	print(tag.string)


# demo 14
tags = soup.select("#google")
print(tags)


# demo 15
tags = soup.select('a[href="https://cn.bing.com"]')
print(tags)