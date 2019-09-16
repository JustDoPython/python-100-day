#定义一个函数
def hello() :
   print("Hello World!")

#调用函数
hello()

#定义一个函数
def helloN(name) :
   print("Hello World!", name)

#调用函数
helloN('neo')

#定义函数
def add(a,b) :
   return a+b

def reduce(a,b) :
   return a-b

def multiply(a,b) :
   return a*b

def divide(a,b) :
   return a/b

#调用函数
print(add(1,2))
print(reduce(12,2))
print(multiply(6,3))
print(divide(12,6))

#定义多个返回值函数
def more(x, y):
    nx = x + 2
    ny = y - 2
    return nx, ny

#调用函数
x, y = more(10, 10)
print(x, y)  


#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

#调用递归函数
print(fact(6)) 