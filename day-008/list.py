# 使用list函数
ll = list('hello list')
print(ll)

# 列表元素赋值 如 x[3]=5
x = [1,2,3,4,5]
# 改变列表第四个元素的值
x[3] = 5
print(x)

# 删除元素 del
names = ['zhangsan','lisi','wangwu','zhaoliu']
print(names)
# 删除第三个元素
del names[2]
# 最后列表长度变为3
print(names)


# 分片赋值
name = list('python')
name[2:] = 'wr'
print(name)

# 序列不等长分片替换
name_re = list('perl')
# 替换第一个元素后的所有内容
name_re[1:] = list('ython')
print(name_re)

# 插入新元素
num = [1,4,5]
# 在第一个元素后插入新的元素
num[1:1] = [2,3]
num
print(num)

# 给第一个和迪桑元素之间分片赋值一个空序列，即删除元素
num[1:3] = []
num
[1, 4, 5]

# 负数分片操作
num[-1:-1] = [5,5,5]
print(num)


# 列表方法 追加内容
list_append = [1,2,3,4]
list_append.append(5)
print(list_append)

# 统计列表中某个内容的词频
num.count(5)


# 统计字母a出现的次数
name = ['a','a','abf','ark','nhk']

name.count('a')


# extend 方法
a =[1,2,3]
b = [4,5,6]
# 将列表b追加在列表a后面
a.extend(b)
print(a)


# index 方法
content = ['where','who','lisi','cntent','who']
content.index('who')

# insert 方法
num = [1,2,5,6,7]
num.insert(2,3)
print(num)
num.insert(3,4)
print(num)


# pop 方法
x = [1,2,3]
x.pop()
3
print(x)
x.pop()
print(x)

# remove 方法
content = ['where', 'who', 'lisi', 'cntent', 'who', 'who']
# 移除了第一个匹配的元素
content.remove('who')
print(content)


# reverse 方法
x = [1, 2, 3]
# 元素反向存储
x.reverse()
print(x)

# sort 方法
x = [2,3,5,6,1,4,7]
x.sort()
print(x)

#  clear 方法
list1 = ['baidu', 'google', 12, 23]
print(list1)
list1.clear()
print(list1)

#  copy 方法
list1 = ['baidu', 'google', 12, 23];
list2 = list1.copy()
print(list2)
