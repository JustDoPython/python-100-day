class Reverse:
    """反向遍历序列对象的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


if __name__ == "__main__":
    rev = Reverse('justdopython.com')
    while True:
        try:
            print(next(rev))
        except StopIteration as identifier:
            print("Iteration stopped.")
            break
