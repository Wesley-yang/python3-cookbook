#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

from operator import itemgetter

from itertools import groupby

# 通过某个字段记录分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5412 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '5800 E 58TH', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(" ", i)

# 一个非常重要的准备步骤是要根据指定的字段将数据排序。
# 因为groupby()仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果，比如说：

for address, items in groupby(rows, key=itemgetter('address')):
    print(address)
    for i in items:
        print(" ", i)

# 地址为'5412 N CLARK'的没有分到一组
