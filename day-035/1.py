from pathlib import Path
currentPath = Path.cwd()
homePath = Path.home()
print("文件当前所在目录:%s\n用户主目录:%s" %(currentPath, homePath))