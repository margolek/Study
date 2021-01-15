import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt


def Z1(N):
	hn = np.array([])
	for n in range(-N,N+1,1):
		if n == 0:
			hn = np.append(hn, 0)
		else:
			hn = np.append(hn, (1-(-1)**n)/(np.pi*n))
	plt.figure(1)
	plt.grid(True)
	plt.stem(range(-N,N+1,1),hn)
	plt.show()
	return hn

def Z2(hn,N):
	H = 0
	H_hamm = 0
	w = np.linspace(-np.pi, np.pi,500)
	for n in range(-N,N+1,1):
		H = H + hn[n+N]*np.exp(-1j*w*n)
	hn_hamm = np.hamming(2*N+1)*hn
	for n in range(-N,N+1,1):
		H_hamm = H_hamm + hn_hamm[n+N]*np.exp(-1j*w*n)
	plt.figure(2)
	plt.title('Charakterystyka amplitudowa')
	plt.xlabel('Pulsacja [rad]')
	plt.ylabel('Amplituda')
	plt.grid(True)
	plt.plot(w,np.abs(H),label='Rectangle')
	plt.plot(w,np.abs(H_hamm),label='Hamming')
	plt.legend()
	plt.show()

	plt.figure(3)
	plt.title('Charakterystyka fazowa')
	plt.xlabel('Pulsacja [rad]')
	plt.ylabel('faza [rad]')
	plt.grid(True)
	plt.plot(w,np.angle(H),label='Rectangle')
	plt.plot(w,np.angle(H_hamm),label='Hamming')
	plt.legend()
	plt.show()

def Z3():
	
	duration = 90
	fs = 1000
	samples = int(fs*duration)
	t = np.arange(samples) / fs
	signal = np.sin(2*np.pi*0.1*t)
	analytic_signal = hilbert(signal)
	plt.figure(4)
	plt.plot(t,np.real(analytic_signal),label='Real part')
	plt.plot(t,np.imag(analytic_signal),label='Imaginary part')
	plt.title('Część rzeczywista i urojona sygnału analitycznego')
	plt.grid(True)
	plt.legend()
	plt.show()
	
	plt.figure(5)
	plt.plot(np.imag(analytic_signal),np.real(analytic_signal))
	plt.grid(True)
	plt.title('Krzywa Lissajous')
	plt.show()

def Z4():
	
hn = Z1(15)
ampl_pha = Z2(hn,15)
Z3()
