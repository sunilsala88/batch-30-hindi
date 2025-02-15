
#parameter
#argumnet

def calcualte_months(monthly:int,final:int)->int:
    """
    this will calcualte how many months is req
    to real the final value
    """

    intrest=0.05
    months=0
    current_money=0
    while True:
        if current_money>=final:
            break
        
        current_money=current_money+(current_money*(intrest/12))+monthly
        months=months+1
   

    return months

m=calcualte_months(500,10_000)
print(m)


def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

a=evenOdd(10)
print(a)





def take_stock_input(stock_prices:dict)->dict:
    """
    take input of stocks and return portfolio dict
    """
    print(abc)
    portfolio={}
    while True:
        name=input('enter the stock name?: ')
        if name.upper()=='Q':
            break
        if name=='nifty':
            print('you cannot trade this stock type again?')
            continue
        found=stock_prices.get(name)
        if found:
            portfolio.update({name:found})
        else:
            print('this stock does not exist')
    return (portfolio)


stock_prices={'amzn':400,'tsla':900,'goog':578,'nifty':6353}
p=take_stock_input(stock_prices)
abc=100
print(p)



