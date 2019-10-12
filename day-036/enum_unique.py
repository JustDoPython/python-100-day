from enum import Enum, unique

# 创建
@unique
class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500
    OTHER = 200

# ValueError: duplicate values found in <enum 'HttpStatus'>: OTHER -> OK
print(HttpStatus)

