from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


def low_pass():
    numtaps = 80
    pass_zero = 'low_pass'
    cutoff = 0.5
    a = signal.firwin(numtaps, cutoff)
    w,h = signal.freqz(a)
    plt.figure(1)
    plt.plot(w,20*np.log10(abs(h)))
    plt.show()

low_pass()
