a = [1, 'hello', [1, 2]]
b = list(a)

a[0] = 100
a[2][0] = 100

print(a)
print(b)
print(a is b)

a = [1, 2, 3]
b = a[:]
print(a == b)
print(a is b)


a = (1, 2, 3)
b = tuple(a)
print(a == b)
print(a is b)


import copy

a = [1, 'hello', [1,2]]
b = copy.deepcopy(a)

a[0] = 100
a[2][0] = 100
print(a)
print(b)

a = (1,2,3)
b = copy.deepcopy(a)
print(a is b)

a = (1,2,[1,2])
b = copy.deepcopy(a)
print(a is b)

a[2][0] = 100
print(a)
print(b)
