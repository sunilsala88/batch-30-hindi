
import datetime as dt

a='2025-03-15'

d1=dt.date(2025,3,15)
print(d1)


t1=dt.time(12,12,13)
print(t1)

dt1=dt.datetime(2025,12,31)
print(dt1)

td1=dt.timedelta(days=1)
print(td1)

m=dt.timedelta(minutes=1)

print(dt1+td1+m)

thurdays_list=[]
current_day=dt.datetime(2024,1,1)
d1=dt.timedelta(days=1)
for i in range(365):
    current_day=current_day+d1
    # print(current_day)
    if current_day.weekday()==3:
        thurdays_list.append(current_day)
        print(current_day)
    
print(thurdays_list)
print(len(thurdays_list))