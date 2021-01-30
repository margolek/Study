import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


#print(np.convolve([1,2,3,4],[1,3,1,2]))
#print()
#print(np.convolve([1,2,3,4],[1,3,1,2],'full'))

print()
def low_high_pass(wg_low=np.pi/5,wg_high=np.pi/8,N=7):
	h_lp = np.array([])
	h_hp = np.array([])
	n = np.arange(-N,N+1,1)
	for i in n:
		if i == 0:
			h_lp = np.append(h_lp,wg_low/np.pi)
		else:
			h_lp = np.append(h_lp,np.sin(wg_low*i)/(np.pi*i))

	h_lp_hamm = np.blackman(2*N+1)*h_lp
	print(np.sum(h_lp_hamm[:9]))

low_high_pass()
def freq_characteristic(a=[1,2,1,2],N=3):
	"""
	wyznaczyć ch-kę częstotliwościową filtrów z poprzedniego zadania dla różnych funkcji
	okien, przy N=15.
	"""
	H = 0
	
	w = np.linspace(0,np.pi,1000)
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
w,h = signal.freqz([1],[0.5,1])
#print(np.abs(h[1]))
x = np.array([0.1, 0.1, 0.15, 0.15, 0.5])
probability = (x)/(np.sum(x))
H =  -np.sum(probability * np.log2(probability))
#print(H)
#print(np.abs(2+1j)*2)
N=7
H = 0
w = np.pi/8
for n in range(-N,N+1,1):
	H = H + hn[n+N]*np.exp(-1j*w*n)
print(H)
