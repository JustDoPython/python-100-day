import itertools
print(list(itertools.islice('123456789', 2)))
print(list(itertools.islice('123456789', 2, 4)))
print(list(itertools.islice('123456789', 2, None)))
print(list(itertools.islice('123456789', 0, None, 2)))