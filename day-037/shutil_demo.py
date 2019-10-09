import shutil

#1、文件和文件夹操作
#1)
# s = open('folder1/fsrc.txt','r')
# d = open('folder1/fdst.txt','w')
# shutil.copyfileobj(s,d,16*1024)

#2)
# shutil.copyfile('folder1/fsrc.txt','folder1/fdst.txt')

#3)
# shutil.copymode('folder1/fsrc.txt','folder1/fdst.txt')

#4)
# shutil.copystat('folder1/fsrc.txt','folder1/fdst.txt')

#5）
# shutil.copy('folder1/fsrc.txt','folder1/fdst.txt')
# shutil.copy('folder1/fsrc.txt', 'tmp/')

#6）
# shutil.copy2('folder1/fsrc.txt','folder1/fdst.txt')

#7）
# shutil.ignore_patterns('tmp*')

#8）
# shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns( 'tmp*'))

#9)
# shutil.rmtree('rm')

#10）
# shutil.move('folder1/', 'folder2/')

#11)
# print(shutil.disk_usage('folder1/'))

#12)
# print(shutil.which('python'))

#2 、归档操作
#1)
# shutil.make_archive('zipfile', 'zip', 'tmp')

#2)
# print(shutil.get_archive_formats())

#3)
# shutil.register_archive_format()

#4)
# shutil.unregister_archive_format()

#5)
# shutil.unpack_archive()

#6)
# shutil.register_unpack_format()

#7)
# shutil.unregister_unpack_format()

#8)
# shutil.get_unpack_formats()

# 3、查询终端大小
print(shutil.get_terminal_size())