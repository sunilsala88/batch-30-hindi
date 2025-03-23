



import yfinance as yf
data=yf.download('^NSEBANK')
print(data)
print(data.info())

data.columns=[i[0] for i in data.columns]
print(data)

