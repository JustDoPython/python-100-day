import builtins

# 作用域的概述及运用
global_scope = 0  # 全局作用域

# 定义闭包函数中的局部作用域
def outer():
    o_count = 1  # 闭包函数外的函数中，相对于函数 inner() 来说 作用域非局部
    def inner():
       local_scope = 2  # 局部作用域

# 查看模块中引入哪些变量
print('builtins 模块中引入的变量为：%s' %dir(builtins))


# # 其他模块中的变量访问
name1 = 'SuSan'
if('SuSan'.__eq__(name1)):
    result = 'I am SuSan,I am from China'
else:
    result = 'I am from USA'

print(result)


# 如果将变量定义在函数内部，则外部不能访问
def names():
    name2 = 'SuSan'

# if('SuSan'.__eq__(name2)):
    result1 = 'I am '+name2 +','+'I am from China'
# else:
    result1 = 'I am from USA'

# print(result1)



# 全局变量和局部变量
total = 0  # 这是一个全局变量
# 函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total

# 调用sum函数，传入参数的计算结果显示局部变量
sum(10, 20)
print("函数外是全局变量 : ", total)


# 使用golbal 关键字访问和修改全局变量
num = 1
def fun1():
# 申明访问全局变量
    global num  # 需要使用 global 关键字声明
# 输出全局变量原始值
    print(num)
#　修改全局变量
    num = 123
    print(num)
# 调用函数
fun1()
# 输出修改后的全局变量值
print(num)


# 使用nonlocal关键字申明变量并修改
# 定义函数
def outer():
# 定义变量
    num = 10
    #　定义嵌套函数
    def inner():
        nonlocal num   # nonlocal关键字声明，使用函数中变量
        # 修改变量值
        num = 100
        print(num)
    inner()
    print(num)
outer()


#　特殊情况下
b = 8
def test(b):
    b = b * 10
    print(b)
test(b)


b = 8
def test():
    global b
    b = b * 30
    print(b)
test()