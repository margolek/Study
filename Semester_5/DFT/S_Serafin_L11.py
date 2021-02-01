from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def Z1():

	wc = 25
	w = np.linspace(0,100,1000)
	n = [3,4,8]
	for i in n:
		Gw = 1/np.sqrt(1+((1j*w)/(1j*wc))**(2*i))
		plt.figure(1)
		plt.grid()
		plt.plot(w,Gw,label='n = {}'.format(i))
	plt.xlabel('$\omega$')
	plt.ylabel('$G(\omega)$')
	plt.legend()
	plt.show()
Z1()
def Z2(w3,n):
	#Krok 1
	wc = 2*np.tan(w3/2)
	poles = np.array([])
	#Krok 2
	for k in range(0,n):
		sk = wc*(np.exp(1j*np.pi*(1+2*k)/(2*n)))*np.exp(1j*np.pi/2)
		poles = np.append(poles,sk)
		plt.figure(2)
		plt.plot(np.real(sk),np.imag(sk),marker = 'x')
	plt.title('Położenie biegunów filtru analogowego')
	plt.xlabel('Real part')
	plt.ylabel('Imaginary part')
	plt.show()

	#Krok 3
	G0_num,G0_den = 1,1
	for k in range(0,n):
		G0_num = G0_num*(-poles[k]) 
		G0_den = G0_den*(2-poles[k]) 
	G0 = G0_num/G0_den
	poles_digital = (2+poles)/(2-poles)
	for n in poles_digital:
		plt.figure(3)
		plt.scatter(np.real(poles_digital),np.imag(poles_digital),marker='x')
	plt.xlim((-1.5,1.5))
	plt.title('Położenie zer oraz biegunów filtru cyfrowego')
	plt.ylabel('Imaginary part')
	plt.xlabel('Real part')
	plt.plot(-1,0,marker = 'o')
	plt.show()

	#Krok 4
	w,h = signal.freqz_zpk([-1,-1,-1], poles_digital, G0)
	fig = plt.figure(4)
	plt.title('Digital filter frequency response')
	plt.plot(w, (abs(h)), 'b')
	plt.xlabel('Frequency [rad/s]')
	plt.grid()
	plt.show()

Z2(0.8*np.pi, 3)