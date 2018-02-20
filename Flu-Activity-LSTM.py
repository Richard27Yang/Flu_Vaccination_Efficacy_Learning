from __future__ import print_function
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:34:18 2018

@author: yangy
"""

''' prediction of flu activitiy level using Keras '''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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


train_dataset = df_Cal['ACTIVITY LEVEL'].values
train_dataset = train_dataset.astype('float32')
# transform from rank 1 array to a column
train_dataset = train_dataset.reshape((len(train_dataset),1))

# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
train_dataset = scaler.fit_transform(train_dataset)

# split into train and test sets
train_size = int(len(train_dataset) * 0.67)
test_size = len(train_dataset) - train_size
train   = train_dataset[0:train_size,:]
test    = train_dataset[train_size:len(train_dataset)]

# reshape into X=t and Y=t+1
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
trainY = np.reshape(trainY, (trainY.shape[0], 1))

testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
testY = np.reshape(testY, (testY.shape[0], 1))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(6, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
# start training
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)

## results analysis
# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

# shift train predictions for plotting
trainPredictPlot = np.empty_like(train_dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

# shift test predictions for plotting
testPredictPlot = np.empty_like(train_dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(train_dataset)-1, :] = testPredict

# plot baseline and predictions
plt.plot(scaler.inverse_transform(train_dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()

#
###################################33
#import statsmodels.api as sm
#
## Estimation
#olsmod = sm.OLS(trainY, trainX)
#olsres = olsmod.fit()
#print(olsres.summary())
#
#ypred = olsres.predict(X)
#print(ypred)
#
#import matplotlib.pyplot as plt
#
#fig, ax = plt.subplots()
#ax.plot(x1, y, 'o', label="Data")
#ax.plot(x1, y_true, 'b-', label="True")
#ax.plot(np.hstack((x1, x1n)), np.hstack((ypred, ynewpred)), 'r', label="OLS prediction")
#ax.legend(loc="best");
