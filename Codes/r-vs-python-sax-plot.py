import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#===========================================+
# Python Sequential SAX PostHistory & Posts |
#===========================================+
postHistorySequentialPy = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV/PostHistory-sequential-R1.csv")
postHistorySequentialPy['row_count'] = postHistorySequentialPy['row_count']/1000000

postsSequentialPy = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV/Posts-sequential-R1.csv")
postsSequentialPy['row_count'] = postsSequentialPy['row_count']/1000000

newPostsSequentialPy = pd.DataFrame(postsSequentialPy)
newPostsSequentialPy.drop(newPostsSequentialPy.index[0], inplace=True)
newPostsSequentialPy['row_count'] += float(postHistorySequentialPy.tail(1)['row_count'])
newPostsSequentialPy['process_time_sec'] += int(postHistorySequentialPy.tail(1)['process_time_sec'])

#concatenate two dataframes
resultSequentialPy = pd.concat([postHistorySequentialPy,newPostsSequentialPy])
resultSequentialPy= resultSequentialPy.reset_index(drop=True)

#===========================================+
# Python Concurrent SAX PostHistory & Posts |
#===========================================+
postHistoryConcurrentPy = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV/PostHistory-concurrent-R1.csv")
postHistoryConcurrentPy['row_count'] = postHistoryConcurrentPy['row_count']/1000000

postsConcurrentPy = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV/Posts-concurrent-R1.csv")
postsConcurrentPy['row_count'] = postsConcurrentPy['row_count']/1000000

#==========================================+
# Python Parallel SAX PostHistory & Posts  |
#==========================================+
postHistoryParallelPy = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/PostHistory-CSV/PostHistory-parallel-R1.csv")
postHistoryParallelPy['row_count'] = postHistoryParallelPy['row_count']/1000000

postsParallelPy = pd.read_csv("/home/xiang/Downloads/FYP2/python-sax-parse-concurrent-sequential/Posts-CSV/Posts-parallel-R1.csv")
postsParallelPy['row_count'] = postsParallelPy['row_count']/1000000

#======================================+
# R Sequential SAX PostHistory & Posts |
#======================================+
postHistorySequentialR = pd.read_csv("/home/xiang/Downloads/FYP2/r-sax-parse/CSV/PostHistory-sequential.csv")
postHistorySequentialR['row_count'] = postHistorySequentialR['row_count']/1000000

postsSequentialR = pd.read_csv("/home/xiang/Downloads/FYP2/r-sax-parse/CSV/Posts-sequential.csv")
postsSequentialR['row_count'] = postsSequentialR['row_count']/1000000

newPostsSequentialR = pd.DataFrame(postsSequentialR)
newPostsSequentialR.drop(newPostsSequentialR.index[0], inplace=True)
newPostsSequentialR['row_count'] += float(postHistorySequentialR.tail(1)['row_count'])
newPostsSequentialR['process_time_sec'] += int(postHistorySequentialR.tail(1)['process_time_sec'])

#concatenate two dataframes
resultSequentialR = pd.concat([postHistorySequentialR,newPostsSequentialR])
resultSequentialR= resultSequentialR.reset_index(drop=True)

#======================================+
# R Concurrent SAX PostHistory & Posts |
#======================================+
postHistoryConcurrentR = pd.read_csv("/home/xiang/Downloads/FYP2/r-sax-parse/CSV/PostHistory-concurrent.csv")
postHistoryConcurrentR['row_count'] = postHistoryConcurrentR['row_count']/1000000

postsConcurrentR = pd.read_csv("/home/xiang/Downloads/FYP2/r-sax-parse/CSV/Posts-concurrent.csv")
postsConcurrentR['row_count'] = postsConcurrentR['row_count']/1000000

#=====================================+
# R Parallel SAX PostHistory & Posts  |
#=====================================+
postHistoryParallelR = pd.read_csv("/home/xiang/Downloads/FYP2/r-sax-parse/CSV/PostHistory-parallel.csv")
postHistoryParallelR['row_count'] = postHistoryParallelR['row_count']/1000000

