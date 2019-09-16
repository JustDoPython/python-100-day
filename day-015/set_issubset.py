
# 判断集合 x 的所有元素是否都包含在集合 y 中：
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b","y"}

z = x.issubset(y)

print(z)