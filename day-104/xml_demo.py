from xml.dom.minidom import parse
import xml.sax
import xml.etree.ElementTree as ET

# 1. DOM 方式
# 读取文件
# dom = parse('test.xml')
# 获取文档元素对象
# data = dom.documentElement
# 获取 student
# stus = data.getElementsByTagName('student')
# for stu in stus:
#     # 获取标签属性值
#     st_id = stu.getAttribute('id')
#     st_name = stu.getAttribute('name')
#     # 获取标签中内容
#     id = stu.getElementsByTagName('id')[0].childNodes[0].nodeValue
#     name = stu.getElementsByTagName('name')[0].childNodes[0].nodeValue
#     age = stu.getElementsByTagName('age')[0].childNodes[0].nodeValue
#     gender = stu.getElementsByTagName('gender')[0].childNodes[0].nodeValue
#     print('st_id:', st_id,  ', st_name:',st_name)
#     print('id:', id, ', name:', name, ', age:', age, ', gender:',gender)

# 2. SAX 方式
# class StudentHandler(xml.sax.ContentHandler):
#     def __init__(self):
#         self.id = ""
#         self.name = ""
#         self.age = ""
#         self.gender = ""

    # 元素开始调用
    # def startElement(self, tag, attributes):
    #     self.CurrentData = tag
    #     if tag == "student":
    #         stu_name = attributes["name"]
    #         print("stu_name:", stu_name)

    # 元素结束调用
    # def endElement(self, tag):
    #     if self.CurrentData == "id":
    #         print("id:", self.id)
    #     elif self.CurrentData == "name":
    #         print("name:", self.name)
    #     elif self.CurrentData == "age":
    #         print("age:", self.age)
    #     elif self.CurrentData == "gender":
    #         print("gender:", self.gender)
    #     self.CurrentData = ""

    # 读取字符时调用
    # def characters(self, content):
    #     if self.CurrentData == "id":
    #         self.id = content
    #     elif self.CurrentData == "name":
    #         self.name = content
    #     elif self.CurrentData == "age":
    #         self.age = content
    #     elif self.CurrentData == "gender":
    #         self.gender = content

# if (__name__ == "__main__"):
    # 创建 XMLReader
    # parser = xml.sax.make_parser()
    # 关闭命名空间
    # parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写 ContextHandler
    # Handler = StudentHandler()
    # parser.setContentHandler(Handler)
    # parser.parse("test.xml")

# 3. ElementTree 方式
tree = ET.parse("test.xml")
# 根节点
root = tree.getroot()
# 标签名
print('root_tag:',root.tag)
for stu in root:
    # 属性值
    print ("stu_name:", stu.attrib["name"])
    # 标签中内容
    print ("id:", stu[0].text)
    print ("name:", stu[1].text)
    print("age:", stu[2].text)
    print("gender:", stu[3].text)