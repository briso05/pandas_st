#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd
import sqlite3 

print('Hello python')

print(sys.argv[0])
print("====================")

sql = '''
create table if not exists test(
product varchar2(20),
maker varchar2(20),
weight real,
price integer
)
'''

conn = sqlite3.connect('pd15test.db')
conn.execute(sql)
#conn.commit()

def dumyInsert():
    for i in range(10):
        data = ('mouse'+str(i), 'sm'+str(i), 10.5+i, 5000+i)
        insert_sql = 'insert into test(product,maker,weight,price) values(?,?,?,?)'
        conn.execute(insert_sql, data)
        conn.commit()
#dumyInsert()
print("========insert succeed=======")

print("========selectAll=======")


def selectAll():
    selectAll_sql = 'select * from test'
    cursor = conn.execute(selectAll_sql)
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=['product','maker','weight','price'])
    print(df)

selectAll()
