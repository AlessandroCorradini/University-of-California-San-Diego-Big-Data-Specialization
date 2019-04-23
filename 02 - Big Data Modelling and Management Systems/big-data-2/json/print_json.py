#!/usr/bin/python

# usage: python print_json.py
 
import json
import sys

# initialize variables
filename = raw_input('Enter filename: ')
#filename = sys.argv[1]
data 	= []
i 	= 0
count 	= 0

# read tweet number: 2nd argument
whichTweet = raw_input('Which Tweet Number are you interested in ? ')
whichTweet = int(whichTweet)
#whichTweet = int(sys.argv[2])

# read the nested path: 3rd argument 
ipath = raw_input('Enter path (ex: user/id) : ')
path = ipath.split("/")
#path = str(sys.argv[3]).split("/")

# read file: 1st argument (format: 1 tweet per line)
try:
    with open(filename) as fname:
        for line in fname:
            if count > whichTweet:
            	break
            i=i+1
            if i%2 == 1: #skip every other line since it is empty
                data.append(json.loads(line))
                count=count+1
except Exception:
    print "Error while reading file: ", filename
    print "\nCheck if the file complies with JSON format"
    print "\nUsage: print_json.py jsonfilename"
    sys.exit()


# keep reading nested values for the path in data[X]
try:
	nextStep = 0
	obj = data[whichTweet-1]
	while nextStep < len(path):
		obj = obj[path[nextStep]]
		nextStep = nextStep + 1
	print obj
except Exception:
	print "Check your path	: ", ipath
	print "Problem at 	: ", path[nextStep]
