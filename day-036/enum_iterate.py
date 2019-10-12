from enum import Enum

# 创建
class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500
    OTHER = 200

# 迭代
for status in HttpStatus:
    print('{} : {}'.format(status.name, status.value))

print('\n')

# 使用
# print([name for name, member in HttpStatus.__members__.items() if member.name != name])
for name, member in HttpStatus.__members__.items():
    print('{} : {}'.format(name, member))



