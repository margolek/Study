import pywt
cA, cD = pywt.dwt([59,58,57,56,61,59,57,60,61,65,64,65,69,67,65,63,67,69,68,67], 'db1')
print(cA)
print(cD)