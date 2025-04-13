
import yfinance as yf
import mplfinance as mpf
data=yf.download('TSLA',period='5y')
data.columns=[i[0] for i in data.columns]
print(data)


import pandas_ta as ta
d=ta.bbands(data['Close'],length=20)
print(d)
# data['upper']=d['BBU_20_2.0']
# data['lower']=d['BBL_20_2.0']
# data


# # mpf.plot(data,type='candle',volume=True,show_nontrading=False,style='yahoo')
# a1=mpf.make_addplot(data['upper'],color='blue')
# a2=mpf.make_addplot(data['lower'],color='black')
# mpf.plot(data,type='candle',style='yahoo',addplot=[a1,a2],volume=True)

#rsi
# r=ta.rsi(data['Close'],15)
# print(r)

# a2=mpf.make_addplot(r,color='black',panel=1)
# mpf.plot(data,type='candle',style='yahoo',addplot=[a2],volume=True)

#adx
# adx1=ta.adx(data['High'],data['Low'],data['Close'],length=14)
# print(adx1)

# data['adx']=adx1['ADX_14']
# a2=mpf.make_addplot(data['adx'],color='black',panel=1)
# mpf.plot(data,type='candle',style='yahoo',addplot=[a2],volume=True)

#supertrend
# super=ta.supertrend(data['High'],data['Low'],data['Close'],length=14)
# print(super)

# a1=mpf.make_addplot(super['SUPERTl_14_3.0'],color='blue')
# a2=mpf.make_addplot(super['SUPERTs_14_3.0'],color='black')
# mpf.plot(data,type='candle',style='yahoo',addplot=[a1,a2],volume=True)

#william %r
# w=ta.willr(data['High'],data['Low'],data['Close'],length=15)
# print(w)
# a2=mpf.make_addplot(w,color='black',panel=1)
# mpf.plot(data,type='candle',style='yahoo',addplot=[a2],volume=True)


