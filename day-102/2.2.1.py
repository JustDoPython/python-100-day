# 以 r 模式打开本地建立的 python-100.txt 文件，以 'utf-8' 编码读取文件中的所有内容

with open('python-100.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
	
# 输出结果
# Python-100
# 坚持100天