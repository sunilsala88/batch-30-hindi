#https://www.geeksforgeeks.org/python-functions/



prices=[11,22,33,44]
# total=0
# for i in prices:
#     total=total+i
# avg=total/len(prices)
# print(avg)

#function defination
def average(numbers:list) -> int:
    #doc string
    """
    this function calculates average of given list and return avg value
    """

    total=0
    for i in numbers:
        total=total+i
    avg=total/len(numbers)

    return avg

a=average(prices)
print(a)

customers=[5,6,7,3]
b=average(customers)
print(b)


def add_numbers(num1:int,num2:int)->int:
    s=num1+num2
    return s

v=add_numbers(10,20)
print(v)


def fibonaccci(fib_num:int)->list:
    """
    this will take number as parameter and return fibonnaci numbers
    """
    fib_list=[0,1]
    num1=fib_list[0]
    num2=fib_list[1]

    for i in range(fib_num-2):
        num3=num1+num2
        fib_list.append(num3)
        num1=num2
        num2=num3

    return fib_list

f1=fibonaccci(10)
print(f1)
f2=fibonaccci(20)
print(f2)


def reverse_string(word1:str)->str:
    """
    this will reverse a string
    """
    ans=""
    rev_list=list(range(-1,-(len(word1)+1),-1))

    range(-1,-10,-1)

    # print(rev_list)
    for i in rev_list:
        ans=ans+word1[i]
    return ans

r1=reverse_string('hello')
print(r1)
r2=reverse_string('fessorpro')
print(r2)

'tsla'.replace()