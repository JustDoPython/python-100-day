# 打开 'python-100.txt' 文件，如果文件不存在会在程序文件 *.py 所在的目录下创建该文件。

file = open('python-100.txt', 'w')
print('测试1：python-100.txt 文件已打开。')

# 关闭已打开的 'python-100.txt' 文件

file.close()
print('测试1：python-100.txt 文件已关闭。')

# 打开 'C:\Users\Desktop\py' 路径下的 'python-100.txt' 文件。

file = open('C:\\\\Users\\\\Desktop\\\\py\\\\python-100.txt', 'w')
print('测试2：python-100.txt 文件已打开。')

# 关闭已打开的 'python-100.txt' 文件

file.close()
print('测试2：python-100.txt 文件已关闭。')