from pathlib import Path
currentPath = Path.cwd() / 'python'

print(currentPath.exists())  # 判断是否存在 python 文件夹，此时返回 False。
print(currentPath.is_dir())  # 判断是否存在 python 文件夹，此时返回 False。

currentPath.mkdir()  # 创建 python 文件夹。

print(currentPath.exists())  # 判断是否存在 python 文件夹，此时返回 True。
print(currentPath.is_dir())  # 判断是否存在 python 文件夹，此时返回 True。

currentPath = Path.cwd() / 'python-100.txt'

print(currentPath.exists())  # 判断是否存在 python-100.txt 文件，此时文件未创建返回 False。
print(currentPath.is_file())  # 判断是否存在 python-100.txt 文件，此时文件未创建返回 False。

f = open(currentPath,'w')  # 创建 python-100.txt 文件。
f.close()

print(currentPath.exists())  # 判断是否存在 python-100.txt 文件，此时返回 True。
print(currentPath.is_file())  # 判断是否存在 python-100.txt 文件，此时返回 True。