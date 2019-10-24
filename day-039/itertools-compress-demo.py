import itertools
data = [81, 82, 84, 76, 64, 78]
tf = [1,1,0,1,1,0]
print(list(itertools.compress(data, tf)))