from reprlib import recursive_repr
class MyList(list):
    @recursive_repr()
    def __repr__(self):
        return '<' + '|'.join(map(repr, self)) + '>'
m = MyList('abc')
m.append(m)
m.append('x')
print(m)


# 递归实例演示
import reprlib
a = [1,2,3,[4,5],6,7]
reprlib.aRepr.maxlevel = 1
print(reprlib.repr(a))


# array 模块实例
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(array('H', [10, 700]))

