# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:34:35 2018

@author: yangy
"""


import pandas as pd
import matplotlib.pyplot as plt

filename = 'State_Custom_Data.csv'
chunksize = 10 ** 3
numrow = 0
chunks = []
for chunk in pd.read_csv(filename, chunksize=chunksize):
#    for row in chunk:
#        print(row)
    chunks.append(chunk)

## data cleaning    
dataframe1 = pd.concat(chunks, axis=0) 

dataframe1['SEASON'] = dataframe1['SEASON'].str.replace('2017-18', '2017')
dataframe1['SEASON'] = dataframe1['SEASON'].str.replace('2015-16', '2015')
dataframe1['SEASON'] = dataframe1['SEASON'].str.replace('2016-17', '2016')

df2 = dataframe1.drop(['AREA', 'AGE GROUP','PERCENT P&I','PERCENT COMPLETE'], axis=1)
#df2['NUM INFLUENZA AND PNEUMONIA DEATHS'] = df2['NUM INFLUENZA AND PNEUMONIA DEATHS'].astype('int')

df2015 = df2.loc[df2['SEASON'] == '2015']
df2016 = df2.loc[df2['SEASON'] == '2016']
df2017 = df2.loc[df2['SEASON'] == '2017']

df_California = df2016[df2016['STATENAME'] == 'California'].sort_values(by=['WEEK'])
df_NewYork= df2016[df2016['STATENAME'] == 'New York'].sort_values(by=['WEEK'])
df_Texas = df2016[df2016['STATENAME'] == 'Texas'].sort_values(by=['WEEK'])
df_Florida = df2016[df2016['STATENAME'] == 'Florida'].sort_values(by=['WEEK'])
 
x = list(df_California['WEEK'])
y = list(df_California['NUM INFLUENZA AND PNEUMONIA DEATHS'])
z = list(df_NewYork['NUM INFLUENZA AND PNEUMONIA DEATHS'])
k = list(df_Texas['NUM INFLUENZA AND PNEUMONIA DEATHS'])
l = list(df_Florida['NUM INFLUENZA AND PNEUMONIA DEATHS'])


fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_title('2016 NUM INFLUENZA AND PNEUMONIA DEATHS')
ax.set_xlabel('Week')
ax.set_ylabel('NUM INFLUENZA AND PNEUMONIA DEATHS')

plt.plot(x, y, 'r', label = 'California')
plt.plot(x, z, 'b',label = 'NewYork')
plt.plot(x, k, 'g',label = 'Texas')
plt.plot(x,l,'m',label = 'Florida')      
plt.legend(bbox_to_anchor=(0.3, 0.8, 0.6, 0.8), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('2016 NUM INFLUENZA AND PNEUMONIA DEATHS')
ax.set_xlabel('Week')
ax.set_ylabel('NUM INFLUENZA AND PNEUMONIA DEATHS')

width = 0.35  
bar1 = plt.bar(x,y,color='red',label = 'California')
bar2 = plt.bar(x,z,color='blue', bottom=y, label = 'NewYorkCity')
bar3 = plt.bar(x, k,color='green',label = 'Texas')
bar4 = plt.bar(x, l,color='purple',label = 'Florida')
plt.legend(bbox_to_anchor=(0.3, 0.8, 0.6, 0.8), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

plt.show()
