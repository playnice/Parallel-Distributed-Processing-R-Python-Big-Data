#File: votetypeid-serial.py
#Date: Fri Aug 11 14:07:24
#Envn: Linux Xiang 4.10.0-33-generic #37~16.04.1-Ubuntu SMP  UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

from lxml import etree
import multiprocessing
from multiprocessing import Pool
from itertools import chain
import time

def sax_parse(filename, voteTypeId):
		
	context = etree.iterparse(filename, tag = 'row')
	for event, element in context:
		row_vote_type_id = element.attrib.get('VoteTypeId')
	
		#increment the counter on the matched VoteTypeId
		for i in range(len(voteTypeId)):
			if row_vote_type_id == str(i+1):
				voteTypeId[i] += 1
		element.clear() 
		element.getparent().remove(element)

	return voteTypeId
	
if __name__ == "__main__":  
	
	

	#files to be parsed
	file_list = ["/home/xiang/Downloads/FYP/datasets/stackoverflow/Votes.xml",
		     "/home/xiang/Downloads/FYP/datasets/stackoverflow/Votes.xml",
	 	     "/home/xiang/Downloads/FYP/datasets/stackoverflow/Votes.xml",
	 	     "/home/xiang/Downloads/FYP/datasets/stackoverflow/Votes.xml"]

	voteTypeId = [0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	#setup cores
	no_cores = multiprocessing.cpu_count()
	pool = Pool(no_cores)
	
	#Set start time for parsing
	start = time.time() 

	#parallel parse
	results = pool.starmap(sax_parse, [(file_list[0],voteTypeId),
					   (file_list[1],voteTypeId),
					   (file_list[2],voteTypeId),
					   (file_list[3],voteTypeId)])

	voteTypeId = [sum(x) for x in zip(*results)]
		
	end = time.time() #Set end time for parsing
	exec_time = end - start
	
	
	num_lines_se = sum(1 for line in open (file_list[0])) - 3

	print('************************\n'+
	      '* Number of VoteTypeId *\n' +
              '************************')
	print('AcceptedByOriginator: %d' % voteTypeId[0]) 
	print('UpMod: %d' % voteTypeId[1]) 
	print('DownMod: %d' % voteTypeId[2]) 
	print('Offensive: %d' % voteTypeId[3]) 
	print('Favorite: %d' % voteTypeId[4]) 
	print('Close: %d' % voteTypeId[5]) 
	print('Reopen: %d' % voteTypeId[6]) 
	print('BountyStart: %d' % voteTypeId[7]) 
	print('BountyClose: %d' % voteTypeId[8]) 
	print('Deletion: %d' % voteTypeId[9]) 
	print('Undeletion: %d' % voteTypeId[10]) 
	print('Spam: %d' % voteTypeId[11]) 
	print('InformModerator: %d' % voteTypeId[12]) 	
	print('No lines in Votes.xml : %d' % num_lines_se)
	print('Total lines parsed : %d' % (num_lines_se * len(file_list)))
	print('Execution time: %fs' % (exec_time))

