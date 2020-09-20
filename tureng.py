# -*- coding:utf-8 -*-
import sys
import pandas as pd
from tabulate import tabulate
from ftfy import fix_encoding
u = "https://tureng.com/en/turkish-english/"
rl = sys.argv
rl = rl[1]
url = u + rl
print(url)
# page = pd.read_html(url, index_col=0, encoding='utf-8')
page = pd.read_html(url, encoding='utf-8')
# print(page[1]['Category'])
# print(page[1]['English'])
# table = table.drop(table.columns[3], axis=1)

t1 = page[0]
t1 = t1[['Category','Turkish','English']]
t1 = t1.dropna(subset = ['Turkish'])

# t2 = page[1]
# t2 = t2[['Turkish','English']]
# t2 = t2.dropna(subset = ['Turkish'])

t1 = t1.values.tolist()
# t2 = t2.values.tolist()

headers = ['Category', 'Turkish', 'English']
print(tabulate(t1[:5], headers, tablefmt="grid"))
# print(tabulate(t2[:3], tablefmt="grid"))
