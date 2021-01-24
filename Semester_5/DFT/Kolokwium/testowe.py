import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


print(np.convolve([1,2,3],[2,1,1,1]))
print()
print(np.convolve([1,2,3],[1,2],'full'))