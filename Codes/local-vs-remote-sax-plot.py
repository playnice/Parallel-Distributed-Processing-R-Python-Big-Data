import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#===================================+
# Sequential SAX PostHistory Remote |
#===================================+
postHistorySequentialRemote = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV-remote-corrected/PostHistory-sequential.csv")
postHistorySequentialRemote['row_count'] = postHistorySequentialRemote['row_count']/1000000
postHistorySequentialRemote['process_time_sec'] = postHistorySequentialRemote['process_time_sec']/3600

#==================================+
# Sequential SAX PostHistory Local |
#==================================+
postHistorySequentialLocal = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV/PostHistory-sequential-R1.csv")
postHistorySequentialLocal['row_count'] = postHistorySequentialLocal['row_count']/1000000
postHistorySequentialLocal['process_time_sec'] = postHistorySequentialLocal['process_time_sec']/3600

#=============================+
# Sequential SAX Posts Remote |
#=============================+
postsSequentialRemote = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV-remote-corrected/Posts-sequential.csv")
postsSequentialRemote['row_count'] = postsSequentialRemote['row_count']/1000000
postsSequentialRemote['process_time_sec'] = postsSequentialRemote['process_time_sec']/3600

newpostsSequentialRemote = pd.DataFrame(postsSequentialRemote)
newpostsSequentialRemote.drop(newpostsSequentialRemote.index[0], inplace=True)
newpostsSequentialRemote['row_count'] += float(postHistorySequentialRemote.tail(1)['row_count'])
newpostsSequentialRemote['process_time_sec'] += float(postHistorySequentialRemote.tail(1)['process_time_sec'])

#concatenate two dataframes
resultSequentialRemote = pd.concat([postHistorySequentialRemote,newpostsSequentialRemote])
resultSequentialRemote= resultSequentialRemote.reset_index(drop=True)

#============================+
# Sequential SAX Posts Local |
#============================+
postsSequentialLocal = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV/Posts-sequential-R1.csv")
postsSequentialLocal['row_count'] = postsSequentialLocal['row_count']/1000000
postsSequentialLocal['process_time_sec'] = postsSequentialLocal['process_time_sec']/3600

newpostsSequentialLocal = pd.DataFrame(postsSequentialLocal)
newpostsSequentialLocal.drop(newpostsSequentialLocal.index[0], inplace=True)
newpostsSequentialLocal['row_count'] += float(postHistorySequentialLocal.tail(1)['row_count'])
newpostsSequentialLocal['process_time_sec'] += float(postHistorySequentialLocal.tail(1)['process_time_sec'])

#concatenate two dataframes
resultSequentialLocal = pd.concat([postHistorySequentialLocal,newpostsSequentialLocal])
resultSequentialLocal= resultSequentialLocal.reset_index(drop=True)

#==========================================+
# Concurrent SAX PostHistory & Posts Local |
#==========================================+
postHistoryConcurrentLocal = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV/PostHistory-concurrent-R1.csv")
postHistoryConcurrentLocal['row_count'] = postHistoryConcurrentLocal['row_count']/1000000
postHistoryConcurrentLocal['process_time_sec'] = postHistoryConcurrentLocal['process_time_sec']/3600

postsConcurrentLocal = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV/Posts-concurrent-R1.csv")
postsConcurrentLocal['row_count'] = postsConcurrentLocal['row_count']/1000000
postsConcurrentLocal['process_time_sec'] = postsConcurrentLocal['process_time_sec']/3600

#===========================================+
# Concurrent SAX PostHistory & Posts Remote |
#===========================================+
postHistoryConcurrentRemote = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV-remote-corrected/PostHistory-concurrent.csv")
postHistoryConcurrentRemote['row_count'] = postHistoryConcurrentRemote['row_count']/1000000
postHistoryConcurrentRemote['process_time_sec'] = postHistoryConcurrentRemote['process_time_sec']/3600

postsConcurrentRemote = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV-remote-corrected/Posts-concurrent.csv")
postsConcurrentRemote['row_count'] = postsConcurrentRemote['row_count']/1000000
postsConcurrentRemote['process_time_sec'] = postsConcurrentRemote['process_time_sec']/3600

#================+
# Graph Plotting |
#================+
fig = plt.figure(figsize=(11,8))
ax = fig.add_subplot(111)

#PostHistory Line Graph Local
ax.plot(resultSequentialLocal['process_time_sec'], resultSequentialLocal['row_count'],label = 'Local Sequential Posts+PostsHistory', color = 'm')
ax.plot(postHistoryConcurrentLocal['process_time_sec'], postHistoryConcurrentLocal['row_count'],label='Local Concurrent PostsHistory', color='y', marker = '*')
ax.plot(postsConcurrentLocal['process_time_sec'], postsConcurrentLocal['row_count'],label='Local Concurrent Posts', color='y', marker = 'x')

#PostHistory Line Graph Remote
ax.plot(resultSequentialRemote['process_time_sec'], resultSequentialRemote['row_count'],label = 'Remote Sequential Posts+PostsHistory', color = 'b')
ax.plot(postHistoryConcurrentRemote['process_time_sec'], postHistoryConcurrentRemote['row_count'],label='Remote Concurrent PostsHistory', color='r', marker = '*')
ax.plot(postsConcurrentRemote['process_time_sec'], postsConcurrentRemote['row_count'],label='Remote Concurrent Posts', color='r', marker = 'x')

#Setting up graph's parameters
plt.xticks(np.arange(min(postHistoryConcurrentRemote['process_time_sec']), max(postHistoryConcurrentRemote['process_time_sec'])+1 , 1))
plt.yticks(np.arange(min(resultSequentialRemote['row_count']), max(resultSequentialRemote['row_count'])+10 , 10))

plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.xlabel('Process Time (hr)')
plt.ylabel('Row Count (million)')
ax.set_title('Performance Comparison of SAX Parse between Local & Remote',fontweight = "bold",fontsize = 15)
handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='lower right')
ax.grid('on')
ax.annotate('Local Posts.XML starts here', xy=(newpostsSequentialLocal.loc[1]['process_time_sec'],newpostsSequentialLocal.loc[1]['row_count']),  xycoords='data',
            xytext=(0.4, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',)
ax.annotate('Remote Posts.XML starts here', xy=(newpostsSequentialRemote.loc[1]['process_time_sec'],newpostsSequentialRemote.loc[1]['row_count']),  xycoords='data',
            xytext=(0.4, 0.8), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',)
ax.annotate('Parsing speed increased here', xy=(postsConcurrentRemote.loc[37]['process_time_sec'],59),  xycoords='data',
            xytext=(0.55,0.5), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',)

plt.vlines(postsConcurrentRemote.loc[37]['process_time_sec'], 0, 59, linestyle="dashed")
plt.vlines(postsConcurrentLocal.loc[37]['process_time_sec'], 0, 59, linestyle="dashed")
plt.hlines(postsConcurrentLocal.loc[37]['row_count'], 0,3900, linestyle="dashed")
plt.hlines(postHistoryConcurrentLocal.loc[94]['row_count'], 0,3900, linestyle="dashed")
plt.hlines(resultSequentialLocal.loc[131]['row_count'], 0,3900, linestyle="dashed")
plt.savefig('Performance Comparison of SAX Parse of Local & Remote.png')


