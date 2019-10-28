import paramiko


try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("IP","端口号","用户名", "密码", timeout=5)
    sftp = client.open_sftp()
    for fileName in sftp.listdir("/root/data"):
        if fileName.endswith(".txt"):
            print(fileName)
except:
    print('文件没有找到!')
finally:
    client.close()
