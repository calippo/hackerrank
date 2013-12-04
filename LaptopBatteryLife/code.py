from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pl
import numpy as np

import sys
data = float(sys.stdin.readline())

f = open("trainingdata.txt", "r")
X_train, y_train = zip(*[(float(r.split(",")[0]),float(r.split(",")[1])) for r in f])

true_x, true_y = [], []
for i in range(len(X_train)):
  if y_train[i] < 4:
    true_x.append([X_train[i]])
    true_y.append(y_train[i])

true_y = np.array(true_y)
true_x = np.array(true_x)
regr = LinearRegression()
regr.fit(true_x, true_y)

if data > 4:
  print 8
else:
  print regr.predict([data])
