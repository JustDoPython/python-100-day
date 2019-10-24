import itertools
x = itertools.takewhile(lambda x: x < 5, [1,3,5,7,4,2,1])
print(list(x))