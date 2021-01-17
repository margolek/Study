import numpy as np



arr1 = np.array([[1,2,3,4],[3,2,3,4],[5,4,6,4],[7,6,4,3]])
print(arr1)

D,V = np.linalg.eig(arr1)
print(D)
print(V)
print(V.transpose())