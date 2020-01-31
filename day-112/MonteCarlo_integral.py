import random


def solve_integral(repeat = 20000) -> float:
    '''
    :param repeat: integral

    :return: float
    '''
    
    count = 0
    for i in range(repeat):
        x = random.random()
        y = random.random()
        if y > x*x:
            count += 1

    ratio = count / repeat
    integral = ratio * 1
    return integral

if __name__ == "__main__":
    repeat = int(input("请输入实验次数："))
    print(solve_integral(repeat))
