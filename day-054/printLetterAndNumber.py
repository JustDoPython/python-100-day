import threading
from threading import Event


# 打印字母函数
def printLetter(letterEvent, numEvent):
    for item in ["a", "b", "c"]:
        letterEvent.wait()
        print(item, end="")
        letterEvent.clear()
        numEvent.set()


# 打印数字函数
def printNum(numEvent, letterEvent):
    for item in [2, 4, 6]:
        numEvent.wait()
        print(item, end=" ")
        numEvent.clear()
        letterEvent.set()


if __name__ == '__main__':
    letterEvent, numEvent = Event(), Event()
    t1 = threading.Thread(target= printLetter, args=(letterEvent, numEvent))
    t2 = threading.Thread(target= printNum, args=(numEvent, letterEvent))

    threads = []
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()

    letterEvent.set()
