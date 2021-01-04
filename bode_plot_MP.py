from scipy import signal
import matplotlib.pyplot as plt
import math
import cmath

sys = signal.TransferFunction([1], [6.17*0.00000001, 4*0.0001, 1])
w, mag, phase = signal.bode(sys)


def bode_plot():
	plt.figure(1)
	plt.style.use('seaborn')
	plt.semilogx(w, mag)
	plt.title('Uzyskana charakterystyka Body Plot')
	plt.ylabel('[dB]')
	plt.xlabel(r'$\omega$')
	plt.axvline(4000,label=r'$\omega_0$ = 4026 [Hz]', linewidth = 0.5)
	plt.axvline(1257,label=r'$\omega_1$ = 1257 [Hz]', linewidth = 0.5)
	plt.legend()
	plt.show()

def amplitude_value():
	K1 = 1/(6.17*0.00000001*(complex(0,4026))**2+4*0.0001*complex(0,4026)+1)
	K2 = 1/(6.17*0.00000001*(complex(0,1026))**2+4*0.0001*complex(0,1026)+1)
	gain1 = abs(K1)
	gain2 = abs(K2)
	return gain1,gain2

a,b = amplitude_value()
relative_error = ((b-a)/1)*100
print('Wartość amplitudy dla w1=1026 wynosi: {0:1.3f} natomiast dla w1=4026: {0:1.3f}'.format(b,a))
print('Względny błąd: {0:2.3f}%'.format(relative_error))

