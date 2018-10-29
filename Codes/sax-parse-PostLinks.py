import time,psutil,xml.sax 

class UsersHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.Row_Count = 0
	def startElement(self, tag, attributes):
		if tag == "row":
			self.Row_Count = self.Row_Count + 1

if __name__ == "__main__":
	start_time = time.time()
	start_mem = int(psutil.virtual_memory().available/(1024.0 ** 2))
	# Initiate SAX API
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	Handler = UsersHandler()
	parser.setContentHandler(Handler)		
	parser.parse("/home/xiang/Downloads/FYP1/datasets/stackoverflow/PostLinks.xml")
	# Print out the report.
	end_time = time.time()
	end_mem = int(psutil.virtual_memory().available/(1024.0 ** 2))
	print("Starting available memory: {} MB".format(start_mem))
	print("Final available memory: {} MB".format(end_mem))
	print("Number of Rows: {}".format(Handler.Row_Count))
	print("Time taken: {} s".format(int((end_time - start_time))))
	print("Memory used: {} MB".format(abs(end_mem - start_mem)))
