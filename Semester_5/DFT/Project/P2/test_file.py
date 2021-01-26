import numpy as np


my_dict = {'dict0.0':np.array([1,2,3,4]),'dict1.0':np.array([5,6,7,8]),'dict2.0':np.array([4,2,7,9])}
#print(my_dict)
arr1 = np.array([[1,0],[3,0]])
arr2 = np.array([[5,6],[7,7]])
#print(x for x in my_dict.keys())


#for n in np.arange(0.0,3.0,1.0):
	#print(n)
#print(np.count_nonzero(arr1))
x = np.array([1,2,3,4])
#print(x.mean())
y = np.array([1,1,2,3])
z = np.sum(x*y)
#print(z)
#print(1/3)

x = [1,2,4]
coef = 0.5
d = np.array([])
for i in range(1,len(x)):
    d = np.append(d,x[i]-coef*x[i-1])
print(np.var([d],ddof=1))

x = np.array([0.1,0.5,0.2,0.4,0.9])
probability = (x)/(np.sum(x))
H =  -np.sum(probability * np.log2(probability))
print(H)