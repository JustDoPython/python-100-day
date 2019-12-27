# 以 w 模式打开本地建立的空文件 python-100.txt，获取文件中读取指针的位置

f = open('python-100.txt', 'w', encoding='utf-8')

print('打开空文件时，指针位置为:', f.tell())
f.write('Python-100\n' + '坚持100天')  # 'utf-8'编码格式下，换行符占 2 个字节，汉字占 3 个字节
print('写入内容后，指针位置为:', f.tell())

f.close()

# 输出结果：
# 打开空文件时，指针位置为: 0
# 写入内容后，指针位置为: 24

# 以 r 模式打开文件 python-100.txt，移动文件中读取指针的位置

f = open('python-100.txt', 'rb')

print("1.文件内容为:")
print(f.read().decode('utf-8'))

f.seek(6)
print('\n2.偏移量为 12 个字节时，输出内容为:')
print(f.read().decode('utf-8'))

f.seek(-12, 2)
print('\n3.偏移量为 -12 个字节时，输出内容为:')
print(f.read().decode('utf-8'))

print('\n4.在当前指针位置偏移:')
f.seek(12)
print('文件指针当前位置为：', f.tell())
f.seek(-6, 1)
print('文件指针当前位置为：', f.tell())
f.seek(6, 1)
print('文件指针当前位置为：', f.tell())
print(f.read().decode('utf-8'))

f.close()

# 输出结果:
# 1.文件内容为:
# Python-100
# 坚持100天
#
# 2.偏移量为 12 个字节时，输出内容为:
# -100
# 坚持100天
#
# 3.偏移量为 -12 个字节时，输出内容为:
# 坚持100天
# 
# 4.在当前指针位置偏移:
# 文件指针当前位置为： 12
# 文件指针当前位置为： 6
# 文件指针当前位置为： 12
# 坚持100天