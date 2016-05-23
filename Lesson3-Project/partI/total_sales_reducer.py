#!/usr/bin/python

import sys

salesTotal = 0
number_of_sales = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store or item name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    salesTotal += float(data_mapped[1])
    number_of_sales += 1

print number_of_sales,"\t", salesTotal

