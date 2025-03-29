import yfinance as yf
data=yf.download('TSLA',period='5y')
data.columns=[i[0] for i in data.columns]
print(data)

import pandas_ta as ta
data['sma']=ta.sma(data['Close'],length=20)

# how to install talib
# https://youtu.be/ZA8BNzUkyY4?si=IshM-xjRZ8zH8ib0
# https://youtu.be/M3n_H3fIoGo?si=psmcHkxm97NF0Way


data['ema']=ta.ema(data['Close'],length=10)
print(data)
#erros
#ModuleNotFoundError: No module named 'pkg_resources'
#pip install setuptools

#cannot import name 'NaN' from 'numpy' 
#pip install numpy==1.26.4