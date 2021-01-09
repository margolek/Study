import matplotlib.pyplot as plt
import numpy as np


def current_characteristic(Uf,R1,R21,X1,X21,RL,XL):
	s = np.linspace(start=0.001,stop=1,num=1000)
	formula = np.array([])
	for n in s:
		func = Uf/(np.sqrt((RL+R1+R21/n)**2+(2*np.pi*50*X1+2*np.pi*50*X21+2*np.pi*50*XL)**2))
		formula = np.append(formula, func)
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Charakterystyka prądu silnika w funkcji poślizgu')
	plt.xlabel('$s$')
	plt.ylabel('$I$ [A]')
	plt.plot(s,formula)
	plt.show()
	return formula


a = current_characteristic(320,0.5,0.5,0.00035,0.0055,0.01,0.00001)
print(a)

