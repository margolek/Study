import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def generowanie_sygnałow():
	"""
	1. Dla sygnałów:
	a) impuls prostokątny wsp. wypełnienia 50%,
	b) fragment sygnał sinusoidalnie zmiennego: sin(2π 0.1n),
	c) szum o rozkładzie gaussowskim (randn),
	wyznaczyć (korzystając z podanych poniżej definicji) następujące parametry sygnałów:
	wartość średnia, energia, moc średnia,wariancja, odchylenie standardowe.
	Uzyskane wartości porównać z wartościami zwracanymi przez
	funkcje Matlab'a. Przyjąć długość sygnału N=1000, indeks próbki sygnału n=0,1,...,N-1.
	"""
	N = 1000
	t = np.arange(0,N)
	sqr = signal.square(t,duty=0.5)
	sqr_mean = np.sum(sqr)/N
	sqr_energy = np.sum(np.abs(sqr)**2)
	sqr_energy_mean = sqr_energy/N
	sqr_var = np.sum((sqr-sqr_mean)**2)/(N-1)
	sqr_std = sqr_var**(1/2)
	print('Dla sygnału prostokątnego')
	print('wartość średnia: {}, energia: {}, moc: {}, wariancja: {}, odchylenie standardowe: {}'.format(sqr_mean,
	sqr_energy,sqr_energy_mean,sqr_var,sqr_std))
	print()

	sinwave = np.sin(2*np.pi*0.1*t)
	sinwave_mean = np.sum(sinwave)/N
	sinwave_energy = np.sum(np.abs(sinwave)**2)
	sinwave_energy_mean = sinwave_energy/N
	sinwave_var = np.sum((sinwave-sinwave_mean)**2)/(N-1)
	sinwave_std = sinwave_var**(1/2)
	print('Dla sygnału sinusoidalnego')
	print('wartość średnia: {}, energia: {}, moc: {}, wariancja: {}, odchylenie standardowe: {}'.format(sinwave_mean,
	sinwave_energy,sinwave_energy_mean,sinwave_var,sinwave_std))
	print()
	
	random = np.random.normal(size=N)
	random_mean = np.sum(random)/N
	random_energy = np.sum(np.abs(random)**2)
	random_energy_mean = random_energy/N
	random_var = np.sum((random-random_mean)**2)/(N-1)
	random_std = random_var**(1/2)
	print('Dla szumu o rozkładzie gausowskim')
	print('wartość średnia: {}, energia: {}, moc: {}, wariancja: {}, odchylenie standardowe: {}'.format(random_mean,
	random_energy,random_energy_mean,random_var,random_std))
	print()
def autokorelacja():
	"""
	2. Dla następujących sygnałów dyskretnych:
	a) impuls (jak na rysunku) o czasie trwania N=10 próbek,
	b) x=[1,2,3,0,0]; y=[4,1,1,0,0],
	c) szumu o rozkładzie normalnym, N=100 próbek z generatora randn,
	d) x1(t) = sin(2*pi*5*t), x2(t) = sin(2*pi*5*t) + 0.5sin(2*pi*10*t) + 0.25sin(2*pi*30t), dla 0<t<1 [s]
	"""
	N = 10
	t = np.arange(-20,20)
	t1 = np.arange(-10,11)

	part1 = np.zeros(20)
	part2 = np.ones(10)
	part3 = np.zeros(10)
	sqr = np.concatenate((part1,part2,part3),axis=0)
	sqr_acorr = np.correlate(sqr, sqr,mode='same')
	print(f'Macierz autokorelacji sygnału prostokątnego: {sqr_acorr}')
	
	
	plt.figure(1)
	plt.stem(t,sqr)
	plt.grid()
	plt.plot(t,sqr_acorr)
	#plt.show()

	#b)
	x = np.array([1,2,3,0,0])
	y = np.array([4,1,1,0,0])
	x_corr = np.correlate(x, x,mode='same')
	y_corr = np.correlate(y, y,mode='same')
	print(f'Autokorelacja x wynosi: {x_corr}')
	print(f'Autokorelacja y wynosi: {y_corr}')

	#c)
	N = 100
	t1 = np.arange(0,N)
	t2 = np.arange(-N,N-1)
	random = np.random.normal(size=N)
	random_corr = np.correlate(random, random,mode='full')
	plt.figure(2)
	plt.plot(t2,random_corr)
	plt.grid()
	plt.plot(t1,random)
	plt.show()

	#d)
	N = 50
	t1 = np.arange(0,N)
	t2 = np.arange(-N,N-1)
	sinwave = np.sin(2*np.pi*0.1*t1)
	sinwave_acorr = np.correlate(sinwave, sinwave,mode='full')
	plt.figure(3)
	plt.plot(t1,sinwave)
	plt.plot(t2,sinwave_acorr)
	plt.grid()
	plt.show()


		
