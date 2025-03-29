#matplotlib
#mplfinance

import yfinance as yf
data=yf.download('TSLA',period='5y')
data.columns=[i[0] for i in data.columns]
print(data)

import pandas_ta as ta
data['sma']=ta.sma(data['Close'],length=20)
data['ema']=ta.ema(data['Close'],length=10)

import mplfinance as mpf
# mpf.plot(data,type='candle',volume=True,show_nontrading=False,style='yahoo')
# a1=mpf.make_addplot(data['sma'],color='blue')
# a2=mpf.make_addplot(data['ema'],color='black')
# mpf.plot(data,type='candle',style='yahoo',addplot=[a1,a2],volume=True)
mpf.plot(data,type='renko',style='yahoo')