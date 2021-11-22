#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd

print('Hello python')

print(sys.argv[0])
print("====================")


#print(dir(pd)) #show methods in pandas module

col = pd.Series([11,22,33,11,22,33])
print(col)
print(type(col))
print(col.index)
print(len(col))

print(col.values, type(col.values))
print(col.value_counts())

print(col.describe())

print("====================")

col = pd.Series(['a', 'b', 'c', 'a', 'b', 'c', 'd'])
print(col.describe())
print("====================")

ndarray = np.array([11,22,33])
for item in ndarray:
    print(item)

for item in col:
    print(item)
print("====================")
col = pd.Series([11,22,33,11,22,33,44])
print(col)
print(col.values)
print(col + 10)
print(col - 10)
print(col + col)

print("====================")
col_str = pd.Series(['aa', 'bb', 'cc'])
print(col_str)
print(col_str + " kim")

print(col_str[0])
col_str[0] = col_str[0].upper()
print(col_str[0])


print("====================")
print(col)
print(col[2])

col[2] = 100
print(col[2])

print(col[[3,6]])
print(col[[3,6]].values)

col[[3,6]] = [88,99]
print(col)

col[[3,6]] = col[[2,5]]
print(col)
print("====================")

print(col[1:4])
print(col[1:4].values)

print("====================")
print(col)
print(col >= 33)
print(col[col >= 33])

print("====================")
print(col)

col = pd.Series([11,22,33,11,22,33],index=['a', 'b', 'c', 'd', 'e', 'f'])
print(col)
print(col.index)
print(col['a'])
print(col[['a','d']])
print(col['a':'d'])

print("sum:",col.sum())
print("mean:",col.mean())
print("std:", col.std())

print("====================")
phones = ['010-xxxx-xxxx', '02-aaa-aaaa', '010-bbbb-bbbb', '02-ccc-cccc', '010-bbbb-bbbb', '031-ccc-cccc']

col = pd.Series(phones)
print(col)
print(col.value_counts())

lst = []
for item in col:
    lst.append(item.split("-")[0])
print(lst)

print(pd.Series(lst))
print(pd.Series(lst).value_counts())


print("====================")
print(pd.Series(number.split("-")[0] for number in phones))

print(pd.Series(number.split("-")[0] for number in phones).value_counts())

print("====================")
col = pd.Series(['kim', 'lee','yang'], index=[1,3,4])
print(col)

#reindex
print(col.reindex(range(6), fill_value='other'))
print(col.reindex(range(6), method='ffill'))
print(col.reindex(range(6), method='bfill'))
