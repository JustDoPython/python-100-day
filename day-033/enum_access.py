from enum import Enum

# 创建
class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500

# value 访问使用元组()
print(HttpStatus(200))      # HttpStatus.OK
# name 访问使用list[]
print(HttpStatus['OK'])     # HttpStatus.OK

# 赋值给 enum对象
number = HttpStatus.OK
print(number)               # HttpStatus.OK





