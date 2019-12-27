# 以 r 模式打开本地建立的 python-100.txt 文件，读取文件中所有内容，以列表形式返回

with open('python-100.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(content)

    for line in content:
        print(line.strip('\n'))

# 输出结果
# ['Python-100\n', '坚持100天']
# Python-100
# 坚持100天