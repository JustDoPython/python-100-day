# 定义一个学生序列
stuinfo = ['zhangsan', 'lisi', 'wangwu', 18, 20]
print(stuinfo)

# 定义学生姓名和学生年龄，然后再定义一个属于自己的数据库将两个列表加入
stuname = ['zhangsan','lisi','wangwu']
stuage = [18, 20, 16]
database = [stuname, stuage]
print('我的学生库信息是：%s ' % database)
print('我的学生库姓名信息是：%s ' % database[0])
print('我的学生库年龄信息是：%s ' % database[1])

# 字符串序列的索引
str = 'hello'
print("下标是0的元素是 ：%s" % str[0])
print("下标是1的元素是 ：%s" % str[1])
print("下标是-1的元素是 ：%s" % str[-1])
print("下标是-2的元素是 ：%s" % str[-2])

# 分片
# 构建一个序列tag，里面包含一个元素
tag=['https://www.cnblogs.com/yangyuqig/p/10101663.html']

# 拿到这个元素后通过分片取出一个范围的值
print("下标从0-24的元素内容是：%s " % tag[0][0:24])

num=[1,2,3,4,5,6,7,8,9,10]

# 表示从第四个到最后一个元素
print("数字从3-10的内容是：%s " % num[3:10])

# 分片快捷操作
print("前三个数字是：%s " % num[0:3])

# 按照步长为2返回第1个和第6个之间的元素
print("0-6之间步长为2的元素是：%s " % num[0:6:2])


print("负数分片结果是：%s" %  num[7:-1])

print("结果是： %s " %num[-9:-1])

# 提取前6个元素，步长为2
print("前6个元素中步长为2的结果为：%s " % num[:6:2])

# 序列相加

a = 'hello'
b = ' world !'
print("两个序列相加的结果是：%s " % a+b)

# 序列相乘
a = 'hello '
b = a * 3
print("返回序列相乘的结果是：%s " % b)

# 序列的成员资格
str = 'hello'
print('h' in str)

print('x' in str)

# 序列长度、最大值、最小值
print(len([11,34,23]))

print(max(11,34,23))

print(min(11,34,23))