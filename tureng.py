# -*- coding:utf-8 -*-
import sys
import pandas as pd
import tabulate
from ftfy import fix_encoding
u = "https://tureng.com/tr/turkce-ingilizce/"
rl = sys.argv
rl = rl[1]
url = u + rl
# page = pd.read_html(url, index_col=0, encoding='utf-8')
page = pd.read_html(url, encoding='utf-8')

table = page[0]
# table = table.drop(table.columns[3], axis=1)

print(table)