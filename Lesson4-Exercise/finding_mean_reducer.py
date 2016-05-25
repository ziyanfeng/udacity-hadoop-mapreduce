#!/usr/bin/python

import sys

last_day = None
total_sales = 0
day_count = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    this_day = data[0]
    sale = data[1]

    if last_day and last_day != this_day:
        average_sale = float(total_sales) / float(day_count)
        print last_day, '\t', average_sale
        last_day = this_day
        total_sales = 0
        day_count = 0

    last_day = this_day
    total_sales += float(sale)
    day_count += 1

if last_day is not None:
    average_sale = float(total_sales) / float(day_count)
    print last_day, '\t', average_sale


# # Another Method
# from collections import defaultdict
#
# weekday_sales = defaultdict(list)
#
# for line in sys.stdin:
#     data = line.strip().split('\t')
#     if len(data) != 2:
#         continue
#     weekday = data[0]
#     sale = data[1]
#     weekday_sales[weekday].append(sale)
#
# for weekday in weekday_sales:
#     total_sales = weekday_sales[weekday]
#     average_sale = sum([float(i) for i in total_sales]) / len(total_sales)
#     print '{0}\t{1}'.format(weekday, average_sale)