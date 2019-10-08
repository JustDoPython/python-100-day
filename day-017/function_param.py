# -*-coding:UTF-8-*-

# 默认值函数测试
def def_param_fun(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# 函数调用
# def_param_fun('Do you really want to quit?')
# def_param_fun('Do you really want to quit?', 2)
# def_param_fun('Do you really want to quit?', 2, 'Come on, only yes or no!')

# 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要
def f(a, l=[]):
    l.append(a)
    return l


# def f(a, l=None):
#     if l is None:
#         l = []
#     l.append(a)
#     return l

# print(f(1))
# print(f(2))
# print(f(3))

# 可变参数
def variable_fun(kind, *arguments, **keywords):
    print("friend : ", kind, ";")
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# 调用1
# variable_fun("xiaoming",
#              "hello xiaoming", "nice to meet you!",
#             mother="xiaoma",
#             father="xiaoba",
#             son="see you")

# 调用2
# list01 = ["hello xiaoming", "nice to meet you!"]
# dict01 = {'mother': 'xiaoma', 'father': 'xiaoba', 'son': 'see you'}
# variable_fun("xiaoming", *list01, **dict01)


# 关键字参数 以下函数接受一个必需的参数（voltage）和三个可选的参数（state, action，和 type）
def key_fun(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This key_fun wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

key_fun(1000)                                          # 1 positional argument
key_fun(voltage=1000)                                  # 1 keyword argument
key_fun(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
key_fun(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
key_fun('a million', 'bereft of life', 'jump')         # 3 positional arguments
key_fun('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# 重复传入参数，不允许
# TypeError: key_fun() got multiple values for argument 'voltage'
key_fun(100, voltage=1000)                             # error


