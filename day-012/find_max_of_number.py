def findMaxofNumber():
    '''
    打印并返回 Python 常量池中的最大数值
    '''
    for b in range(300):
        if b is not range(300)[b]:
            print("常量池最大值为：", (b - 1))
            return (b - 1)

if __name__ == '__main__':
    findMaxofNumber()