import itertools
x = itertools.cycle("XYZ")
for k in x:
	print(k, end = ", ")