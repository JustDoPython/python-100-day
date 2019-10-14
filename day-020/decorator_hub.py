# 定义装饰器
def IAmDecorator(fun):
    def wrapper(*args, **kw):
        print("我真的是一个装饰器")
        return fun(*args, **kw)
    return wrapper

# 定义保留原函数属性的装饰器
import functools
def IAmDecorator(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        print("我真的是一个装饰器")
        return fun(*args, **kw)
    return wrapper

# 定义伪装饰器
def IAmFakeDecorator(fun):
    print("我是一个假的装饰器")
    return fun

# 仅定义原函数
def func_origin():
    print("我是原函数")

# 定义带装饰器的函数
@IAmDecorator
def func():
    print("我是原函数")


# ---- 关于函数参数的示例 1 ----!
# 内部函数返回值是函数对象，即不带参数
def IAmDecorator(fun):
    def wrapper(*args, **kw):
        print("我真的是一个装饰器")
        return fun
    return wrapper

# 为演示参数的影响，增加了参数的原函数
@IAmDecorator
def func(h):
    print("我是原函数")