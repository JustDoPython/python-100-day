# FIFO 队列
import queue
q = queue.Queue()
for index in range(10):
    q.put(index)
while not q.empty():
    print(q.get(), end=", ")
# 输出结果如下
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 


# LIFO 队列
import queue
q = queue.LifoQueue()
for index in range(10):
    q.put(index)
while not q.empty():
    print(q.get(), end=", ")
# 输出结果如下
# 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 


# 优先级队列，存放内置类型
import queue
q = queue.PriorityQueue()
for index in range(10,0,-1):
    q.put(index)
while not q.empty():
    print(q.get(), end=", ")
# 输出结果如下
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 


# 优先级队列，存放元组
import queue
q = queue.PriorityQueue()
q.put(["d","b"])
q.put(["c","b"])
while not q.empty():
    print(q.get(), end=", ")
# 输出结果如下
# ['c', 'b'], ['d', 'b'], 


# 优先级队列，存放自定义类型
import queue
q = queue.PriorityQueue()

class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __lt__(self, other): # 实现 < 操作
        return self.age < other.age # 如果将 < 变成 > 相当于逆序

q.put(Animal(3,"cat"))
q.put(Animal(2,"dog"))

while not q.empty():
    animal = q.get()
    print(animal.name, animal.age, end=", ")
# 输出结果如下
# dog 2, cat 3, 
