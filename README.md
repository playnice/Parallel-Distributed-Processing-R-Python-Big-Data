The main goal of this project is to improve the computation times in data processing
for the R and Python programming languages by utilizing parallel programming
techniques. The goals include implementing and leveraging various
parallel computing strategies. The performance between the two languages are
then compared.
In this project, we processed three large XML datasets, comprising [datascience
(70 MB)], [softwareengineering(1.3 GB)] and [stackoverow (185 GB)] data.
We used R and Python program scripts that implement parallel and distributed
programming strategies for computation speed ups.
We implemented SAX (Simple API for XML) processing instead of DOM (Document
Object Mode) on the humongous XML les in this project because DOM
processing requires memory several times the size of XML les. Thus, it is impossible
to use DOM processing as the machine used in this project only have 8
GB memory. SAX processing requires almost no memory to process large XML
les as it does not load them into memory.
Processing time is very important in data analytics. It would be very unproductive
to be waiting hours, days or even months for the results. Not to mention
time-sensitive analysis. So, we must achieve a reasonable duration for completion
of data processing. In this project, we found that parallel and distributed
processing improved the processing time of large XML les signicantly.
We executed multi-threading SAX processing on an exactly same XML le multiple
times and saw increase in data processing speed. This experiment is wrongly
setup because when we did multi-threaded SAX processing on real dataset (several
dierent XMLs), we saw a decrease in data processing speed. This is because
the machine in this project only had single hard disk drive, thus the performance
is limited by the single read head as the disk need to spin back and forth to
serve multiple read on multiple XML les. In this project, we proved that data
processing speed is improved when we did parallel SAX processing on multiple
HDD.
We analysed large XML les in this project, but depending on the types of data
and its source format, the method to use in Big Data analysis must be approached
Abstract xviii
dierently on a case by case basis. We found the methods of processing in this
project for our XML can be improved by adding more HDD, parallel process data
on separate machines and combine the results upon completion and increasing the
buer size of SAX parser.
It is important to note that, as computer science students, our primary focus in
this project is on computing techniques and time speed ups. Even though we
will be processing big data, the value of the data and its output are of secondary
importance.
