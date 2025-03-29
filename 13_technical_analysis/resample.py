import yfinance as yf
data=yf.download('RELIANCE.NS',period='5d',interval='1m')
data.columns=[i[0] for i in data.columns]
print(data)

data.reset_index(inplace=True)
data['Datetime']=data['Datetime'].dt.tz_convert('Asia/Kolkata')
data.set_index('Datetime',inplace=True)
print(data)

#resample
ohlc_dict={
    "Open":'first',
    'High':'max',
    'Low':'min',
    'Close':'last',
    'Volume':'sum',

}

data=data.resample('60min').agg(ohlc_dict).dropna()
print(data.head(30))