from bs4 import BeautifulSoup

# demo 1
# soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup("<html><head><title>index</title></head><body>content</body></html>", "lxml")
print(soup.head)


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

# demo 2
soup = BeautifulSoup(html_doc, "lxml");
p_tag = soup.p
print(p_tag.name)
print(p_tag["class"])
print(p_tag.attrs)

p_tag.name="myTag" # attrs 同样可被修改，操作同字典
print(p_tag)


# demo 3
soup = BeautifulSoup(html_doc, "lxml");
print(soup.p.b)


# demo 4
soup = BeautifulSoup(html_doc, "lxml");
a_tags=soup.find_all("a")
print(a_tags)


# demo 5
soup = BeautifulSoup(html_doc, "lxml");
head_tag=soup.head
print(head_tag)
print(head_tag.contents)

for child in head_tag.children:
	print("child is : ", child)


# demo 6
soup = BeautifulSoup(html_doc, "lxml");
head_tag=soup.head
for child in head_tag.descendants:
	print("child is : ", child)


# demo 7
soup = BeautifulSoup(html_doc, "lxml");
title_tag=soup.title

print(title_tag.parent)
print(type(soup.html.parent))
print(soup.parent)


# demo 8
soup = BeautifulSoup(html_doc, "lxml");
a_tag=soup.a

for parent in a_tag.parents:
    print(parent.name)


# demo 9
soup = BeautifulSoup(html_doc, "lxml");
div_tag=soup.div

print(div_tag.next_sibling)
print(div_tag.next_sibling.next_sibling)


# demo 10
soup = BeautifulSoup(html_doc, "lxml");
div_tag=soup.div

for pre_tag in div_tag.previous_siblings:
	print("pre_tag is : ", pre_tag)


# demo 11
soup = BeautifulSoup(html_doc, "lxml");

head_tag=soup.head
print(head_tag.next_element)

title_tag=soup.p
print(title_tag.next_element)


# demo 12
soup = BeautifulSoup(html_doc, "lxml");
div_tag=soup.div
for next_element in div_tag.next_elements:
	print("next_element is : ", next_element)
