import re
import numpy as np
import matplotlib.pyplot as plt

def autocorr(x=np.array([1,-9,4,7,9,-7,4,1,8,5])):
    plt.figure(2)
    plt.grid(True)
    plt.xlim([0,10])
    plt.title("Funkcja autokorelacji")
    output_data = plt.acorr(x, maxlags=10,normed=True)
    auto_coef = output_data[1][10:]
    plt.show()
    return auto_coef

autocorr()