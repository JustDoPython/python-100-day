# -*-coding:UTF-8-*-


def boy(n):
    if n % 2 == 0:
        return True
    return False

# 自定义函数
filterList = filter(boy, list(range(20)))

print(list(filterList))
# print out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 自定义函数
filterList2 = filter(lambda n: n % 2 == 0, list(range(20)))

print(list(filterList2))
# print out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

