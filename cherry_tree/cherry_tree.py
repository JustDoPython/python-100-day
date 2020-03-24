import turtle
import random

def cherryTree(branch, t):
    if branch > 4:
        if 7 <= branch <= 13:
            # 随机数生成
            if random.randint(0, 3) == 0:
                t.color('snow')  # 花瓣心的颜色
            else:
                t.color('pink')  #花瓣颜色
            # 填充的花瓣大小
            t.pensize( branch / 6)
        elif branch < 8:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                # 设置樱花树叶颜色
                t.color('green')  # 樱花树颜色
            t.pensize(branch / 5)
        else:
            t.color('Peru')  # 树干颜色
            t.pensize(branch / 11)  #调整树干的粗细
        t.forward(branch)

        a = 1 * random.random()
        t.right(20 * a)
        b = 1 * random.random()
        cherryTree(branch - 10 * b, t)
        t.left(60 * a)
        cherryTree(branch - 10 * b, t)
        t.right(40 * a)
        t.up()
        t.backward(branch)
        t.down()

# 掉落的花瓣 参数是画板和笔
def petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        # 向左移动
        t.left(75)
        # 向前移动
        t.forward(a)
        # 放下画笔
        t.down()
        # 设置花瓣颜色
        t.color('pink')  # 粉红色
        # 画个小圆当作花瓣
        t.circle(1)
        # 提起画笔
        t.up()
        # 画笔向后退
        t.backward(a)
        # 画笔向前行
        t.right(70)
        t.backward(b)

# 描述樱花的句子
def des_word():
    t.color('LightCoral') # 字体颜色设置
    t.hideturtle()
    t.goto(-50,-130)
    t.pu()
    # 昨日雪如花，今日花如雪，山樱如美人，红颜易消歇。
    t.write('昨日雪如花,',move=False, align='center', font=('Arial', 20, 'normal'))
    t.pd()

    t.pu()
    t.goto(90,-130)
    t.write('今日花如雪', move=False, align='center', font=('Arial', 20, 'normal'))
    t.pd()


# 绘图区域
t = turtle.Turtle()
# 画布大小 获取到屏幕
w = turtle.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(8, 0)  # 获取屏幕大小
w.screensize(bg='LightCyan')  # 设置屏幕背景颜色
t.left(80)
t.up()
t.backward(140)
t.down()
t.color('sienna')
cherryTree(50, t)
petal(300, t)
des_word()
# 点击屏幕任意地方退出
w.exitonclick()

