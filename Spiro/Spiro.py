import turtle
import math
import random

import sys

class Spiro:
    def __init__(self, R, r, l, num, color):
        """
        :params R: int. 大圆半径
        :params r: int. 小圆半径
        :params l: float. 画笔到小圆圆心的距离与小圆半径之比，在[0,1)区间
        :params num: int. 要画的完整曲线个数
        :params color: string, (int, int, int), (float, float, float). 指定曲线颜色
        """
        self.R = R
        self.r = r
        self.l = l
        self.num = num
        self.pen = turtle.Turtle()
        self.pen.pencolor(color)
        turtle.colormode(1.0)
        

    def drawSingleSpiro(self):
        # 周期数 p
        p = self.periods()

        for i in range(0, 360*p + 2, 2):
            if i != 0:
                self.pen.setpos(*self.cor_x_y_Spiro(i))
            else:
                self.pen.up()
                self.pen.setpos(*self.cor_x_y_Spiro(i))
                self.pen.down()


    def drawWhole(self):
        for s in range(self.num):
            if s != 0:
                self.randomSetting()
                self.drawSingleSpiro()
            else:
                self.drawSingleSpiro()


    def randomSetting(self):
        self.l = random.random()

        # r = int(random.random() * 255)
        # g = int(random.random() * 255)
        # b = int(random.random() * 255)
        r = random.random()
        g = random.random()
        b = random.random()
        self.pen.pencolor((r, g, b))


    def hcf(self, x, y):
        if x == y:
            result = x
        elif x > y:
            result = self.hcf(x-y, y)
        else:
            result = self.hcf(x, y-x)
        return result


    def periods(self):
        div = self.hcf(self.R, self.r)
        return self.r//div
    

    def cor_x_y_Spiro(self, theta):
        k = self.r/self.R
        ef = 1 - k
        
        rad = self.degreeToRadian(theta)
        x = self.R*(ef*math.cos(rad) + self.l*k*math.cos(ef/k*rad))
        y = self.R*(ef*math.sin(rad) - self.l*k*math.sin(ef/k*rad))
    
        return (x, y)
    

    def degreeToRadian(self, degree):
        return degree * math.pi / 180

if __name__ == "__main__":
    # s = Spiro(100, 40, 0.6, 10, "pink")
    # s.drawWhole()
    # turtle.mainloop()
    if len(sys.argv) == 1:
        """
        示例输入：python Spiro.py
        """
        s = Spiro(100, 40, 0.6, 10, "pink")
        s.drawWhole()
        turtle.mainloop()
    elif len(sys.argv[5].split(',')) == 1:
        """
        示例输入：python Spiro.py 100 40 0.6 10 pink
        """
        s = Spiro(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), 
                int(sys.argv[4]), sys.argv[5])
        s.drawWhole()
        turtle.mainloop()
    else:
        """
        示例输入：python Spiro.py 100 40 0.6 10 "251,165,59"
        """
        rgb_list = sys.argv[5].split(',')
        rgb =[]
        for color in rgb_list:
            color = int(color)/255
            rgb.append(color)
        
        rgb = tuple(rgb)
        s = Spiro(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), 
                    int(sys.argv[4]), rgb)
        s.drawWhole()
        turtle.mainloop()
    # print(sys.argv)
    # # print(sys.argv[1].split(','))
    # int('25,36,55')
