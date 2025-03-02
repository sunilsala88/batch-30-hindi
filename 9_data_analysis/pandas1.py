#pip install pandas

import pandas as pd
import numpy as np


nd1=np.arange(25).reshape(5,5)
print(nd1)
df1=pd.DataFrame(nd1,index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])
print(df1)

import pandas as pd
df1=pd.read_csv(r'/Users/algo trading 2025/batch 30 hindi/9_data_analysis/sp500.csv')
print(df1)