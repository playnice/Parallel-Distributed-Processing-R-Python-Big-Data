#! /usr/bin/env python

## MODIFIED BY WRY FROM REFERENCE
## https://www.tutorialspoint.com/python/python_xml_processing.htm
## Python Object Oriented Programming

## This is pure SAX processing.
import xml.sax
import datetime
import time
import argparse

argsParser = argparse.ArgumentParser()                                               
argsParser.add_argument("--file", "-f", type=str, required=True)
args = argsParser.parse_args()

global_Row_Count = 0

# =========================================================
class UsersHandler( xml.sax.ContentHandler ):
	def __init__(self):
		self.Row_Count = 0

	# ======================================================
	# Call when an element starts, that is the start <tag>.
	# In our Users.xml case, the start <tag> is the <row> tag.
	# We do not have any internal <tag>s inside our <row> tag.
	# We only have attributes between our start <row> and end </row> tag.
	# The attributes are the "dictionary type", that is, "key-value" pairs.
	# ======================================================
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "row":
			self.Row_Count = self.Row_Count + 1
			pass
       

		# UPDATE AND PRINT ROW COUNT 
		# print

		millionthCount = (self.Row_Count % 1000000)

		if (millionthCount == 0):
			print "ROW NUMBER PROCESSED:\t", self.Row_Count
			print "Now time at:", datetime.datetime.now(), "at %s " %(time.time() - globalStartTime), "\n"

		global_Row_Count = self.Row_Count

	# ======================================================
	# Call when an elements ends i.e. start <tag> until end </tag>
	# Attributes-Value pairs are inside the tag itself, normally the start <tag>
	# ======================================================
	def endElement(self, tag):

		# RESET THE ELEMENT
		self.CurrentData = ""

	# ======================================================
	# Call when a character is read
	# The content is the "value" of the element, i.e. what is
	# written between the start <tag> and end </tag>
	# In our Users.xml case, contents between <row> and </row>.  
	# ======================================================
	def characters(self, content):
		pass

if ( __name__ == "__main__"):

	globalStartTime = time.time() 
	print "PARSING", args.file 
	print "\nPROGRAM STARTING:", datetime.datetime.now(), "at %s " %(time.time() - globalStartTime), "\n"

	# create an XMLReader
	parser = xml.sax.make_parser()

	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)

	# override the default ContextHandler
	Handler = UsersHandler()
	parser.setContentHandler(Handler)
   
	# parse file path provided by user input
	parser.parse(args.file)
	
	try:
		print "\nNUMBER OF ROWS PARSED: ", Handler.Row_Count, "\n"
	except:
		pass   

	print "\nPROGRAM FINISHED:", datetime.datetime.now(), "at %s " %(time.time() - globalStartTime), "\n"
