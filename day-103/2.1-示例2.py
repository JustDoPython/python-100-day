# 当然也可以用 read()、readline() 等来读取 StringIO 中写入的字符串

from io import StringIO

str = 'Python-100' + '\n' + '坚持100天'

f = StringIO(str)

currentStr = f.read()
print('写入内存中的字符串为:\n%s' %currentStr)

f.close()