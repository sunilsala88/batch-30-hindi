


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