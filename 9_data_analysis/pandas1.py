#pip install pandas

import pandas as pd
import numpy as np


nd1=np.arange(25).reshape(5,5)
print(nd1)
df1=pd.DataFrame(nd1,index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])
print(df1)