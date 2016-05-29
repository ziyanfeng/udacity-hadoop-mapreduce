#!/usr/bin/python

import sys

last_id = None
last_hour = None
peak_hours = []
count = 0
max_count = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    this_id, this_hour = data

    if last_id and last_id != this_id:
        for h in peak_hour:
            print last_id, '\t', h

    elif this_id == last_id:
        last_id = this_id