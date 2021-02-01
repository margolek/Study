import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def filtruj(x=[1,2,3],h=[1,1,1,1]):
	"""
	Napisać funkcję y = filtruj(x, h), która wyznacza sygnał y będący wynikiem filtracji
	sygnału x przez filtr FIR o odpowiedzi impulsowej h
	"""
	filtered_signal = signal.convolve(x,h,mode='full')
	print(filtered_signal)	#len(filtered) == len(signal)
def low_high_pass(wg_low=np.pi/8,wg_high=np.pi/6,N=7):
	h_lp = np.array([])
	h_hp = np.array([])
	n = np.arange(-N,N+1,1)
	for i in n:
		if i == 0:
			h_lp = np.append(h_lp,wg_low/np.pi)
			h_hp = np.append(h_hp, 1-(wg_high/np.pi))
		else:
			h_lp = np.append(h_lp,np.sin(wg_low*i)/(np.pi*i))
			h_hp = np.append(h_hp,-np.sin(wg_high*i)/(np.pi*i))

	h_hp_blackam = np.blackman(2*N+1)*h_hp
	print(f'blackamn wynosi{np.sum(h_hp_blackam[:9])}')
	h_hp_hamm = np.hamming(2*N+1)*h_hp
	plt.figure(1)
	plt.title('Low pass')
	plt.scatter(n,h_lp,label='Rect',marker='x')
	plt.scatter(n,h_lp_hamm,label='Hamm',marker='o')
	plt.legend()
	plt.grid()
	plt.show()

	plt.figure(2)
	plt.title('High pass')
	plt.scatter(n,h_hp,label='Rect',marker='x')
	plt.scatter(n,h_hp_hamm,label='Hamm',marker='o')
	plt.legend()
	plt.grid()
	plt.show()
	return h_lp,h_lp_hamm
a,b = low_high_pass()
def freq_characteristic(a,b,N=15):
	"""
	wyznaczyć ch-kę częstotliwościową filtrów z poprzedniego zadania dla różnych funkcji
	okien, przy N=15.
	"""
	H = 0
	H_hamm = 0
	w = np.linspace(-np.pi,np.pi,1000)
	for n in np.arange(-N,N+1):
		H = H+a[n+N]*np.exp(-1j*w*n)
		H_hamm = H_hamm+b[n+N]*np.exp(-1j*w*n)

	w1, h1 = signal.freqz(a)
	w2, h2 = signal.freqz(b)
	plt.figure(1)
	plt.plot(w,H,label='Rect')
	plt.plot(w,H_hamm,label='Hamm')
	plt.ylabel('Wzmocnienie')
	plt.xlabel('$\pi$')
	plt.legend()
	plt.grid()
	plt.show()

	plt.figure(2)
	plt.plot(w,20*np.log10(H),label='Rect')
	plt.plot(w,20*np.log10(H_hamm),label='Hamm')
	plt.ylabel('Wzmocnienie [dB]')
	plt.legend()
	plt.xlabel('$\pi$')
	plt.grid()
	plt.show()

	plt.figure(3)
	plt.title('Freqz')
	plt.plot(w1, 20*np.log10(h1))
	plt.plot(w2, 20*np.log10(h2))
	plt.ylabel('Amplitude Response (dB)')
	plt.xlabel('Frequency (rad/sample)')
	plt.grid()
	plt.show()
#freq_characteristic(a, b)
def zaprojektowac_filtr():
	"""
	Zaprojektować cyfrowy filtr dolnoprzepustowy o częstotliwości granicznej f0 = 150 Hz,
	przy częstotliwości próbkowania fp = 1000Hz. Narysować ch-kę amplitudową. Sprawdzić
	działanie zaprojektowanego filtru poprzez filtrację sygnału złożonego z dwóch sinusoid o
	częstotliwościach f1 = 100Hz i f2 = 250Hz.
	"""



