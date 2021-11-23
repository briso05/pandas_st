#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd

print('Hello python')

print(sys.argv[0])
print("====================")

col01 = pd.Series([11,22,33,44])
print(col01)
col02 = pd.Series([55,66,77,88,99])
print(col02)

print(col01 + col01)

print("====================")
sum_col = col01 + col02 # if the number of rows that two Series have are not same, it end up making NaN
print(sum_col)

print("====================dropna()")
print(sum_col.dropna())

print("====================fillna(value)")
print(sum_col.fillna(0))
print("====================add(),sub(),mul(),div()")

sum_col = col01.add(col02, fill_value=0) #when adding two columns, no data row will be fill with 0. => added col's data = 0[col1] + col2's data
print(sum_col)

print("====================")
df01 = pd.DataFrame(np.arange(11,19+1).reshape(3,3), columns=['num','price','each'])
print(df01)

print("====================")
df02 = pd.DataFrame(np.arange(11,22+1).reshape(4,3), columns=['num','price','each'])
print(df02)
print("====================add,sub,mul,div")
sum_df = df01.add(df02,fill_value=0)
print(sum_df)
print("====================")
mul_df = df01.mul(df02,fill_value=1)
print(mul_df)
