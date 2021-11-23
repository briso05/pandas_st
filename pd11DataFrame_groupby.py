#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd

print('Hello python')

print(sys.argv[0])
print("====================")

# key1 key2 data1 data2
#0 a   one    1   randn
#1 a   two    2   randn
#2 b   one    3   randn
#3 b   two    4   randn
#4 a   one    5   randn

dict1 = {
        'key1': ['a','a','b','b','a'],
        'key2': ['one','two','one','two','one'],
        'data1': np.arange(1,5+1),
        'data2': np.random.randn(5)
        }
print(dict1)
df = pd.DataFrame(dict1)
print(df)

print("====================")
#groupby >> mean,max,min,sum,...
print(df.groupby(df['key1'])) #DataFrameGroupBy object
print("====================")
print(df.groupby(df['key1']).mean())
print("====================")
print(df.groupby(df['key2']).mean())
print("====================")
print(df[['data2']].groupby(df['key2']).mean())

print("====================")
print(df[['data2']].groupby([df['key1'],df['key2']]).mean())
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
print(df)

print("====================")
print(df[['salary']].groupby(df['dept_id']).mean())
