# 导入模块
import hello
 
# 现在可以调用模块里包含的函数了
hello.sayhello()


## 直接导入方法
from hello import sayhello
sayhello()



## 导入所有方法
from hello import *
sayhello()
world()


print("测试包的使用")

import cal.calculator
print(cal.calculator.add(1,2))


from cal import calculator
# 使用包的模块的方法
print(calculator.multiply(3,6))