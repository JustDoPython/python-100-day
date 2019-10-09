from enum import Enum

# 创建
class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500


print('Member: {}'.format(HttpStatus.OK))               # Member: HttpStatus.OK
print('Member name: {}'.format(HttpStatus.OK.name))     # Member name: OK
print('Member value: {}'.format(HttpStatus.OK.value))   # Member value: 200
print(repr(HttpStatus.OK))                              # <enum 'HttpStatus'>
print(type(HttpStatus.OK))                              # <HttpStatus.OK: 200>
print(isinstance(HttpStatus.OK, HttpStatus))            # True




