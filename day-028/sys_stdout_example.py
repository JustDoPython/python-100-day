import sys


# 以附加模式打开文件，若不存在则新建
with open("count_log.txt", 'a', encoding='utf-8') as f:
    sys.stdout = f
    for i in range(10):
        print("count = ", i)