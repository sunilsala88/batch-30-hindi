


def fun1(a,b):
    c=a+b
    return c


def fun2(r,q):
    d=fun1(r,q)
    print(d)

fun2(5,10)


def order(price=0):
    if price==0:
        print('market')
    else:
        print(f'limit order with price {price}')

order(100)

#default argument
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


# Driver code (We call myFun() with only
# argument)
myFun(10,20)


#positional arg
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


# You will get correct output because 
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")


#keyword argument
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')



def do_somethig():
    pass

do_somethig()


# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = 'I love GeeksforGeeks'
    
    def f2():
        print(s)
        
    f2()

# Driver's code
f1()



def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))


def myFun(x):

    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

x = 10
def myFun():
    global x
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20


# Driver Code (Note that x is not modified
# after function call.
print(x)
myFun()
print(x)
