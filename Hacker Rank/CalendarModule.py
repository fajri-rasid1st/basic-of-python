import datetime
import calendar

s = input()

day = datetime.datetime.strptime(s, "%m %d %Y")
print((calendar.day_name[day.weekday()]).upper())
