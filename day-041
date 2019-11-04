from operator import *

class Student:
    pass

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return '%s(name=%r,score=%r)' % (self.__class__.__name__, self.name, self.score)

if __name__ == '__main__':
    students = [Student("zhangSan", 89),
                Student("liSi", 60),
                Student("wangWu", 70),
                Student("xiaoMing", 100)]


    print("按分数排序: ")
    print(sorted(students, key=attrgetter('score'), reverse=True))

    g = attrgetter("score") # 
    vals = [g(i) for i in students]
    print("获取分数属性: ")
    print (vals)
