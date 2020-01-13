# 1.以 r 模式打开本地建立的 python-100.txt 文件，每次读取 n 个字符

with open('python-100.txt', 'r', encoding='utf-8') as f:
    content = f.read(8)
    print(content)

    content = f.read(8)
    print(content)

# 输出结果(注意：每次读取到的换行符 '\n' 也是算一个字符的，换行符位于每行内容的末尾)
# Python-1
# 00
# 坚持100

# 2.以 rb 模式打开本地建立的 python-100.txt 文件，每次读取 n 个字节，注意是字节

with open('python-100.txt', 'rb') as f:
    content = f.read(8)
    print(content)

    content = f.read(8)
    print(content)

# 输出结果
# b'Python-1'
# b'00\r\n\xe5\x9d\x9a\xe6'