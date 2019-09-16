
# 在原始集合 x 中移除与 y 集合中的重复元素，并将不重复的元素插入到集合 x 中：
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

x.symmetric_difference_update(y)

print(x)