# -*-coding:UTF-8-*-

list01 = [5, -1, 3, 6, -7, 8, -11, 2]
list02 = ['apple', 'pig', 'monkey', 'money']

print(sorted(list01))
# print out: [-11, -7, -1, 2, 3, 5, 6, 8]

print(sorted(list01, key=abs))
# print out: [-1, 2, 3, 5, 6, -7, 8, -11]

# 默认升序
print(sorted(list02))
# print out: ['apple', 'money', 'monkey', 'pig']

# 降序
print(sorted(list02, reverse=True))
# print out: ['pig', 'monkey', 'money', 'apple']

# 匿名函数排序
print(sorted(list02, key=lambda x: len(x), reverse=True))
# print out: ['monkey', 'apple', 'money', 'pig']




