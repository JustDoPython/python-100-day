def sayHello(name): # name 为形式参数
    print("Hello %s" % name)


name = "hanmeimei" # 实际参数
sayHello(name)

def swap(a, b):
    a, b = b, a
    print("in swap a = %d and b = %d " % (a, b))


a = 100
b = 200
swap(a, b)
print("in main a = %d and b = %d " % (a, b))