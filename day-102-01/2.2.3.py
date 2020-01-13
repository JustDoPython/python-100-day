# 以 r 模式打开本地建立的 python-100.txt 文件，每次读取文件中的一行内容，利用 strip() 函数去掉每一行末尾的换行符

with open('python-100.txt', 'r', encoding='utf-8') as f:
    firstLine = f.readline().strip('\n')
    secondLine = f.readline().strip('\n')

    print(firstLine)
    print(secondLine)

# 输出结果
# Python-100
# 坚持100天