import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import *



def read():
	col_name = [
	'Time',
	'U(N)_motor',
	'A(P)_motor',
	'U(N)_gen',
	'A(P)_gen',
	'Isk',
	'engine_speed'
	]
	data1 = pd.read_csv(
	r'C:\Users\margo\Dysk Google\Semestr_5\EAA\EA11_EA12\EA11\dane_oraz_charakterystyki\pomiar1.csv',
	names = col_name)
	return data1

def plot_figure():
	a = read()
	Un_mot = a['U(N)_motor']
	t = a['Time']
	plt.figure(1)
	plt.scatter(t,Un_mot,marker = '.')
	p1 = polyfit(t,Un_mot,2)
	plt.plot(t,polyval(p1,t))
	plt.show()


plot_figure()