
# 返回两个或者多个集合的交集
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.intersection(y)

print(z)

#　返回三个集合的交集
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)
print('三个集合的差集是：%s' % result)