# -*- coding:utf-8 -*-
import sys
import pandas as pd
import tabulate
from ftfy import fix_encoding
u = "https://tureng.com/en/turkish-english/"
rl = sys.argv
rl = rl[1]
url = u + rl
# page = pd.read_html(url, index_col=0, encoding='utf-8')
page = pd.read_html(url, encoding='utf-8')
print(len(page))
# print(page[1]['Category'])
# print(page[1]['English'])
# table = table.drop(table.columns[3], axis=1)

df = page[0]
df = df[['Category','Turkish','English']]
df = df.dropna(subset = ['Turkish'])
print(df)