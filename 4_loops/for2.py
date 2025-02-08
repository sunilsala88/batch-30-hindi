# https://colab.research.google.com/drive/1TBfkK8yE_M6YNwkOwrP2TQUYOj2ayP00?usp=sharing

list1=[1,2,3,4,5,6]
#loop
#iteration

#type 1
# for t in list1:
#     print(t)

#type 2
# for i in range(100):
#     if i%2==0:
#         print(i)

#range function
# l=range(7,16,2)
# print(list(l))

# for i in range(0,100,2):
#     print(i)


l1=[44,55,6,777,8,67,543,88,434]
#type 3
# for i in range(len(l1)):
#     print(l1[i])


#print hello 10 time
for i in range(10):
    print('hello')
#get highest value in alist



high=l1[0]
for i in l1:
    if high<i:
        high=i
print(high)

a=max(l1)
print(a)


low=l1[0]
for i in range(len(l1)):
    if low>l1[i]:
        low=l1[i]
print(low)


p= [+10, -20, +15, +30, -5]
count=0
for i in p:
    if i<0:
        count=count+1

print(count)


prices=[100, 105, 110]
Volumes =[200, 150, 300]

pv=0
for i in range(len(prices)):
    p=prices[i]
    v=Volumes[i]
    print(p,v)
    t=p*v
    print(t)