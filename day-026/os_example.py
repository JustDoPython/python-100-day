import os

# 打印系统型号
print("打印系统型号")
print(os.name)
print()

# 打印环境变量
print("打印环境变量")
for item in os.environ:
    print(item, ": ", os.environ[item])
print()

# 获取当前目录下全部文件名的函数
def get_filelists(file_dir='.'):
    list_directory = os.listdir(file_dir)
    filelists = []
    for directory in list_directory:
        # os.path 模块稍后会讲到
        if(os.path.isfile(directory)):
            filelists.append(directory)
    return filelists