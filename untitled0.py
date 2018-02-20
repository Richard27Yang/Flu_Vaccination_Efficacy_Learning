# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:13:14 2018

@author: yangy
"""


# PROBLEM LINK : https://www.hackerrank.com/challenges/temperature-predictions

import numpy as np
from sklearn import ensemble

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def func(x, p1,p2,p3):
  return p1 * np.sin(p2*x + p3) + 10

m={"January":0,"February":1,"March":2,"April":3,"May":4,"June":5,"July":6,"August":7,"September":8,"October":9,
         "November":10,"December":11}
n = int(input())
input()
mins = []
maxs = []
x = []
testx = []
for i in range(n):
    line = input().split('\t')
    maxs.append(float(line[2]) if isfloat(line[2]) else None)
    mins.append(float(line[3]) if isfloat(line[3]) else None)
    if isfloat(line[2]) and isfloat(line[3]):
        x.append([int(line[0]), m[line[1]]])
    else:
        testx.append([int(line[0]), m[line[1]]])
y = ([(x + y)/2 for x, y in zip(maxs, mins) if x is not None and y is not None])
# x = [[int(line[0]), m[line[1]]] for i in range(n) if maxs[i] is not None and mins[i] is not None]
model = ensemble.GradientBoostingRegressor()
model.fit(x, y)
a = list(model.predict(testx))

for i in range(n):
    if mins[i] == None:
        print(2 * a.pop(0) - maxs[i])
    if maxs[i] == None:
        print(2 * a.pop(0) - mins[i])

# plt.plot(x, y)