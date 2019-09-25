# 1 str.format() 示例

# 1)
print('{}网址： "{}!"'.format('Python技术', 'www.justdopython.com'))

# 2)
print('{0} 和 {1}'.format('Hello', 'Python'))
print('{0} {1}'.format('Hello', 'Python'))
print('{1} {0}'.format('Hello', 'Python'))

# 3)
print('{name}网址： {site}'.format(name='Python技术', site='www.justdopython.com'))

# 4)
print('电商网站 {0}, {1}, {other}。'.format('淘宝', '京东', other='拼多多'))

# 5)
"repr() shows quotes: {!a}; str() doesn't: {!s}".format('test1', 'test2')

# 6)
import math
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

# 7)
table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789}
for name, phone in table.items():print('{0:10} ==> {1:10d}'.format(name, phone))

# 8)
table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789789789789}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789789789789}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# 2
str = input("请输入：");
print ("输入的内容是: ", str)

# 3
# read()
f = open('tmp.txt', 'r')
str = f.read(5)
print(str)
f.close()

# readline()
f = open('tmp.txt', 'r')
str = f.readline()
print(str)
f.close()

# readlines()
f = open('tmp.txt', 'r')
str = f.readlines(1)
print(str)
f.close()

# write()
f = open('tmp.txt', 'w')
num = f.write('Hello Python')
print(num)
f.close()

# seek()
f = open('tmp.txt', 'rb+')
f.write(b'0123456789abcdef')
# 移动到文件的第 6 个字节
f.seek(5)
print(f.read())

# tell()
f = open('tmp.txt', 'r')
f.seek(5)
print(f.tell())

# close()
with open('tmp.txt', 'r') as f:
     read_data = f.read()
print(f.closed)

# with 使用
with open('tmp.txt', 'r') as f:
    read_data = f.read()
print(f.closed)

# json 操作
import json
data = {'id':'1', 'name':'jhon', 'age':12}
with open('t.json', 'w') as f:
   json.dump(data, f)
with open("t.json", 'r') as f:
   d = json.load( f)
print(d)

