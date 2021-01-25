import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


#print(np.convolve([1,2,3,0],[2,1,1,1]))
#print()
#print(np.convolve([1,2,3],[1,2],'full'))


def freq_characteristic(a=[1,2,1,2],N=3):
	"""
	wyznaczyć ch-kę częstotliwościową filtrów z poprzedniego zadania dla różnych funkcji
	okien, przy N=15.
	"""
	H = 0
	#w = np.linspace(-np.pi,np.pi,1000)
	w = np.pi/5
	for n in np.arange(-N,1):
		H = H+a[n+N]*np.exp(-1j*w*n)
	#plt.figure(1)
	#print(np.where(np.isclose(w,0.62580274)))
	#print(np.abs(H))
	#plt.plot(w,H,label='Rect')
	#plt.ylabel('Wzmocnienie')
	#plt.xlabel('$\pi$')
	#plt.legend()
	#plt.grid()
	#plt.show()

freq_characteristic()

system = ([1],[1,0.5],1/100)
t,y = signal.dimpulse(system)
print(np.abs(signal.dfreqresp(system,w=np.pi)[1]))
