#!/usr/bin/python

import sys

last_page = None
occurrence = 0
most_popular = None
highest_occurrence = 0

for line in sys.stdin:
    this_page = line.strip()
    if last_page and last_page != this_page:
        occurrence = 0
    
    last_page = this_page
    occurrence += 1
    
    if occurrence > highest_occurrence:
        highest_occurrence = occurrence
        most_popular = this_page

if last_page is not None:
    if occurrence > highest_occurrence:
        highest_occurrence = occurrence
        most_popular = last_page

print most_popular, '\t', highest_occurrence
