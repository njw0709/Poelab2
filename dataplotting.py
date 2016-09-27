from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import interpolate as intp
import csv
import math

with open('data.csv', 'r') as f:
	data = list(csv.reader(f))
	data = data[:-1]

angle1 = [i[0] for i in data][:-1]
angle2 = [i[1] for i in data][:-1]
signal = [i[2] for i in data][:-1]


angle1=np.array(angle1,dtype=float)
angle2=np.array(angle2,dtype=float)
signal=np.array(signal,dtype=float)
distance = [-0.356*x+64.36+12.0 for x in signal]
angle1 = [math.pi/180.0*x for x in angle1]
angle2 = [math.pi/180.0*x for x in angle2]
xdist =[None]*len(distance)
ydist =[None]*len(distance)
zdist =[None]*len(distance)
for i in range(0,len(distance)):
	if distance[i]<40:
		xdist[i] = distance[i]*math.cos(angle1[i])*math.sin(angle2[i])
		ydist[i] = distance[i]*math.sin(angle1[i])
 		zdist[i] = distance[i]*math.cos(angle1[i])*math.cos(angle2[i])
	else:
		xdist[i]=0
print xdist
fig = plt.figure()

ax = fig.add_subplot(1,1,1,projection ="3d")
ax.scatter(xdist,ydist,zdist)
plt.show()
