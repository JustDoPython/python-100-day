# 定义一个 BytesIO 对象，写入并读取其在内存中的内容

from io import BytesIO

str = 'Python-100' + '\n' + '坚持100天'

f = BytesIO(str.encode('utf-8'))

print('写入内存的字节为:%s' %f.getvalue())

print('字节解码后内容为:\n%s' %f.getvalue().decode('utf-8'))