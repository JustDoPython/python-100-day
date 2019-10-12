#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###基类###

class BException(Exception):  #继承Exception基类
    pass

class CException(BException):  #继承BException基类
    pass

class DException(CException):  #继承CException基类
    pass

for cls in [BException, CException, DException]:
    try:
        raise cls()  #抛出异常
    except DException:
        print("D")
    except CException:
        print("C")
    except BException:
        print("B")


###不带异常类型的 except###

try:
    raise BException()  #抛出异常
except DException:
    print("D")
except:
    print("处理全部其它异常") #处理全部其它异常




try:
    raise BException()  #抛出异常
except (BException, DException):
    print("D")
except:
    print("处理全部其它异常") #处理全部其它异常
else:
    print("没有异常发生") #没有异常发生




try:
    raise BException()  #抛出异常
except (BException, DException):
    print("D")
except:
    print("处理全部其它异常") #处理全部其它异常
else:
    print("没有异常发生") #没有异常发生
finally:
    print("你们绕不过我，必须执行") #必须执行的代码


###异常的参数###

try:
    x = 1 / 0  # 除数为0
except ZeroDivisionError as err: #为异常指定变量err
    print("Exception")
    print(err.args) #打印异常的参数元组
    print(err) #打印参数，因为定义了__str__()


###触发异常###

def diyException(level):
    if level > 0:
        raise Exception("raise exception", level)  #主动抛出一个异常，并且带有参数
        print('我是不会执行的') #这行代码不会执行

try:
    diyException(2)  #执行异常方法
except Exception as err: #捕获异常
    print(err) #打印异常参数




#定义函数
def diyException(level):
    if level > 0:
        raise Exception("error level", level)  #主动抛出一个异常，并且带有参数
        print('我是不会执行的') #这行代码不会执行

try:
    diyException(2)  #执行异常方法
except 'error level' as err: #捕获异常
    print(err) #打印异常参数





import traceback

#定义函数
def diyException(level):
    if level > 0:
        raise Exception("error level", level)  #主动抛出一个异常，并且带有参数
        print('我是不会执行的') #这行代码不会执行

try:
    diyException(2)  #执行异常方法
except Exception: #捕获异常
    traceback.print_exc()


###用户自定义异常###

#自定义异常
class DiyError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise DiyError("my diy exception") #触发异常
except DiyError as e:
    print(e)


###预定义的清理行为###

for line in open("myfile.txt"):
    print(line, end="")


with open("myfile.txt") as f:
    for line in f:
        print(line, end="")