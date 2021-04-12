import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_default():
	my_data = pd.read_csv(r"C:\Users\margo\Dysk Google\Semestr_6\MIS\Projekt\OBIEKT.DAT",
	sep='\s+',names=['Time','Temperature'])
	plt.figure(1)
	plt.style.use('fivethirtyeight')
	plt.plot(my_data['Time'],my_data['Temperature'],linewidth=2)
	plt.xlabel('Time')
	plt.ylabel('Temperature [$\circ$C]')
	plt.show()
	plt.tight_layout()
	return my_data

def predict(V=0.09,z=26,D=0.12,Tp=0.032,tau=0.1,tr=420):
	T = []
	t = np.arange(1,tr+1,tau)
	for n in t:
		K = z/(2*(np.pi*D*n**3)**0.5)*np.exp((-z**2/(4*D*n))-(n*V**2/(4*D)))
		Tm = Tp+np.exp((V*z)/(2*D))*K
		T.append(Tm)
	T = np.asarray(T)
	plt.figure(2)
	plt.plot(t,T)
	plt.grid()
	plt.show()

predict()
