#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)
for line in reader:
    if len(line) == 19:  # check if the input is ok
        node_id = line[0]  # id is the 1st column
        body = line[4]  # body is the 4th column
        body_words = re.findall(r"[a-zA-Z]+", body)  #  '[a-zA-Z]+' means "a word character (a-z A-Z etc.) repeated one or more times"
        body_words = [word.lower() for word in body_words]
        for word in body_words:
            print "{0}\t{1}".format(word, node_id)
