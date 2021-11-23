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

print("====================")
#select emp_id from df
print(df['emp_id'])
print(type(df['emp_id']))
print(df.emp_id)

print("====================")
print(df[['emp_id']])
print(type(df[['emp_id']]))

print("====================")
print(df[['emp_id', 'salary']])

print("====================")

#Series -> emp_id = 11,22,33,44,55,66
df['emp_id'] = pd.Series([11,22,33,44,55,66])
df.emp_id = pd.Series([11,22,33,44,55,66])
print(df)

#numpy.array ->
df.emp_id = np.arange(1,6+1)
print(df)

print("====================DataFrame Transpose")
print(df.T)

