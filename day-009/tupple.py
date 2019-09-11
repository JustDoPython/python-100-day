tup1 = ('baidu', 'google', 12, 34);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
tup4 = ()
print(tup1)
print(tup2)
print(tup3)

print(type(tup3))


# 访问元组中元素
tup1 = ('baidu', 'google',1,2)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组
tup1 = ('baidu', 'google',1,2)
tup2 = (1, 2, 3, 4, 5, 6, 7)
tup1 + tup2

# 删除元组
tup1 = ('baidu', 'google',1,2)
print(tup1)
del tup1
print("删除后的元组 tup1 : ")
print(tup1)


#元组求长度
tup1 = ('baidu', 'google',1,2)
len(tup1)

# 元组连接
tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = (7,8,9)
tup1 + tup2 + tup3

# 复制元组
tup1 = ('abc')
tup1 * 3

# 指定元素访问
content = ('hello','world','!')
print(content)
print(content[1:])
print(content[:2])

print(content[-1])

print(content[-2])

# 元组内置函数

tup1 = (21,3,44,56,3,10)
# 求个数
print(len(tup1))

# 求最大值
print(max(tup1))

#　求最小值
print(min(tup1))

# 元组转换
# 元组转为list
list(tup1)
# list转为元组
tuple(tup1)
