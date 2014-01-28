from scipy import stats
import numpy as np
import math

num = int(raw_input())
ds =  np.array([float(elem) for elem in raw_input().split(" ")])
mean = ds.mean()
std=np.std(ds)
confidence = 1.96 * (std / math.sqrt(9))

print '%.1f' % mean
print '%.1f' % np.median(ds)
print int(stats.mode(ds)[0][0])
print '%.1f' % std
print '%.1f' % (mean - confidence) + " " + '%.1f' % (mean + confidence)