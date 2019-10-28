import paramiko

transport = paramiko.Transport(("IP", 端口号))
transport.connect(username = "用户名", password = "密码")
sftp = paramiko.SFTPClient.from_transport(transport)
# 下载文件
sftp.get("远程服务器文件地址",'本地文件名',print("上传完成"))
# 上传文件
sftp.put('本地文件地址','远程服务器文件地址')
# 关闭连接
transport.close();
