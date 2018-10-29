#File: xml-to-json-mongodb.py
#Date: Fri Aug 11 14:07:24
#Envn: Linux Xiang 4.10.0-33-generic #37~16.04.1-Ubuntu SMP  UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

import json  
import xmltodict  
import sys
import argparse
from pymongo import MongoClient

#Set argument for file to be converted and upload to MongoDB
parser = argparse.ArgumentParser(description='Convert an XML file to JSON.')
parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'),
                    default=sys.stdin)

#parsing XML file into dictionary and then convert into JSON
def xmltojson(xmlstr):  
	xmlparse = xmltodict.parse(xmlstr,attr_prefix='')  
	jsonstr = json.dumps(xmlparse,indent=1) 
	jsonstr = json.loads(jsonstr)
	print(jsonstr)
	return(jsonstr)

if __name__ == "__main__": 
	args = parser.parse_args()

	#Connect to MongoDB
	client = MongoClient('localhost', 27017)
    
	#Switch db to 'fyp'
	db = client.fyp

	#Use collection 'tester'
	tester = db.tester

	#pass in XML to convert into JSON
	json_data = xmltojson(args.infile)

	#insert converted JSON file into collection
	result = tester.insert(json_data)
	    
	#close connection
	client.close()

