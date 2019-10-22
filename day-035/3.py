from pathlib import Path
currentPath = Path.cwd()
makePath = currentPath / 'python-100'
makePath.mkdir()
print("创建的目录为:%s" %(nmakePath))


from pathlib import Path
currentPath = Path.cwd()
delPath = currentPath / 'python-100'
delPath.rmdir()
print("删除的目录为:%s" %(delPath))