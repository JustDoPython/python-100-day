# 定义一个字典，并将一定的值赋给变量

MyDog = {'size':'big','color':'white','character':'gentle'}

# 字典值通过‘键’来访问
print(MyDog['size'])

print('My Dog has '+MyDog['color']+' fur.' + ' and it has a ' + MyDog['character']+' character')
# 字典数据类型
MyCon = {12:'big',0:'white',354:'gentle',1:'good'}

# list 和 dictionary　区别
list1 = ['zhangsan',23,'BeiJing']
list2 = ['BeiJing','zhangsan',23]
# list元素内容对比
list1 == list2
#False

dic1 = {'name':'zhangsan','age':23,'address':'BeiJing'}
dic2 = { 'age':23,'name':'zhangsan','address':'BeiJing'}
# 比较字典值内容是否相同
dic1 == dic2
# True

# 字典键重复的后面的键值覆盖前面的键值
dic1 = {'name':'zhangsan','age':23,'address':'BeiJing','name':'lisi'}
print(dic1)

print(dic1['name'])

dic2 = { 'age':23,'name':'zhangsan','address':'BeiJing'}
# 定义字典类型

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258',('a','b'):(12,43)}
dict = {'Name': 'Fiona', 'Age': 10, 'Class': 'Three'}
# 更新
dict['Age'] = 8
# 添加
dict['School'] = "Middle School"

print(dict)



