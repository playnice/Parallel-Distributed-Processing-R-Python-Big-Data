#File: xml_accounting.py
#Date: Fri Aug 11 14:07:24
#Envn: Linux Xiang 4.10.0-33-generic #37~16.04.1-Ubuntu SMP  UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

from lxml import etree
	
if __name__ == "__main__":  	

	filename = "/home/xiang/Downloads/FYP/datasets/datascience/Votes.xml"
	
	#initialize attribute counter
	one_cat = two_cat = three_cat = four_cat = five_cat = count  = 0
	
	context = etree.iterparse(filename)
	#Check how many rows have how many attributes
	for event, element in context:
		if element.tag == 'row':
			if 'Id' in element.attrib:
				count += 1
			if 'PostId' in element.attrib:
				count += 1
			if 'VoteTypeId' in element.attrib:
				count += 1
			if 'UserId' in element.attrib:
				count += 1
			if 'CreationDate' in element.attrib:
				count += 1
				
			if count == 1:
				one_cat += 1
			elif count == 2:
				two_cat += 1
			elif count == 3:
				three_cat += 1
			elif count == 4:
				four_cat += 1
			elif count == 5:
				five_cat += 1
			
			count = 0
			element.clear() 

	#get total rows in file
	num_lines = sum(1 for line in open ("/home/xiang/Downloads/FYP/datasets/datascience/Votes.xml")) - 3

	print('Checking the file......')
	print('Total rows in file : %d' % num_lines)
	print('Rows with 1 attribute: %d' % one_cat)
	print('Rows with 2 attribute: %d' % two_cat)
	print('Rows with 3 attribute: %d' % three_cat)
	print('Rows with 4 attribute: %d' % four_cat)
	print('Rows with 5 attribute: %d' % five_cat)
