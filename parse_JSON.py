#!/usr/bin/python

import json

f = file('temp.json')
s = json.load(f)

# print s
# print s['name']

for i in s:
	print "%s: %s" % (i, s[i])

f.close()
