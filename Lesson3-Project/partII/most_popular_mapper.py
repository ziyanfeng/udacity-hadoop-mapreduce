#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        page = data[6]
        if page.find('http://www.the-associates.co.uk') == -1:
            print page
        else:
            page = page[len('http://www.the-associates.co.uk'):]
            print page
