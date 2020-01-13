# 考虑一个场景，比如你需要对爬虫爬取到的数据进行操作，但是你不想把数据写入本地的硬盘上，这时候 StringIO 就派上用场了。

from io import StringIO

# 假设的爬虫数据输出函数 outputData()
def outputData():
    dataOne   = '我是 1 号爬虫数据\n'
    dataTwo   = '我是 2 号爬虫数据\n'
    dataThree = '我是 3 号爬虫数据'
    data = dataOne + dataTwo + dataThree
    return data

# dataStr 为爬虫数据字符串
dataStr = outputData()

# 1. 将 outputData() 函数返回的内容写入内存中
dataIO = StringIO(dataStr)

# 1.1 输出 StringIO 在内存中写入的数据
print('1.1内存中写入的数据为:\n%s' %dataIO.getvalue())

# 输出结果:
# 1.1内存中写入的数据为:
# 我是 1 号爬虫数据
# 我是 2 号爬虫数据
# 我是 3 号爬虫数据

# 1.2 按行输出写入的数据方式一
print('1.2按行输出写入的数据方式一:')
for data in dataIO.readlines():
    print(data.strip('\n')) # 去掉每行数据末尾的换行符

# 输出结果:
# 1.2按行输出写入的数据方式一:
# 我是 1 号爬虫数据
# 我是 2 号爬虫数据
# 我是 3 号爬虫数据

# 1.3 按行输出写入的数据方式二
# 由于上一步的操作，此时文件指针指向数据末尾(32)，我们需要将指针指向起始位置
print('由于上一步操作的输出，此时文件指针位置为:%d' %dataIO.tell())

# 将文件指针指向起始位置，方便下面的演示
dataIO.seek(0)
print('1.3按行输出写入的数据方式二:')
for data in dataIO:
    print(data.strip('\n'))

# 输出结果:
# 1.3按行输出写入的数据方式二:
# 我是 1 号爬虫数据
# 我是 2 号爬虫数据
# 我是 3 号爬虫数据

# 2. 采用 write() 的方法将字符串写入内存
dataWriteIO = StringIO()
dataWriteIO.write(dataStr)

# 2.1 输出内存中写入的数据
print('2.1内存中写入的数据为:\n%s' %dataIO.getvalue())

# 输出结果:
# 2.1内存中写入的数据为:
# 我是 1 号爬虫数据
# 我是 2 号爬虫数据
# 我是 3 号爬虫数据
 
# 2.2 按行输出写入的数据方式一
# 由于 write() 写入字符串后，文件指针会指向写入内容的结尾，需要将文件指针指向起始位置，否则未能输出内容
print('2.2按行输出写入的数据方式一:')
print('输出内容为空！')
for data in dataIO:
    print(data.strip('\n'))
print('输出内容为空！')

# 输出结果：
# 2.2按行输出写入的数据方式一:
# 输出内容为空！
# 输出内容为空！


# 2.3 按行输出写入的数据方式二
# 将指针指向起始位置重新按行输出
dataIO.seek(0)
print('2.3按行输出写入的数据方式:')
for data in dataIO.readlines():
    print(data.strip('\n'))

# 输出结果
# 2.3按行输出写入的数据方式:
# 我是 1 号爬虫数据
# 我是 2 号爬虫数据
# 我是 3 号爬虫数据