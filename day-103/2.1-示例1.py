# 定义一个 StringIO 对象，写入并读取其在内存中的内容
from io import StringIO

f = StringIO()

f.write('Python-100')
str = f.getvalue()
print('写入内存中的字符串为:%s' %str)

f.write('\n') # 追加写入内容
f.write('坚持100天')
str = f.getvalue()  # getvalue() 可以读取到 StringIO 中的所有内容
print('写入内存中的字符串为:\n%s' %str)

f.close() # 释放内存中的数据，后续不可再对该 StringIO 进行内容的读写操作

# 输出结果
# 写入内存中的字符串为:
# Python-100
# 写入内存中的字符串为:
# Python-100
# 坚持100天