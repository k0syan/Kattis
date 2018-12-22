import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
d = input().split()
day, month = int(d[0]), int(d[1])
year = 2009
print(days[datetime.datetime(year, month, day).weekday()])
