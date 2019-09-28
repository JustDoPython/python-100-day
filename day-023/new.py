#创建线程-构造器方式
import time
import threading
def work(num):
    print('线程名称：',threading.current_thread().getName(),'参数：',num,'开始时间：',time.strftime('%Y-%m-%d %H:%M:%S'))
if __name__ == '__main__':
    print('主线程开始时间：',time.strftime('%Y-%m-%d %H:%M:%S'))
    t1 = threading.Thread(target=work,args=(3,))
    t2 = threading.Thread(target=work,args=(2,))
    t3 = threading.Thread(target=work,args=(1,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('主线程结束时间：', time.strftime('%Y-%m-%d %H:%M:%S'))

#创建线程-继承方式
class MyThread(threading.Thread):
    def __init__(self,num):
        super().__init__()
        self.num = num
    def run(self):
        print('线程名称：', threading.current_thread().getName(), '参数：', self.num, '开始时间：', time.strftime('%Y-%m-%d %H:%M:%S'))
if __name__ == '__main__':
    print('主线程开始时间：',time.strftime('%Y-%m-%d %H:%M:%S'))
    t1 = MyThread(3)
    t2 = MyThread(2)
    t3 = MyThread(1)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('主线程结束时间：', time.strftime('%Y-%m-%d %H:%M:%S'))