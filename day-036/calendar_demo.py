# 1 calendar 模块方法与属性
import calendar

# calendar.setfirstweekday(calendar.SUNDAY)

# print(calendar.firstweekday())

# print(calendar.isleap(9102))

# print(calendar.leapdays(1945,2019))

# print(calendar.weekday(2019,10,1))

# print(calendar.monthrange(2019, 10))

# print(calendar.monthcalendar(2019,10))

# print(calendar.prmonth(2019,10))

# print(calendar.prcal(2019))

# print(calendar.day_name[0])

# print(calendar.day_abbr[0])

# print(calendar.month_name[1])

# print(calendar.month_abbr[1])

# 2 Calendar 实例方法
# from calendar import Calendar
#
# c = Calendar()
# print(list(c.iterweekdays()))

# print(list(c.itermonthdates(2019,10)))

# print(list(c.itermonthdays2(2019,10)))

# print(list(c.itermonthdays3(2019,10)))

# 3 TextCalendar 实例方法

# from calendar import TextCalendar
#
# tc = TextCalendar()
# print(tc.formatmonth(2019,10))

# print(tc.prmonth(2019,10))

# print(tc.formatyear(2019))

# print(tc.pryear(2019))

# 3 HTMLCalendar 实例方法
from calendar import HTMLCalendar

hc = HTMLCalendar()

# print(hc.formatmonth(2019,10))

# print(hc.formatyear(2019))

print(hc.formatyearpage(2019))
