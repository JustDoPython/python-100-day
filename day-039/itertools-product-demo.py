import itertools
print(list(itertools.product("ab", "12")))
print(list(itertools.product("ab", "ab")))
print(list(itertools.product("ab", repeat=2)))