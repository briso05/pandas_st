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
print(df)

print("====================")
print(df.drop(df.index[0])) # It doesn't affect real data
#print(df.drop(df.index[0], inplace=True)) # It affect real data
print(df)

print("====================")
# drop using slicing
print(df.drop(df.index[:3]))

print("====================")
# drop using indexing
print(df.drop(df.index[[1,3]]))

print("====================")
# drop column
print(df.drop(['location'], axis=1))
