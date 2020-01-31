import random


def solve_pi(repeat = 20000) -> float:
    '''
    :param repeat: integral

    :return: float
    '''
    count = 0
    for i in range(repeat):
        x = random.random()
        y = random.random()
        if x*x + y*y < 1.0:
            count += 1

    ratio = count / repeat
    PI = 4 * ratio
    return PI

if __name__ == "__main__":
    repeat = int(input("请输入实验次数："))
    print(solve_pi(repeat))
