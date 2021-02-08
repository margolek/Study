import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


#print(np.convolve([1,2,3,4],[1,3,1,2]))
#print()
print(np.convolve([1,2,3,4],[1,3,1,2],'full'))
energia = np.abs(-2+0j)**2+2*np.abs(0+3j)**2+2*np.abs(2)**2+2*np.abs(0+5j)**2+2*np.abs(6)**2
print(f'Energia wynosi {energia}')
print()