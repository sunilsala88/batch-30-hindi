#https://www.geeksforgeeks.org/python-functions/



prices=[11,22,33,44]
# total=0
# for i in prices:
#     total=total+i
# avg=total/len(prices)
# print(avg)

#function defination
def average(numbers:list) -> int:

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