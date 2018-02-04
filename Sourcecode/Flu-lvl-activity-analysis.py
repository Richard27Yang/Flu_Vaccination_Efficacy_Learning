# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:57:06 2018

@author: yangy
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

filename = 'Flu_lvl_2015-2018.csv'
chunksize = 10 ** 3
numrow = 0
chunks = []
for chunk in pd.read_csv(filename, chunksize=chunksize):
#    for row in chunk:
#        print(row)
    chunks.append(chunk)

## data cleaning    
dataframe1 = pd.concat(chunks, axis=0) 
dataframe1['ACTIVITY LEVEL'] = dataframe1['ACTIVITY LEVEL'].str.replace('Level', '')
dataframe1['SEASON'] = dataframe1['SEASON'].str.replace('2017-18', '2017')
dataframe1['SEASON'] = dataframe1['SEASON'].str.replace('2015-16', '2015')
dataframe1['SEASON'] = dataframe1['SEASON'].str.replace('2016-17', '2016')
df2 = dataframe1.drop(['ACTIVITY LEVEL LABEL', 'WEEKEND'], axis=1)
df2['ACTIVITY LEVEL'] = df2['ACTIVITY LEVEL'].astype('int')

df2015 = df2.loc[df2['SEASON'] == '2015']
df2016 = df2.loc[df2['SEASON'] == '2016']
df2017 = df2.loc[df2['SEASON'] == '2017']

df_Alabama = df2016[df2016['STATENAME'] == 'Alabama'].sort_values(by=['WEEK'])
# df_Alabama = df2016[df2016['STATENAME'] == 'Alabama'].drop('STATENAME',axis =1 )
df_Alabama.plot(x='WEEK', y='ACTIVITY LEVEL', title='Alabama')

df_California = df2016[df2016['STATENAME'] == 'California'].sort_values(by=['WEEK'])
df_NewYork= df2016[df2016['STATENAME'] == 'New York'].sort_values(by=['WEEK'])
df_Texas = df2016[df2016['STATENAME'] == 'Texas'].sort_values(by=['WEEK'])
df_Florida = df2016[df2016['STATENAME'] == 'Florida'].sort_values(by=['WEEK'])
 
df4states = pd.merge(df_California, df_NewYork, on='WEEK', how='inner')
df4states = df4states.merge(df_Texas, on='WEEK', how='inner')
df4states = df4states.merge(df_Texas, on='WEEK', how='inner')
df4states = df4states.merge(df_Florida, on='WEEK', how='inner')

x = list(df_California['WEEK'])
y = list(df_California['ACTIVITY LEVEL'])
z = list(df_NewYork['ACTIVITY LEVEL'])
k = list(df_Texas['ACTIVITY LEVEL'])
l = list(df_Florida['ACTIVITY LEVEL'])

# plt.plot(x, y, color='r', linewidth=2.0,label="California")

#plt.plot(x, y, 'r', label="test1", x, z, 'b', x, k, 'g',x,l,'m',linewidth=2.0)
# cannot put legend


fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_title('2016 Flu Activity Level in 4 States')
ax.set_xlabel('Week')
ax.set_ylabel('Flu Activity Level')

plt.plot(x, y, 'r', label = 'California')
plt.plot(x, z, 'b',label = 'NewYork')
plt.plot(x, k, 'g',label = 'Texas')
plt.plot(x,l,'m',label = 'Florida')      
plt.legend(bbox_to_anchor=(0.3, 0.8, 0.6, 0.8), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

plt.show()

bar1 = plt.bar(x,y,color='red')
bar2 = plt.bar(x,z,color='blue')


#plt.plot(df2015['WEEK'],df2015['ACTIVITY LEVEL'])
#plt.plot(df2016['WEEK'],df2016['ACTIVITY LEVEL'])

###########################################################
###########################################################
# bar plot
fig, ax = plt.subplots()
ax.set_title('2016 Flu Activity Level in 4 States')
ax.set_xlabel('Week')
ax.set_ylabel('Flu Activity Level')

xfloat = [float(i) for i in x]
xfloat = np.array(x)
yfloat = np.array(y)
zfloat = np.array(z)
index = xfloat
bar_width = 0.35
opacity = 0.8
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, y, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='California')

rects2 = plt.bar(xfloat + bar_width, zfloat, bar_width,
                 alpha=opacity,
                 color='r',
                 label='NewYork')


rects2 = plt.bar(xfloat + 2*bar_width, k, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Texas')

plt.legend(bbox_to_anchor=(0.3, 0.8, 0.6, 0.8), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
fig.show()
###########################################################
###########################################################
