

#class 
#class is a blueprint of an object

#object
#its a instance of a class

#class attribute
#variable which are common for all object

#constructor
#function which is called when you create an object

#object /instance attribute
#this is unique for each student

#method
# any function created inside a class is called method

class Student:
    dress_code='while'
    scool_name='oxford'

    #contructor
    def __init__(self,name,email,phone,roll_no):
        self.name=name
        self.email=email
        self.phone=phone
        self.roll_no=roll_no
    
    def about_me(self):
        return f"my name is {self.name} and my email is {self.email}"

s1=Student('akshay','akshay@gmail.com',8999999,10)
s2=Student('vikas','vikas@gmail.com',999999999,20)

print(s1.name)
print(s2.name)

print(s1.about_me())
print(s2.about_me())



class Book:

    def __init__(self,title,author,price,quantity):
        self.title=title
        self.author=author
        self.price=price
        self.quantity=quantity

    def get_price(self):
        return round(self.price+(0.08*self.price),2)
    
    def set_price(self,price):
        self.price=price

    def set_quantity(self,q):
        self.quantity=q
    def get_quantity(self):
        return self.quantity

    def sell(self, number_sold):
        self.quantity=self.quantity-number_sold
    
my_book = Book(title="1984", author="George Orwell", price=29.99, quantity=100)
print(my_book.price)

print(my_book.get_price())
my_book.set_price(100)
print(my_book.get_price())

print(my_book.quantity)
my_book.set_quantity(200)
my_book.sell(22)
print(my_book.get_quantity())


class Circle:
    pi=3.14

    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return self.pi*(self.radius**2)

    def circumfrence(self):
        return 2*self.pi*self.radius
    
c1=Circle(10)
c2=Circle(20)
print(c1.pi)
print(c2.pi)

class BankAccount:

    def __init__(self,account_number,balance):
        self.balance=balance
        self.account_number=account_number

    def __str__(self):

        return f"{self.account_number}:{self.balance}" 
    
    def deposit(self, amount):
        self.balance=self.balance+amount
    
    def withdraw(self, amount): 
        if amount<self.balance:
            self.balance=self.balance-amount
            print('money withdrawn ',amount,'current balance is',self.balance)
        else:
            print('not enough money')
    def get_balance(self):
        return self.balance
my_account = BankAccount(account_number="12345678", balance=1000)

# Deposit and withdraw
my_account.deposit(500)
my_account.withdraw(200)
print(my_account.get_balance())  # Output: 1300
print(my_account)




class Broker:
    stock_prices={'goog':400,'amzn':900,'tsla':567,'nifty':780}

    def __init__(self,name,balance,acc_no):
        self.name=name
        self.balance=balance
        self.acc_no=acc_no
        self.porfolio={}
    def __str__(self):
        return f"name is {self.name} and acc no is {self.acc_no}"

    def get_porfolio(self):
        return self.porfolio

    def get_balance(self):
        return self.balance
    
    def buy(self,stock_name):
        found=self.stock_prices.get(stock_name)
        if found:
            if self.balance>found:
                self.porfolio.update({stock_name:found})
                self.balance=self.balance-found
            else:
                print('you dont have enough money')
        else:
            print('incorrect stock name')
            


    def sell(self,stock_name):
        found=self.porfolio.get(stock_name)
        if found:
            self.porfolio.pop(stock_name)
            self.balance=self.balance-found
        

acc1=Broker('sanjay',3000,133)
acc2=Broker('santosh',2000,144)
print(acc1)
print(acc2)
print(acc1.get_porfolio())
acc1.buy('amzn')
print(acc1.get_porfolio())
acc1.buy('tsla')
print(acc1.get_porfolio())
acc1.sell('tsla')
print(acc1.get_porfolio())
acc1.name='sunil'
print(acc1.name)

print(acc1.get_balance())
print(Broker.get_balance(acc1))