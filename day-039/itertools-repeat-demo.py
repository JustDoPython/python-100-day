import itertools
#x = itertools.repeat("XYZ")
x = itertools.repeat("XYZ", 3)
for k in x:
	print(k, end = ", ")