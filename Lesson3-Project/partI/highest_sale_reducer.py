#!/usr/bin/python

import sys

oldSale = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the highest individual sale thusfar

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", oldSale
        oldKey = thisKey
        oldSale = 0

    oldKey = thisKey
    if float(thisSale) > float(oldSale):
        oldSale = thisSale

if oldKey is not None:
    print oldKey, "\t", oldSale