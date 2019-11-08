import paramiko
import select
import sys
import tty
import termios


# 创建一个安全的通道
trans = paramiko.Transport(('IP地址', 22))
# 启动一个客户端
trans.start_client()

# 如果使用用户名和密码登录
trans.auth_password(username='用户名', password='密码')
# 打开一个通道
channel = trans.open_session()
# 获取一个终端
channel.get_pty()
# 激活终端
channel.invoke_shell()

# 获取Linux操作终端的属性
oldtty = termios.tcgetattr(sys.stdin)
try:
    # 将Linux操作终端的属性设置为 SSH 服务器的终端属性，并使用 TAB 键
    tty.setraw(sys.stdin)
    channel.settimeout(0)

    while True:
        read_list, write_list, err_list = select.select([channel, sys.stdin,], [], [])
        # 输入命令，sys.stdin会发生变化
        if sys.stdin in read_list:
            # 获取输入的内容
            input_cmd = sys.stdin.read(1)
            # 将命令发送给服务器
            channel.sendall(input_cmd)

        # SSH服务器返回结果
        if channel in read_list:
            result = channel.recv(1024)
            # 断开连接后退出
            if len(result) == 0:
                print("连接断开了！")
                break
            sys.stdout.write(result.decode())
            sys.stdout.flush()
finally:
    # 还原Linux终端属性
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

channel.close()
trans.close()
