#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
print('Hello python')

print(sys.argv[0])
print("====================")

emp = {
        'emp_id':[100,101,200,201,300,400],
        'name':('kim','lee','choi','han','gang','yoon'),
        'salary':[8000000,7000000,7500000,5000000,4000000,6000000],
        'dept_id':[1,1,2,2,3,4],
        'location':['seoul','seoul','busan','busan','degu','incheon']
    }
print(emp)
print("====================")
df = pd.DataFrame(emp)
#select * from df
print(df)

print("====================to_csv(filename, sep=',')")
df.to_csv('pd12save.csv',sep=',',index=False)

#save only data
#df.to_csv('pd12save.csv',sep=',',index=False,header=False)

#seperate data using by tab
#df.to_csv('pd12save.csv',sep='\t',index=False,header=False)
print("====================read_csv()")
print(pd.read_csv('pd12save.csv'))

