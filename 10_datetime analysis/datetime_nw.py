import datetime as dt
# from datetime import datetime

d1=dt.datetime(2024,1,1)
print(d1)

t1=dt.timedelta(days=1)
print(d1+t1)

ct=dt.datetime.now()
print(ct)

print(ct.timestamp())
import time
print(time.time())

n1=1742642005
y1=dt.datetime.fromtimestamp(n1)
print(y1)

#string
print(y1.strftime('%Y=%m'))

st1='2024-01-02 10:20:40'
f="%Y-%m-%d %H:%M:%S"
i1=dt.datetime.strptime(st1,f)
print(i1)

import yfinance as yf
data=yf.download('TSLA',period='7d',interval='1m')

#utc et convert
data.columns
l1=[]
for i in data.columns:
    l1.append(i[0])
data.columns= l1

data=data.reset_index()
print(data)
tz1='Asia/Kolkata'
print(data['Datetime'].dt.tz_convert(tz1).dt.tz_localize(None))