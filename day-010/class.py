# 类的定义
class Car:
    pass


# 创建 Car 的实例对象 c
class Car:
    pass
c = Car()


# 定义 Car 类的属性 name
class Car:
    name = 'BMW'


'''
类方法（可调类变量、可被实例调用、可被类调用）
1、类方法通过@classmethod装饰器实现，只能访问类变量，不能访问实例变量；
2、通过cls参数传递当前类对象，不需要实例化。
'''
class Car(object):
    name = 'BMW'
    def __init__(self, name):
        self.name = name
    @classmethod
    def run(cls,speed):
        print(cls.name,speed,'行驶')
# 访问方式1
c = Car("宝马")
c.run("100迈")
# 访问方式2
Car.run("100迈")


'''
静态方法（可调类变量、可被实例调用、可被类调用）
1、用 @staticmethod 装饰的不带 self 参数的方法；
2、静态方法名义上归类管理，实际中在静态方法中无法访问类和实例中的任何属性；
3、调用时并不需要传递类或实例。
'''
class Car(object):
    name = 'BMW'
    def __init__(self, name):
        self.name = name
    @staticmethod
    def run(speed):
        print(Car.name, speed, '行驶')
# 访问方式1
c = Car("宝马")
c.run("100迈")
# 访问方式2
Car.run("100迈")


# 实例方法（可调类变量、可调实例变量、可被实例调用）
# 第一个参数强制为实例对象 self。
class Car(object):
    name = 'BMW'
    def __init__(self, name):
        self.name = name
    def run(self,speed):
        print(self.name,speed,'行驶')
# 访问
c = Car("宝马")
c.run("100迈")


# 类的继承
# 基本语法：class ClassName(BaseClassName)
# 父类
class Car(object):
    name = 'BMW'
    def __init__(self, name):
        self.name = name
    def run(self, speed):
        print(self.name, speed, '行驶')
# 子类
class BMWCar(Car):
    conf = "经济适用型"
    pass
# 调用父类 Car 中 run 方法
bc = BMWCar("BMW经济适用型轿车")
bc.run("100迈")


# 类的多态
# 父类
class Car(object):
    name = 'BMW'
    def __init__(self, name):
        self.name = name
    def run(self,speed):
        print('Car-->',self.name,speed,'行驶')
# 子类1
class BMWCar(Car):
    def run(self,speed):
        print('BMWCar-->',self.name,speed,'行驶')
# 子类2
class SVWCar(Car):
    def run(self,speed):
        print('SVWCar-->',self.name,speed,'行驶')
# 调用 run 方法
c = Car("Car")
c.run("120迈")
bc = BMWCar("宝马")
bc.run("100迈")
sc = SVWCar("大众")
sc.run("80迈")
