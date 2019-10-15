from collections import OrderedDict

user = OrderedDict()
user["name"] = "admin"
user["age"] = 23
user["weight"] = 65
print(user)

user.move_to_end("name")
print(user)

user.move_to_end("name", last = False)
print(user)