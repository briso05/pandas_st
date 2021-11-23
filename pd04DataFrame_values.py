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

print(df.values)
print("====================")
print(df.values[0])

print("====================")
print(df.values[0:2])

print("====================")
print(df.values[[0,2]])

print("====================")
print(df.values[0,2])
print(df.values[1,2])

print("====================")
print(df[0:1])
print("====================")
print(df[0:3])
print("====================")
print(df[0:])
print("====================")
print(df[3:])
print("====================")
print(df[:3])

print("====================loc[[]] : to see nonsequenced data")
#print(df[[0,2]]) #ERROR

print(df.loc[[0,2]])
print(df.loc[[0,2,5]])

print("====================iloc[]")
print(df.iloc[2])

print("====================iloc[] :slice")
print("====================iloc[:2]")
print(df.iloc[:2])

print("====================iloc[2:3,2]")
print(df.iloc[2:3,2])

print("====================")
#emp_id, salaray
print(df.iloc[2:3, [0,2]])

print("====================head : see top 5 rows")
print(df.head())

print("====================head(3) : see top 3 rows")
print(df.head(3))

print("====================tail : see bottom 5 rows")
print(df.tail())

print("====================tail(3): see bottom 3 rows")
print(df.tail(3))

print("====================")
#emp_id, name, salay / bottom row 2
print(df[['emp_id','name','salary']].tail(2))
print(df.tail(2).iloc[:,0:3])
