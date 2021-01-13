import numpy as np

data2 = np.array([])
data1 = np.array([1,2,3,4,5])
for i in range(1,len(data1)):
	data2 = np.append(data2,data1[i]-data1[i-1])

print(data1[0:len(data1)-1])