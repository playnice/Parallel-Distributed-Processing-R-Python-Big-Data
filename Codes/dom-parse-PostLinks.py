import time,psutil
import xml.etree.ElementTree as ET 

def domParse(handle):
	document = ET.parse(handle)
	root = document.getroot()
	return root

if __name__ == "__main__":
	row_parsed = set()
	start_time = time.time()
	start_mem = int(psutil.virtual_memory().available/(1024.0 ** 2))
	# DOM parse starts here
	with open("/home/xiang/Downloads/FYP1/datasets/stackoverflow/PostLinks.xml") as handle:
		for child in domParse(handle):
			Id = child.attrib.get("Id")
			row_parsed.add(Id)		
    # Print out the report.
	end_time = time.time()
	end_mem = int(psutil.virtual_memory().available/(1024.0 ** 2))
	print("Starting available memory: {} MB".format(start_mem))
	print("Final available memory: {} MB".format(end_mem))
	print("Number of Rows: {}".format(len(row_parsed)))
	print("Time taken: {} s".format(int((end_time - start_time))))
	print("Memory used: {} MB".format(abs(end_mem - start_mem)))
