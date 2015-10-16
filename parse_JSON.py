#!/usr/bin/python

import json

#read json
fr = open('spark-driver.json', 'r')
data = json.load(fr)

fr.close()

#write json
fw = open('spark-driver.json', 'w')
data['spec']['containers'][0]['name'] = 'spark'
print data
json.dump(data, fw)

fw.close()
