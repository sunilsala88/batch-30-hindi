
stock_prices={'tsla':500,'amzn':690,'goog':587}
#type 4
print(stock_prices.items())
total=0
for k,v in stock_prices.items():
  print(k,v)
  total=total+v
total