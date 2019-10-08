# 改变变量的值，变量的标识也对应改变
python_variable = 10000
print("first id of python_variable: ", id(python_variable))
python_variable = 12345
print("second id of python_variable: ", id(python_variable))
print("\n\n")

# 即使变量的值不变，变量的标识也可能改变
python_variable = 10000
print("first id of 10000: ", id(python_variable))
python_variable = 10000
print("second id of 10000: ", id(python_variable))
print("\n\n")
# 注意，这一段示例最好在交互式环境中测试。在 IDE 中可能被优化。


# 对列表来讲，变量对应的值不变，变量标识依然可能改变
python_variable = [1,2]
print("first id of list: ", id(python_variable))
python_variable = [1,2]
print("second id of list: ", id(python_variable))
print("\n\n")


# 对变量进行运算并将结果赋值给原变量，会改变变量的标识
change_ref = 10000
print("first id of unchanged: ", id(change_ref))
change_ref = change_ref + 1
print("second value of change_ref: ", change_ref)
print("second id of changed: ", id(change_ref))
print("\n\n")


# 就地对变量所引用对象进行操作，不改变变量的标识
list_nonchange = [1, 2, 3]
print("first id of list_nonchange: ", id(list_nonchange))
list_nonchange[2] = 5
print("second value of list_nonchange: ", list_nonchange)
print("second id of list_nonchange: ", id(list_nonchange))
list_nonchange.append(3)
print("third value of list_nonchange: ", list_nonchange)
print("third id of list_nonchange: ", id(list_nonchange))
print("\n\n")


# Python 中，变量引用一个对象
const_ref = 10000
print("'const_ref == 10000' is: ", const_ref == 10000)
print("'const_ref is 10000' is: ", const_ref is 10000)
print("first id of const_ref: ", id(const_ref))
print("another id of 10000: ", id(10000))
print("\n\n")


from sys import getrefcount
print("the reference count of const_ref: ", getrefcount(const_ref))
print("the reference count of 10000: ", getrefcount(10000))
