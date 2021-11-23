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

print("====================index sort")
#default :index sort(asc)

print(df.sort_index())

print("====================")
# index sort(row sort) : desc
print(df.sort_index(ascending=False))

print("====================column sort")
# column sort : desc --> axis=1
print(df.sort_index(axis=1,ascending=False))

print("====================")
# column sort : asc --> axis=1
print(df.sort_index(axis=1))

print("====================value sort: order by ")
#vlaue sort :order by salary asc
print(df.sort_values(by='salary'))

print("====================")
#order by salart desc
print(df.sort_values(by='salary', ascending=False))

print("====================rank()")
print(df.rank(ascending=False))

print("====================")
# rank columns which contain number
print(df.rank(axis=1,ascending=False))

print("====================")
#dept_id,count : Series > value_counts()
print(df.dept_id.value_counts())

# #of employees in each location
print(df.location.value_counts())
