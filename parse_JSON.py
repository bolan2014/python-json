#!/usr/bin/python

import json

fr = open('spark-driver.json', 'r')
data = json.load(fr)

# print s
print data['kind']
for i in data:
    print "%s: %s" % (i, data[i])

fr.close()
