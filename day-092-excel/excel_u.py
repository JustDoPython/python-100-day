# excel_u.py

# 导入相应模块
import xlrd
from xlutils.copy import copy

# 打开 excel 文件
readbook = xlrd.open_workbook("test_w.xls")

# 复制一份
wb = copy(readbook)

# 选取第一个表单
sh1 = wb.get_sheet(0)

# 在第四行新增写入数据
sh1.write(3, 0, '王亮')
sh1.write(3, 1, 59)

# 选取第二个表单
sh1 = wb.get_sheet(1)

# 替换总成绩数据
sh1.write(1, 0, 246.5)

# 保存
wb.save('test_w1.xls')