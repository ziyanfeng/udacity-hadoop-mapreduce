#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data
# output will be in the format:
# "id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at"  "score"  "reputation"
# "gold"  "silver"  "bronze"

import sys
from collections import defaultdict


def reducer():
    users = {}
    nodes = defaultdict(list)
    for line in sys.stdin:
        # YOUR CODE HERE
        data = line.strip().split('\t')
        marker = data[1]
        key = data[0]

        if marker == 'A':
            users[key] = data[2:]

        elif marker == 'B':
            nodes[key].append(data[2:])

    for key in nodes:
        reputation, gold, silver, bronze = users[key]
        for item in nodes[key]:
            id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score = item
            print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}'.\
                format(id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score, reputation,
                       gold, silver, bronze)


reducer()