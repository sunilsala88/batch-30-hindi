

import datetime as dt

#epoch to datetime
epoch1=1742124239
n1=dt.datetime.fromtimestamp(epoch1)
print(n1)
n1=n1+dt.timedelta(minutes=1,seconds=1)

#datetime to epoch
n2=n1.timestamp()
print(n2)


#string to datetime
s1='2024-21-03'
f='%Y-%d-%m'
dt1=dt.datetime.strptime(s1,f)
print(dt1)

s1='2024-Jan-15 59&30'
f='%Y-%b-%d %M&%S'
dt2=dt.datetime.strptime(s1,f)
print(dt2)

#datetime to string
print(n1)
f='%b %a'
ans=dt.datetime.strftime(n1,f)
print(ans)
print(type(n1))
print(type(ans))