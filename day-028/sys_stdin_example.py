import sys


# 使用 with 语句打开文件对象，使其可以自动关闭
with open('hello_python.txt', 'r', encoding='utf-8') as f:
    sys.stdin = f
    try:
        # 一直输出输入流中的内容
        while True:
            print(input())
    
    # 若遇文件结束标识则退出
    except EOFError:
        exit()