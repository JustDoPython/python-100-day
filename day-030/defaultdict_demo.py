from collections import defaultdict

default_dict = defaultdict(int)
default_dict["x"] = 10

print(default_dict["x"])
print(default_dict["y"])

def getUserInfo():
    return {
        "name" : "",
        "age" : 0
    }

default_dict = defaultdict(getUserInfo)
admin = default_dict["admin"]
print(admin)
admin["age"] = 34
print(admin)