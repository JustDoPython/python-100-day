import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("IP","端口号","用户名", "密码")
# # 执行命令
catin, catout,caterr = ssh.exec_command('cd data;cat paramiko.txt')
# # 结果放到stdout中，如果有错误将放到stderr中
print(catout.read().decode('utf-8'))
ssh.close()
