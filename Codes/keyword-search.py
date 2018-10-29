#!/usr/bin/env python

import xml.sax
import datetime
import time
import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

unix_timestamp = time.time()
start_local_time = datetime.datetime.utcfromtimestamp(unix_timestamp)
start_file_datetime = start_local_time.strftime("%Y-%m-%d-UTC:%H:%M:%S")

file_datetime = start_local_time.strftime("%Y%m%d-UTC%H%M%S")
file_name = "search-results" + file_datetime + ".txt"

f = open(file_name, 'w+')

global_Row_Count = 0
globalPostsFound = 0

# =========================================================
class UsersHandler( xml.sax.ContentHandler ):
	def __init__(self):
		self.Row_Count = 0
		self.CurrentData = ""

		self.Id = ""
		self.CreationDate = ""
		self.ViewCount = ""
		self.Body = ""
		self.Title = ""
		self.CommentCount = ""
		self.OwnerDisplayName = ""
		self.LastEditorDisplayName = ""

		self.word = ""
		self.keywordCount = 0
		self.postsFound = 0

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
			self.Body = attributes["Body"]
			for i in self.word:
				if i in self.Body.lower():
					self.keywordCount += 1					
			
			if self.keywordCount == len(self.word):
				self.postsFound += 1
				print "==========================================================="
				f.write("==========================================================="+ "\n")
				try:
					self.Id = attributes["Id"]
					print "Id:\t\t\t", self.Id
					f.write("Id:\t\t\t" + self.Id + "\n" )
				except:
					print "Id:\t\t\tNA"
					f.write("Id:\t\t\tNA\n")					
						
				try:
					self.ViewCount = attributes["ViewCount"]
					print "ViewCount:\t\t", self.ViewCount
					f.write("ViewCount:\t\t" + self.ViewCount + "\n" )
				except:
					print "ViewCount:\t\tNA"
					f.write("ViewCount:\t\tNA\n")

				try:
					self.CommentCount = attributes["CommentCount"]
					print "CommentCount:\t\t", self.CommentCount
					f.write("CommentCount:\t\t" + self.CommentCount + "\n" )
				except:
					print "CommentCount:\t\tNA"
					f.write("CommentCount:\t\tNA\n")
				try:
					self.CreationDate = attributes["CreationDate"]
					print "CreationDate:\t\t", self.CreationDate
					f.write("CreationDate:\t\t" + self.CreationDate + "\n" )
				except:
					print "CreationDate:\t\tNA"
					f.write("CreationDate:\t\tNA\n")
						
				try:
					self.OwnerDisplayName = attributes["OwnerDisplayName"]
					print "OwnerDisplayName:\t", self.OwnerDisplayName
					f.write("OwnerDisplayName:\t" + self.OwnerDisplayName + "\n" )
				except:
					print "OwnerDisplayName:\tNA"	
					f.write("OwnerDisplayName:\tNA\n")	
						
				try:
					self.LastEditorDisplayName = attributes["LastEditorDisplayName"]
					print "LastEditorDisplayName:\t", self.LastEditorDisplayName
					f.write("LastEditorDisplayName:\t" + self.LastEditorDisplayName + "\n" )
				except:
					print "LastEditorDisplayName:\tNA"
					f.write("LastEditorDisplayName:\tNA\n")	
						
				try:
					self.Title = attributes["Title"]
					print "Title:\t\t\t", self.Title
					f.write("Title:\t\t\t" + self.Title + "\n" )
				except:
					print "Title:\t\t\tNA"
					f.write("Title:\t\t\tNA\n")	
				try:
					self.Body = attributes["Body"]
					print "Body:\t\t\t", self.Body
					f.write("Body:\t\t\t" + self.Body + "\n" )
				except:
					print "Body:\t\t\tNA"
					f.write("Body:\t\t\tNA\n")

			self.keywordCount = 0


		# UPDATE AND PRINT ROW COUNT 
		# print

		millionthCount = (self.Row_Count % 1000000)
		

		try:
			if (millionthCount == 0) and (self.Row_Count != 0):
				print "ROW NUMBER PROCESSED:\t", self.Row_Count
				f.write("ROW NUMBER PROCESSED:\t" + str(self.Row_Count) + "\n" )
				print "Now time at:", datetime.datetime.now(), "at %s " %(time.time() - globalStartTime), "\n"
				f.write("Now time at:"+ str(datetime.datetime.now())+ "at " +str(time.time() - globalStartTime)+ "\n")
				#f.close()
				#f = open("search1000000.txt", 'w+',0)
		except: 
			pass

		global_Row_Count = self.Row_Count
		globalPostsFound = self.postsFound
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
	print "Parsing Posts.xml...\n"
	print "PROGRAM STARTING:", datetime.datetime.now(), "at %s " %(time.time() - globalStartTime), "\n"

	# create an XMLReader
	parser = xml.sax.make_parser()

	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)

	# override the default ContextHandler
	Handler = UsersHandler()
	parser.setContentHandler(Handler)
	
	# ask users to enter search keyword
	keyword = raw_input("Please enter search keyword: ")
	keyword = keyword.lower()

	# use stopwords to filter sentence to improve searchability
	stop = set(stopwords.words('english'))
	tokenizedKeyword = word_tokenize(keyword)
	tokenizedKeyword = [i for i in tokenizedKeyword if i not in stop] 
	print "\nSearching for keywords: ", tokenizedKeyword
	Handler.word = tokenizedKeyword
	try:
		#parser.parse("test.xml")
		parser.parse("/home/xiang/Downloads/FYP1/datasets/stackoverflow/Posts.xml")
	except:
		pass 

	try:
		print "\nNumber of rows parsed: ", Handler.Row_Count, "\n"
	except:
		pass   

	print "\nNumber of results: ", Handler.postsFound,"\n"
	print "\nPROGRAM FINISHED:", datetime.datetime.now(), "at %s " %(time.time() - globalStartTime), "\n"
	f.close()
