#!/usr/bin/python

#prints the schema of a json file
# usage: json_schema.py jsonfilename

import sys
import json

filename = sys.argv[1]
data = []
i = 0
try:
    with open(filename) as fname:
        for line in fname:
            i=i+1
            if i%2 == 1: #skip every other line since it is empty
                data.append(json.loads(line))
except Exception:
    print "Error while reading file: ", filename
    print "Check if the file complies with JSON format"
    print "\nUsage: json_schema.py jsonfilename"
    sys.exit()

#inner dfs
def dfs_inner(x, indent):
    try:
        for key, value in x.iteritems():
            print indent + key
            try:
                dfs_inner(value, indent+"....")
            except Exception:
                pass
    except Exception:
        pass

#outer dfs
indent = " "
for key, value in data[0].iteritems():
    print key
    dfs_inner(value, indent+"....")
