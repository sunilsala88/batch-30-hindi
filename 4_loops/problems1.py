

#fibonacii number
#0,1,1,2,3,5,8,13,21,34

fib_num=20
fib_list=[0,1]
num1=fib_list[0]
num2=fib_list[1]

for i in range(fib_num-2):
    num3=num1+num2
    fib_list.append(num3)
    num1=num2
    num2=num3
print(fib_list)


fib_list=[0,1]
num1=fib_list[0]
num2=fib_list[1]
count=0
while True:
    if count==(fib_num-2):
        break
    num3=num1+num2
    fib_list.append(num3)
    num1=num2
    num2=num3
    count=count+1
print(fib_list)




numbers=20
total=0
for i in range(1,numbers+1):
    total=total+i
print(total)


total=0
i=0
while True:
    if i==numbers:
        break
    i=i+1
    total=total+i
print(total)



word1='fessorpro'
ans=""
rev_list=list(range(-1,-(len(word1)+1),-1))

range(-1,-10,-1)

print(rev_list)
for i in rev_list:
    ans=ans+word1[i]
print(ans)


word1='fessorpro'
i=-1
ans=""
while True:
    if i==-len(word1)-1:
        break
    ans=ans+word1[i]
    i=i-1
print(ans)



numbers=[3, 1000, 45, 44, 1, 5, 9]
numbers.sort()
print(numbers)
largest=numbers[0]
largest2=numbers[0]
i=0
while True:
    if i==len(numbers):
        break
    current_num=numbers[i]

    if largest<current_num:
        largest2=largest
        largest=current_num
    i=i+1

print(largest)
print(largest2)