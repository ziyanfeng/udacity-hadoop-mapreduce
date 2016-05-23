#!/usr/bin/python

import sys

number_of_visit = 0

for line in sys.stdin:
    if line.strip() == '/assets/js/the-associates.js':
        number_of_visit += 1

print number_of_visit