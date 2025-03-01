
import numpy as np
b2=np.array([[22,33,44],[55,66,77],[88,99,11]])
# print(b2)
# print(b2[1,2])
# print(b2[ 2,[1,2] ])
# print(b2[ [1,2],1 ])

# print(b2[1:3,1:3])
# print(b2[1:,1:])

# print(b2[0:2,1:3])
# print(b2[:2,1:])

nd1=np.arange(25).reshape(5,5)
print(nd1)

print(nd1[3,1])
print(nd1[ 2 , [2,3] ])
print(nd1[ 2 , 2:4 ])


print(nd1[ 1:4 , 1:4 ])
print(nd1[[0,1,2,3,4],[0,1,2,3,4]])

nd2=np.random.randint(100,200,25).reshape(5,5)
print(nd2)