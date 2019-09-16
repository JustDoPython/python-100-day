# 返回一个无返回值的集合交集
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

x.intersection_update(y)

print(x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)