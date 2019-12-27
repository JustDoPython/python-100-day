# 以 r 模式打开本地建立的空文件 python-100.txt，向文件中写入内容并读取

f = open('python-100.txt', 'w', encoding='utf-8')

f.write('Python-100\n')
f.write('坚持100天')

f.close()

f = open('python-100.txt', 'r', encoding='utf-8')

print(f.read())

f.close()

# 输出结果
# Python-100
# 坚持100天