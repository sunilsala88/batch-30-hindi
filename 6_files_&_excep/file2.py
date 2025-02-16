

# f1=open('something.txt','r')
# data=f1.read()
# print(data)

# f1.close()
# try:
#     n1=int(input('enter a number 1'))
#     n2=int(input('enter a number 2(zero is not allowed)'))
#     print(n1/n2)
# except Exception as e:
#     print('this is nor working')
#     print(e)
# print('this is important')


a=["10", "20", "hello", "40"]
ans=[]
i=0
while True:
    if i==len(a):
        break
    current_value=a[i]
    i=i+1 

    try:
        t=int(current_value)
        ans.append(t)
    except:
        print(current_value,'invalid string')
        ans.append(0)

print(ans)