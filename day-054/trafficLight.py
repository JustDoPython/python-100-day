import threading
import time

event = threading.Event()


def drive(name):
    i = 0
    while True:
        i = i + 1
        print(name + "正在行驶中，行驶了" + str(i * 60) + "Km")
        time.sleep(1)
        event.wait()
        print(name + "通过了红灯")


def sign():
    print("绿灯初始化")
    event.set()
    while True:
        # 红绿灯切换时间为3秒
        time.sleep(3)
        if event.isSet():
            print("红灯亮起，所有行驶中的车辆不允许通过")
            event.clear()
        else:
            print("绿灯亮起，所有行驶中的车辆必须通过")
            event.set()


if __name__ == '__main__':

    # 设置公路线程组
    highwayThreads = []

    # 创建汽车新线程
    bmwCar = threading.Thread(target = drive, args=("BMWCar", ))
    vwCar = threading.Thread(target = drive, args=("VWCar", ))


    # 将汽车线程添加到公路线程组
    highwayThreads.append(bmwCar)
    highwayThreads.append(vwCar)

    # 汽车启动
    for thread in highwayThreads:
        thread.start()

    # 红绿灯发送事件通知
    sign()
