#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd

print('Hello python')

print(sys.argv[0])
print("====================")
print(np.NaN, np.nan)
lst = [[3.14, np.NaN],[99, -22.5],[np.nan, np.nan],[100.5, -100]]
df = pd.DataFrame(lst, columns=['one','two'])
print(df)
print("====================")
# show NaN => True
print(df.isnull())
print("====================")
# show NaN => False
print(df.notnull())
print("====================")
#do not show rows which have NaN 
print(df.dropna())

print("====================")
#do not show rows which values are all NaN
print(df.dropna(how='all'))

print("====================")
print(df.fillna(88))

print("====================col cum : sum() nan >> 0")
print(df.sum())
print(df.sum(axis=0))
print("====================sum() nan >> nan")
# if colum has any NaN, it's sum will be NaN
print(df.sum(skipna=False))

print("====================row sum : sum(axis=1)")
print(df)

#sum values in same rows
print(df.sum(axis=1))

print("====================col mean")
print(df.mean())

print("====================row mean")
# NaN values are excluded while calculating mean
print(df.mean(axis=1))
print("====================")
# to show statistical values 
print(df.describe())
