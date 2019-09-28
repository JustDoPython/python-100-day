from threading import Timer
import time
#定时器-单次执行
# def work():
#     print("Hello Python")
# # 5 秒后执行 work 方法
# t = Timer(5, work)
# t.start()

#定时器-重复执行
count = 0
def work():
    print('当前时间：', time.strftime('%Y-%m-%d %H:%M:%S'))
    global t, count
    count += 1
    # 如果 count 小于 5，开始下一次调度
    if count < 5:
        t = Timer(1, work)
        t.start()
# 指定 2 秒后执行 work 方法
t = Timer(2, work)
t.start()