import csv

# with open('test.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['1001', '张三', '222'])
    # 写入多行
    # data = [('1001', '张三', '21'), ('1002', '李四', '31')]
    # writer.writerows(data)

# with open('test.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=' ')
#     for row in reader:
#         print(', '.join(row))

# csv.register_dialect('mydialect', delimiter='|', quoting=csv.QUOTE_ALL)
# with open('test.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, 'mydialect')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['1001', '张三', '222'])
# with open('test.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=' ')
#     for row in reader:
#         print(', '.join(row))

# with open('test.csv', 'w', newline='') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '1001', 'name': '张三', 'age': '21'})
#     writer.writerow({'id': '1002', 'name': '李四', 'age': '31'})
# with open('test.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=' ')
#     for row in reader:
#         print(', '.join(row))

# with open('test.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['id'], row['name'], row['age'])

# with open('test.csv', newline='') as csvfile:
#      dialect = csv.Sniffer().sniff(csvfile.read(1024))
#      csvfile.seek(0)
#      reader = csv.reader(csvfile, dialect)
#      for row in reader:
#          print(row)
