import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def square_signal(N=100,c=50,b=20):
	"""
	 Napisać skrypt imp_prost.m generujący impuls prostokątny o czasie trwania N, przesunięciu c,
	 szerokości b. Wielkości te wyrażone są liczbą próbek (przykładowo N=100, c=50, b=20)
	"""
	part1 = np.zeros(c)
	part2 = np.ones(b)
	part3 = np.zeros(N-(c+b))
	sqr = np.concatenate((part1,part2,part3),axis=0)
	plt.plot(np.arange(0,N),sqr)
	plt.grid()
	plt.show()

def generate_sinus_discrete_by_time(Td=1,f=10,fp=100):
	"""
	Napisać skrypt sinus1.m generujący sygnał sinusoidalnie zmienny o częstotliwości f [Hz], czasie
	trwania Td [s], częstotliwości próbkowania fp [Hz]. Na okoliczność testów przyjąć: f=10Hz,
	p=100Hz, Td=1s
	"""
	t = np.linspace(0,1,fp)
	sinwave=np.sin(2*np.pi*f*t)
	plt.figure(1)
	plt.plot(t,sinwave)
	plt.show()

def generate_sinus_discrete_by_sample(f=10,fp=100,N=100):
	"""
	Napisać skrypt sinus2.m generujący sygnał sinusoidalnie zmienny o częstotliwości f [Hz], czasie
	trwania wyrażonym liczbą próbek N, częstotliwości próbkowania fp [Hz]. Na okoliczność testów
	przyjąć: f=10Hz, fp=100Hz, N=200.
	"""
	t = np.linspace(0,2,200) #method 1
	t1 = np.arange(0,N)*(1/fp) #method 2
	sinwave = np.sin(2*np.pi*f*t1)
	print(f'suma 13 pierwszych próbek wynosi{np.sum(sinwave[:13])}')
	print(np.var(sinwave))
	plt.plot(t1,sinwave)
	plt.grid()
	plt.show()

generate_sinus_discrete_by_sample()
def sinus_liniowo_narastajaca_czestotliwosc(N=200,f0=50,fp=10000,fi0=0):
	pass
