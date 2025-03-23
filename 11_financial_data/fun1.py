



import yfinance as yf
data=yf.download('^NSEBANK',start='2021-01-01',end='2021-12-31')
print(data)
data.columns=[i[0] for i in data.columns]
print(data)


data=yf.download('^NSEBANK',period='1mo')
print(data)
data.columns=[i[0] for i in data.columns]
print(data)


data=yf.download('^NSEBANK',period='2y',interval='1h')
print(data)
data.columns=[i[0] for i in data.columns]
data.reset_index(inplace=True)
data['Datetime']=data['Datetime'].dt.tz_convert('Asia/Kolkata')
print(data)

data=yf.download('^NSEBANK',period='10d',interval='1m')
print(data)
data.columns=[i[0] for i in data.columns]
data.reset_index(inplace=True)
data['Datetime']=data['Datetime'].dt.tz_convert('Asia/Kolkata')
print(data)