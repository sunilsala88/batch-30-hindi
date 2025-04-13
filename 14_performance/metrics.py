
import pandas_ta as ta
import yfinance as yf


data=yf.download('^NSEI',period='5y')
data.columns=[i[0] for i in data.columns]
print(data)

#cagr
a=ta.cagr(data['Close'])
print(a)

#drawdown
drawdown=ta.max_drawdown(data['Close'],method='percent')
print(drawdown)

#calmar ratio
calmar=ta.calmar_ratio(data['Close'])
print(calmar)

import numpy as np
#volatility
def volatility(DF):
    "function to calculate annualized volatility of a trading strategy"
    df = DF.copy()
    df["daily_ret"] = DF["Close"].pct_change()
    vol = df["daily_ret"].std() * np.sqrt(252)
    return vol

vol=volatility(data)
print(vol)

#sharpe ratio
sharpe=ta.sharpe_ratio(data['Close'])
print(sharpe)

#sortino ratio
sortino=ta.sortino_ratio(data['Close'])
print(sortino)