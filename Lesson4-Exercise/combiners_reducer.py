#!/usr/bin/python

import sys
from collections import defaultdict

weekday_sales = defaultdict(float)

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    weekday = data[0]  # day of the week
    sale = data[1]  # single day sale
    weekday_sales[weekday] += float(sale)  # cumulating total sales on specific day of the week

for weekday in weekday_sales:
    print '{0}\t{1}'.format(weekday, weekday_sales[weekday])
