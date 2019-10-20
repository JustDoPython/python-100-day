from pathlib import Path
txtPath = Path('python-100.txt')
nowPath = txtPath.resolve()
print("文件的完整路径为:%s" % nowPath)
print("文件完整名称为(文件名+后缀名):%s" % nowPath.name)
print("文件名为:%s" % nowPath.stem)
print("文件后缀名为:%s" % nowPath.suffix)
print("文件所在的文件夹名为:%s" % nowPath.parent)
print("文件所在的盘符为:%s" % nowPath.anchor)