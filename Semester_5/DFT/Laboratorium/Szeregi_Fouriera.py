import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def iloczyn_skalarny(T=1):
	"""
	Narysować kilka funkcji z podanych zbiorów i wyznaczyć ich iloczyny skalarne.
	"""

	#Zbior1
	#arr1 = [1/(np.sqrt(T)),np.sqrt(2/T)*np.cos(2*np.pi*n)]

def szereg_fouriera(N=200,T=4):
	"""
	Dany jest szereg Fouriera reprezentujący sygnał ciągu impulsów prostokątnych
	"""
	n = np.arange(-N,N+1)
	t = np.linspace(0,T,1000)
	xt = 0
	ampl = np.array([])
	for i in n:
		if i == 0:
			Xn = 1/2
			xt = xt + Xn*np.exp(1j*2*np.pi*i*t)
			ampl = np.append(ampl,np.abs(Xn))
		else:
			Xn = (np.float(-1)**i-1)/(-1j*2*np.pi*i)
			xt = xt + Xn*np.exp(1j*2*np.pi*i*t/T)
			if i > 0:
				ampl = np.append(ampl,np.abs(Xn*2))
	plt.figure(1)
	plt.plot(t,xt)
	plt.title(f'Użyte harmoniczne: {N}, T = {T}')
	plt.grid()
	plt.show()
	plt.figure(2)
	plt.stem(np.arange(0,N+1),ampl)
	plt.grid()
	plt.show()

szereg_fouriera()