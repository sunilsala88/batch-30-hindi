
#library/module/package

# import time

# def main():
#     print('starting main fun')

# while True:
#     main()
#     time.sleep(2)


import demo1
print(demo1.sample1)
print(demo1.get_value())

c1=demo1.Circle(50)
print(c1.area())



import demo1 as d1
print(d1.sample1)
print(d1.get_value())


import stocks.tsla as t1

print(t1.current_price)

import asdfjaskdjfklajwfidjlakdjflkajdfkjasdfjkladfjk as y1

print(y1.stop_price)