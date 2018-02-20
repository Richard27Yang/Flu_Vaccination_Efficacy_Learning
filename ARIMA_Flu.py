# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:18:35 2018

@author: yangy
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.stats import norm
import statsmodels.api as sm
import matplotlib.pyplot as plt
from datetime import datetime
import requests
from io import BytesIO

''' prediction of flu activitiy level using Keras '''

from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return np.array(dataX), np.array(dataY)

def read_dataset(filename):
    chunksize = 10 ** 3
    # numrow = 0
    chunks = []
    for chunk in pd.read_csv(filename, chunksize=chunksize):
#    for row in chunk:
#        print(row)
        chunks.append(chunk)   
    dataframe1 = pd.concat(chunks, axis=0)
    return dataframe1

def dataframe_clean(dataframe1):
    dataframe1['ACTIVITY LEVEL'] = dataframe1['ACTIVITY LEVEL'].str.replace('Level', ' ')
    dataframe1['ACTIVITY LEVEL'] = dataframe1['ACTIVITY LEVEL'].astype('float')
    dataframe1['WEEKEND_DATE'] =  pd.to_datetime(dataframe1['WEEKEND'])
    dataframe1.drop('ACTIVITY LEVEL LABEL', axis =1 )
    dataframe1.drop('WEBSITE', axis = 1 )
    df2 = dataframe1.sort_values(by='WEEKEND_DATE')
    return df2

# fix random seed for reproducibility
np.random.seed(7)

# load the dataset
filename = './Datasets/ILI-history-data-state.csv'
dataframe1 = read_dataset(filename)
df_clean = dataframe_clean(dataframe1)

df_Cal = dataframe1.loc[dataframe1['STATENAME'] == 'California'].sort_values(by='WEEKEND_DATE')
df_Cal.index=df_Cal['WEEKEND_DATE']

train_dataset = df_Cal['ACTIVITY LEVEL'].values
train_dataset = train_dataset.astype('float32')
# transform from rank 1 array to a column
train_dataset = train_dataset.reshape((len(train_dataset),1))
#
## normalize the dataset
#scaler = MinMaxScaler(feature_range=(0, 1))
#train_dataset = scaler.fit_transform(train_dataset)
#
# Fit the model
mod = sm.tsa.statespace.SARIMAX(train_dataset, trend='c', order=(1,1,1))
res = mod.fit(disp=True)
print(res.summary())


# Graph data
fig, axes = plt.subplots(1, 2, figsize=(15,4))

# Levels
axes[0].plot(df_Cal.index._mpl_repr(), df_Cal['ACTIVITY LEVEL'], '-')
axes[0].set(title='US Flu activity level')

# Log difference
axes[1].plot(df_Cal.index._mpl_repr(), df_Cal['ACTIVITY LEVEL'], '-')
axes[1].hlines(0, df_Cal.index[0], df_Cal.index[-1], 'r')
axes[1].set(title='US Flu activity level - difference of logs');

