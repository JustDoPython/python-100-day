x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
#　判断集合 y 中是否包含集合 x 中的元素，如果没有返回 True, 有则返回 False
z = x.isdisjoint(y)
# 结果返回 False,说明集合 y 中有和 x 中相同的元素
print(z)



x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "baidu"}
#　判断集合 y 中是否包含集合 x 中的元素，如果没有返回 True, 有则返回 False
z = x.isdisjoint(y)
# 结果返回 True,说明集合 y 中没有和 x 中相同的元素
print(z)