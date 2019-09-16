
# 移除两个集合中都存在的元素，无返回值,将 x 中存在的 y 中不存在的留下，将 x 和 y 中都存在的删除，y 中存在和不存在的删除
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)


x1 = {1,2,3,4}
y1 = {1,2,3}

x1.difference_update(y1)

print(x1)