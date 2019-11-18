import http

# 打印“OK”对应的状态码
print('"OK" match to "{}"'.format(http.HTTPStatus.OK))

# 打印“NOT FOUND”对应的状态码
print('"NOT_FOUND" match to "{}"'.format(http.HTTPStatus.NOT_FOUND))


# 打印状态码对应的状态短语
while True:
    st_code = input("请输入要查询的状态码：（输入 q 退出）\n")

    try:
        print("状态为：{}\n".format(http.HTTPStatus(int(st_code)).phrase))
    except ValueError:
        if st_code == 'q':
            break
        print("对应的状态码 {} 不存在\n".format(st_code))
