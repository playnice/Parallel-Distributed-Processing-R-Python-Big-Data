import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#============================+
# Sequential SAX PostHistory |
#============================+
postHistorySequential = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV/PostHistory-sequential-R1.csv")
postHistorySequential['row_count'] = postHistorySequential['row_count']/1000000

#======================+
# Sequential SAX Posts |
#======================+
postsSequential = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV/Posts-sequential-R1.csv")
postsSequential['row_count'] = postsSequential['row_count']/1000000

newPostsSequential = pd.DataFrame(postsSequential)
newPostsSequential.drop(newPostsSequential.index[0], inplace=True)
newPostsSequential['row_count'] += float(postHistorySequential.tail(1)['row_count'])
newPostsSequential['process_time_sec'] += int(postHistorySequential.tail(1)['process_time_sec'])

#concatenate two dataframes
resultSequential = pd.concat([postHistorySequential,newPostsSequential])
resultSequential= resultSequential.reset_index(drop=True)

#====================================+
# Concurrent SAX PostHistory & Posts |
#====================================+
postHistoryConcurrent = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV/PostHistory-concurrent-R1.csv")
postHistoryConcurrent['row_count'] = postHistoryConcurrent['row_count']/1000000

postsConcurrent = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV/Posts-concurrent-R1.csv")
postsConcurrent['row_count'] = postsConcurrent['row_count']/1000000

#====================================+
#  Parallel SAX PostHistory & Posts  |
#====================================+
postHistoryParallel = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV/PostHistory-parallel-R1.csv")
postHistoryParallel['row_count'] = postHistoryParallel['row_count']/1000000

postsParallel = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV/Posts-parallel-R1.csv")
postsParallel['row_count'] = postsParallel['row_count']/1000000

#================+
# Graph Plotting |
#================+
fig = plt.figure(figsize=(11,8))
ax = fig.add_subplot(111)

#Sequential Line
ax.plot(resultSequential['process_time_sec'], resultSequential['row_count'],label = 'Sequential Posts+PostHistory', color = 'b')

#Concurrent Lines
ax.plot(postHistoryConcurrent['process_time_sec'], postHistoryConcurrent['row_count'],label='Concurrent PostHistory', color='r')
ax.plot(postsConcurrent['process_time_sec'], postsConcurrent['row_count'],label='Concurrent Posts', color='r', marker = 'x')

#Parallel Lines
ax.plot(postHistoryParallel['process_time_sec'], postHistoryParallel['row_count'],label='Parallel PostHistory', color='c')
ax.plot(postsParallel['process_time_sec'], postsParallel['row_count'],label='Parallel Posts', color='c', marker = 'x')

#Setting up graph's parameters
plt.xticks(np.arange(min(resultSequential['process_time_sec']), max(resultSequential['process_time_sec'])+300 , 300))
plt.yticks(np.arange(min(resultSequential['row_count']), max(resultSequential['row_count'])+10 , 10))

plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.xlabel('Process Time (sec)')
plt.ylabel('Row Count (million)')
ax.set_title('Performance Comparison of Parallel, Concurrent & Sequential SAX Parse',fontweight = "bold",fontsize = 15)
handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper left')
ax.grid('on')
ax.annotate('Posts.XML starts here', xy=(newPostsSequential.loc[1]['process_time_sec'],newPostsSequential.loc[1]['row_count']),  xycoords='data',
            xytext=(0.4, 0.8), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('Parsing speed increased here', xy=(postsConcurrent.loc[37]['process_time_sec'],59),  xycoords='data',
            xytext=(0.7,0.5), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',
            )
plt.vlines(postsConcurrent.loc[37]['process_time_sec'], 0, 59, linestyle="dashed")
plt.hlines(postsConcurrent.loc[37]['row_count'], 0,3900, linestyle="dashed")
plt.hlines(postHistoryConcurrent.loc[94]['row_count'], 0,3900, linestyle="dashed")
plt.savefig('Performance Comparison of Parallel, Concurrent & Sequential SAX Parse.png')


