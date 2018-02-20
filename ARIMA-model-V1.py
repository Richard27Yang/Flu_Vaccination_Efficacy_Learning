# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:04:31 2018

@author: yangy
"""

import pandas as pd
from pandas import datetime
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot

filename = 'daily-total-female-births-in-cal.csv'
chunksize = 10 ** 3
numrow = 0
chunks = []
for chunk in pd.read_csv(filename, chunksize=chunksize):
#    for row in chunk:
#        print(row)
    chunks.append(chunk)
    
dataframe1 = pd.concat(chunks, axis=0) 

dates = np.array(dataframe1['Date'])
female_births = np.array(dataframe1['Daily total female births in California, 1959'])
# datetime.strptime(b, "%Y-%b")

# series = pd.read_csv('daily-total-female-births-in-cal.csv', header=0)
# fit model
model = ARIMA(series, order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())
# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())