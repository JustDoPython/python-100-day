
# 求两个集合的差集，元素在 x 中不在 y 中
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print('两个集合的差集是：%s' % z)