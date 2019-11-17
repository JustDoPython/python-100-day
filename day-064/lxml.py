from lxml import etree
from io import StringIO

test_html = '''
<html>
    <body>
        <div>
            <!-- 这里是注释 -->
            <h4>手机品牌商<span style="margin-left:10px">4</span></h4>
            <ul>
               <li>小米</li>
               <li>华为</li>
               <li class='blank'> OPPO </li>
               <li>苹果</li>
            </ul>
        </div>
        <div id="last_div">
            <h4>电脑品牌商<span style="margin-left:10px">3</span></h4>
            <ul class="ul" style="color:red">
                <li>戴尔</li>
                <li>机械革命</li>
                <li>ThinkPad</li>
            </ul>
        </div>
    </body>
</html>'''

html = etree.parse(StringIO(test_html))
print(html)

li_list = html.xpath('//li')

print("类型：")
print(type(li_list))

print("值：")
print(li_list)

print("个数：")
print(len(li_list))

for l in li_list:
    print("li文本为：" + l.text)

# 根据属性获取
blank_li_list = html.xpath('//li[@class="blank"]')

print("类型：")
print(type(blank_li_list))

print("值：")
print(blank_li_list)

print("个数：")
print(len(blank_li_list))


for l in blank_li_list:
    print("blank_li文本为：" + l.text)


ul = html.find('//ul')
for name, value in ul.attrib.items():
    print('{0}="{1}"'.format(name, value))
ul.set("new_attr", "true")
new_attr = ul.get('new_attr')
print(new_attr)


last_div = html.xpath('//div[last()]')[0]
print("TAG：")
print(last_div.tag)
print("值：")
print(last_div.text)


child = etree.Element("child")
child.text = "这里是新的子元素"
last_div.append(child)
clild_text = last_div.find("child").text
print(clild_text)

first_ul = html.find("//ul")
ul_li = first_ul.xpath("li")
for li in ul_li:
    first_ul.remove(li)

ul_li = first_ul.xpath("li")
if len(ul_li) == 0:
    print("元素被删除了")

body = html.find("body")
for sub in body.iter():
    print(sub.tag)
    print(sub.text)
