import datetime

print('请输入年份判断是否为闰年')
year = int(input('请输入年份：'))
dt = datetime.date(year=year, month=3, day=1)
time_delta = datetime.timedelta(days=1)
last_day_of_feb = dt - time_delta
if last_day_of_feb.day == 29:
    print('yes')  # 闰年
else:
    print('no')   # 平年
我再次对文件进行更改测试