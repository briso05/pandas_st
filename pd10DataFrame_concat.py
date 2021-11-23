#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd

print('Hello python')

print(sys.argv[0])
print("====================")

dict01 = {
        'data1':range(100,107),
        'key':['b','b','a','c','a','a','b']
        }
dict02 = {
        'data2':range(100,103),
        'key':['a','b','d']
        }
dict03 = {
        'data3':range(10,13),
        'key3':['x','y','z']
        }
df1 = pd.DataFrame(dict01)
print(df1)
print("====================")
df2 = pd.DataFrame(dict02)
print(df2)
print("====================")
df3 = pd.DataFrame(dict03)
print(df3)
print("====================")

print(np.concatenate([df1,df2]))
print("====================")
print(np.concatenate([df2,df3]))
print("====================")
print(np.concatenate([df2,df3], axis=1))
print("======join : inner,outer,left,right===")
print(pd.merge(df1, df2))
print(pd.merge(df1, df2,how='outer'))
print(pd.merge(df1, df2,how='left'))
print(pd.merge(df1, df2,how='right'))


print("====================")
emp = {
        'emp_id':[100,101,200,201,300,400],
        'name':('kim','lee','choi','han','gang','yoon'),
        'salary':[8000000,7000000,7500000,5000000,4000000,6000000],
        'dept_id':[1,1,2,2,3,4],
        'location':['seoul','seoul','busan','busan','degu','incheon']
    }
print(emp)

dept = {
        'dept_id':[1,2,3,4,5,6],
        'dept_name':['web','game','temp1','temp2','temp3','temp4']
        }
print(dept)

print("====================")
df_emp = pd.DataFrame(emp)
print(df_emp)

print("====================")
df_dept = pd.DataFrame(dept)
print(df_dept)
print("====================")
#inner join -> show dept_id, emp_id, salary, dept_name
print(pd.merge(df_emp, df_dept)[['dept_id', 'emp_id','salary','dept_name']])
