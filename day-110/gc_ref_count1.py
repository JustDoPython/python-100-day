import os
import psutil


# 打印 python 程序占用的内存大小
def print_memory_info(name):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    MB = 1024 * 1024
    memory = info.uss / MB
    print('%s used %d MB' % (name, memory))


def foo():
    print_memory_info("foo start")
    length = 1000 * 1000
    list = [i for i in range(length)]
    print_memory_info("foo end")


foo()
print_memory_info("main end")
