# 使用 Path.iterdir() 获取当前文件下的所有文件，并根据后缀名统计其个数。
import pathlib
from collections import Counter
currentPath = pathlib.Path.cwd()
gen = (i.suffix for i in currentPath.iterdir())
print(Counter(gen))



import pathlib
from collections import Counter
currentPath = pathlib.Path.cwd()
gen = (i.suffix for i in currentPath.glob('*.txt'))  # 获取当前文件下的所有 txt 文件，并统计其个数。
print(Counter(gen))
gen = (i.suffix for i in currentPath.rglob('*.txt'))  # 获取目录中子文件夹下的所有 txt 文件，并统计其个数。
print(Counter(gen))