postsParallelR = pd.read_csv("/home/xiang/Downloads/FYP2/r-sax-parse/CSV/Posts-parallel.csv")
postsParallelR['row_count'] = postsParallelR['row_count']/1000000

#================+
# Graph Plotting |
#================+
fig = plt.figure(figsize=(11,8))
ax = fig.add_subplot(111)

#Python Sequential Line
ax.plot(resultSequentialPy['process_time_sec'], resultSequentialPy['row_count'],label = 'Python Sequential Posts+PostHistory', color = 'b')

#Python Concurrent Lines
ax.plot(postHistoryConcurrentPy['process_time_sec'], postHistoryConcurrentPy['row_count'],label='Python Concurrent PostHistory', color='r')
ax.plot(postsConcurrentPy['process_time_sec'], postsConcurrentPy['row_count'],label='Python Concurrent Posts', color='r', marker = 'x')

#Python Parallel Lines
ax.plot(postHistoryParallelPy['process_time_sec'], postHistoryParallelPy['row_count'],label='Python Parallel PostHistory', color='c')
ax.plot(postsParallelPy['process_time_sec'], postsParallelPy['row_count'],label='Python Parallel Posts', color='c', marker = 'x')

#R Sequential Line
ax.plot(resultSequentialR['process_time_sec'], resultSequentialR['row_count'],label = 'R Sequential Posts+PostHistory', color = 'violet')

#R Concurrent Lines
ax.plot(postHistoryConcurrentR['process_time_sec'], postHistoryConcurrentR['row_count'],label='R Concurrent PostHistory', color='orange')
ax.plot(postsConcurrentR['process_time_sec'], postsConcurrentR['row_count'],label='R Concurrent Posts', color='orange', marker = 'x')

#R Parallel Lines
ax.plot(postHistoryParallelR['process_time_sec'], postHistoryParallelR['row_count'],label='R Parallel PostHistory', color='green')
ax.plot(postsParallelR['process_time_sec'], postsParallelR['row_count'],label='R Parallel Posts', color='green', marker = 'x')

#Setting up graph's parameters
plt.xticks(np.arange(min(resultSequentialPy['process_time_sec']), max(resultSequentialPy['process_time_sec'])+300 , 300))
plt.yticks(np.arange(min(resultSequentialPy['row_count']), max(resultSequentialPy['row_count'])+10 , 10))

plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.xlabel('Process Time (sec)')
plt.ylabel('Row Count (million)')
ax.set_title('Performance Comparison of SAX Parse between R & Python',fontweight = "bold",fontsize = 15)
handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper left')
ax.grid('on')
ax.annotate('Posts.XML starts here', xy=(newPostsSequentialPy.loc[1]['process_time_sec'],newPostsSequentialPy.loc[1]['row_count']),  xycoords='data',
            xytext=(0.6, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('Posts.XML starts here', xy=(newPostsSequentialR.loc[1]['process_time_sec'],newPostsSequentialPy.loc[1]['row_count']),  xycoords='data',
            xytext=(0.6, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('Parsing speed increased here', xy=(postsConcurrentPy.loc[37]['process_time_sec'],59),  xycoords='data',
            xytext=(0.98,0.3), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate('Parsing speed increased here', xy=(postsConcurrentR.loc[37]['process_time_sec'],59),  xycoords='data',
            xytext=(0.98,0.3), textcoords='axes fraction',
            arrowprops=dict(facecolor='black'),
            horizontalalignment='right', verticalalignment='top',
            )
plt.vlines(postsConcurrentPy.loc[37]['process_time_sec'], 0, 59, linestyle="dashed")
plt.vlines(postsConcurrentR.loc[37]['process_time_sec'], 0, 59, linestyle="dashed")
plt.hlines(postsConcurrentR.loc[37]['row_count'], 0,3900, linestyle="dashed")
plt.hlines(postHistoryConcurrentR.loc[94]['row_count'], 0,3900, linestyle="dashed")
plt.hlines(resultSequentialR.loc[131]['row_count'], 0,3900, linestyle="dashed")
plt.savefig('Performance Comparison of SAX Parse between R & Python.png')
