# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:09:41 2018

@author: yangy
"""


import pandas as pd
import matplotlib.pyplot as plt

filename = 'BRFSS__Graph_of_Current_Flu_Shots_taken_by_Adults_65_.csv'
chunksize = 10 ** 3
numrow = 0
chunks = []
for chunk in pd.read_csv(filename, chunksize=chunksize):
#    for row in chunk:
#        print(row)
    chunks.append(chunk)

## data cleaning    
dataframe1 = pd.concat(chunks, axis=0)

df2 = dataframe1.loc[dataframe1['Response'] == 'Yes']
df3 = df2[['Year','Locationdesc','Data_value']].reset_index()
plt.bar(df3.index,df3['Data_value'])

## population
dataframe2 = pd.read_csv('population.csv')

