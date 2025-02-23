
#library/module/package

import time
import sys
import random
import os

print(os.getcwd())

def main():
    print('starting main fun')
    print('random number is',random.randint(100,200))
i=0
while True:
    main()
    time.sleep(1)
    print(i)
    i=i+1
    if i==5:
        sys.exit()


# import demo1
# print(demo1.sample1)
# print(demo1.get_value())

# c1=demo1.Circle(50)
# print(c1.area())



# import demo1 as d1
# print(d1.sample1)
# print(d1.get_value())


from demo1 import sample1,get_value

print(sample1)
print(get_value())

from demo1 import *
print(sample1)
print(get_value())



import demo1 as d1
import demo2 as d2
print(d1.sample1)
print(d2.sample1)
print(d1.get_value())

# import stocks.tsla as t1

# print(t1.current_price)

# import asdfjaskdjfklajwfidjlakdjflkajdfkjasdfjkladfjk as y1

# print(y1.stop_price)