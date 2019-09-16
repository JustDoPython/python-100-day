# 合并两个集合，重复元素只会出现一次：

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.union(y)

print(z)


# 合并多个集合：

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)