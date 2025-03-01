

# import numpy
# l1=[33,44,55,6.3]
# print(l1)
# a1=numpy.array(l1)
# print(a1)



import numpy as np
l1=[33,44,55,6]
print(l1)
a1=np.array(l1)
print(a1)

print(l1+l1)
print(a1*a1)

# print(l1-3)
print(a1-3)

a2=np.array([[33,44,5],[66,77,88]])
a3=np.array([[33,44,5],[66,77,88],[99,0,88]])

print(list(range(10)))
print(np.arange(10,200,5))
# print(np.zeros(10))
# print(np.ones(10,dtype=int))

b1=np.arange(50,60)
print(b1[:3])

b2=np.array([[22,33],[55,66]])
print(b2)

b2=np.array([[22,33,44],[55,66,77],[88,99,11]])
print(b2)