# 每次读取一行内容，该方法较为实用

with open('python-100.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip('\n'))

# 输出结果
# Python-100
# 坚持100天