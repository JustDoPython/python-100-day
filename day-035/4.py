from pathlib import Path
currentPath = Path.cwd()
mkPath = currentPath / 'python-100.txt'
with mkPath.open('w') as f:  # 创建并以 "w" 格式打开 python-100.txt 文件。
    f.write('python-100')  # 写入 python-100 字符串。
f = open(mkPath, 'r')
print("读取的文件内容为:%s" % f.read())
f.close()


from pathlib import Path
currentPath = Path.cwd()
mkPathText = currentPath / 'python-100-text.txt'
mkPathText.write_text('python-100')
print("读取的文件内容为:%s" % mkPathText.read_text())

str2byte = bytes('python-100', encoding = 'utf-8')
mkPathByte = currentPath / 'python-100-byte.txt'
mkPathByte.write_bytes(str2byte)
print("读取的文件内容为:%s" % mkPathByte.read_bytes())