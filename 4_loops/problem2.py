
stock_prices={'amzn':400,'tsla':900,'goog':578,'nifty':6353}
portfolio={}

#break stops the looop
#continue restarts the loop by skipping the code after continue

# while True:
#     name=input('enter the stock name?: ')
#     if name.upper()=='Q':
#         break
#     if name=='nifty':
#         print('you cannot trade this stock type again?')
#         continue
#     found=stock_prices.get(name)
#     if found:
#         portfolio.update({name:found})
#     else:
#         print('this stock does not exist')
# print(portfolio)


#truthy ans flasy value

#falsy
#0,"",[],{},(),None,False

# a=10
# b=10<11
# print(b)
# if None:
#     print('inside if')
# else:
#     print('inside else')



monthly=500
final=10_000
intrest=0.05
months=0
#20
current_money=0
while True:
    if current_money>=final:
        break
    
    current_money=current_money+(current_money*(intrest/12))+monthly
    months=months+1
    print(current_money)
print(months)