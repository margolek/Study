import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from scipy.interpolate import *


def zad1():
	V = [3,7,12,15.4,20,23,27.4,30]
	n = [532,916,1342,1734,2189,2527,2945,3220]
	p1 = polyfit(V,n,1)
	plt.style.use('seaborn')
	plt.title('Charakterystyka prędkości obrotowej w funkcji napięcia')
	plt.ylabel('obrędkość obrotowa [obr/min]')
	plt.xlabel('Uac [V]')
	plt.plot(V,n,'.',label = 'Punkty pomiarowe')
	plt.plot(V,polyval(p1,V),label = 'Aproksymacja')
	plt.legend()
	plt.show()
def zad2():
	I42 = [11.23,11.36,11.82,12.09,12.79,13.28,14.5,16.97,19.52,25.07,39.14]
	I55 = [11.32,11.72,12.15,12.65,13.03,13.62,13.92,15.39,17.29,19.24,23.94]
	n1 = [1000,1001,999,995,997,1010,993,989,995,1021,959]
	n2 = [1105,1100,1094,1086,1080,1069,1065,1050,1024,997,940]
	p1 = polyfit(I42,n1,1)
	p2 = polyfit(I55,n2,1)
	plt.style.use('seaborn')
	plt.title('Charakterystyka zewnętrzna n = f(Idc)')
	plt.ylabel('Prędkość obrotowa [obr/min]')
	plt.xlabel('I [A]')
	plt.plot(I42,n1,'.',label = 'Punkty pomiarowe U = 42 [V]')
	plt.plot(I42,polyval(p1,I42),label = 'Aproksymacja')
	plt.plot(I55,n2,'.',label = 'Punkty pomiarowe U = 55 [V]')
	plt.plot(I55,polyval(p2,I55),label = 'Aproksymacja')
	plt.legend()
	plt.show()
def read():
	col_name = [
	'Time',
	'U_motor',
	'A_motor',
	'U_gen',
	'A_gen',
	'engine_speed',
	'Isk'
	]
	data1 = pd.read_csv(
	r'C:\Users\margo\Dysk Google\Semestr_5\EAA\EA11_EA12\EA11\dane_oraz_charakterystyki\pomiar1.csv',
	names = col_name)
	data2 = pd.read_csv(
	r'C:\Users\margo\Dysk Google\Semestr_5\EAA\EA11_EA12\EA11\dane_oraz_charakterystyki\pomiarobc_40A.csv',
	names = col_name)
	data3 = pd.read_csv(
	r'C:\Users\margo\Dysk Google\Semestr_5\EAA\EA11_EA12\EA11\dane_oraz_charakterystyki\r1r1dół.obciąznie,pomiar2.csv',
	names = col_name)
	data4 = pd.read_csv(
	r'C:\Users\margo\Dysk Google\Semestr_5\EAA\EA11_EA12\EA11\dane_oraz_charakterystyki\pomiar_n1.obciązęnia.csv',
	names = col_name)
	return data1,data2,data3,data4;
def voltage_motor():
	n_obc,obc,nth,nth2 = read()
	Un_mot = n_obc['U_motor']
	Un_mot_obc = obc['U_motor']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg napięć na silniku w stanie ustalonym')
	plt.plot(t,Un_mot,label = 'Bez obciążenia')
	plt.plot(t,Un_mot_obc,label= 'Z obciążeniem ~40 [A]')
	plt.xlabel('Czas [s]')
	plt.ylabel('Napięcie [V]')
	plt.xlim(0.400,0.460)
	plt.legend()
	plt.show()
def motor_speed_pernament():
	n_obc,obc,nth,nth2 = read()

	Isk = n_obc['engine_speed']
	Isk_obc = obc['engine_speed']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg prędości obrotowej silnika w stanie ustalonym')
	plt.plot(t,Isk,label = 'Bez obciążenia')
	plt.plot(t,Isk_obc,label= 'Z obciążeniem ~40 [A]')
	plt.xlabel('Czas [s]')
	plt.ylabel('Prędkość obrotowa*1000 [obr/min]')
	plt.xlim(0.1,0.14)
	plt.legend()
	plt.show()
def Isk_pernament():
	n_obc,obc,nth,nth2 = read()

	speed = n_obc['Isk']
	speed_obc = obc['Isk']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg skutecznej wartości prądu w stanie ustalonym')
	plt.plot(t,speed,label = 'Bez obciążenia')
	plt.plot(t,speed_obc,label= 'Z obciążeniem ~40 [A]')
	plt.xlabel('Czas [s]')
	plt.ylabel('Prąd*10 [A]')
	plt.xlim(0.1,0.14)
	plt.legend()
	plt.show()
def current_motor():
	n_obc,obc,nth,nth2 = read()
	Un_mot = n_obc['A_motor']
	Un_mot_obc = obc['A_motor']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg prądów silnika w stanie ustalonym')
	plt.plot(t,Un_mot,label = 'Bez obciążenia')
	plt.plot(t,Un_mot_obc,label= 'Z obciążeniem ~40 [A]')
	plt.xlabel('Czas [s]')
	plt.ylabel('Prąd [A]')
	plt.xlim(0.400,0.460)
	plt.legend()
	plt.show()
def voltage_gen():
	n_obc,obc,nth,nth2 = read()
	Un_mot = n_obc['U_gen']
	Un_mot_obc = obc['U_gen']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg napięć na prądnicy obciążenia w stanie ustalonym')
	plt.plot(t,Un_mot,label = 'Bez obciążenia')
	plt.plot(t,Un_mot_obc,label= 'Z obciążeniem ~40 [A]')
	plt.xlabel('Czas [s]')
	plt.ylabel('Napięcie [V]')
	plt.xlim(0.400,0.460)
	plt.legend()
	plt.show()
def current_gen():
	n_obc,obc,nth,nth2 = read()
	Un_mot = n_obc['A_gen']
	Un_mot_obc = obc['A_gen']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg prądów prądnicy w stanie ustalonym')
	plt.plot(t,Un_mot,label = 'Bez obciążenia')
	plt.plot(t,Un_mot_obc,label= 'Z obciążeniem ~40 [A]')
	plt.xlabel('Czas [s]')
	plt.ylabel('Prąd [A]')
	plt.xlim(0.400,0.460)
	plt.legend()
	plt.show()
def current_temporary_motor():
	n_obc,obc,temp,temp1 = read()
	A_mot = temp1['A_motor']
	A_mot_obc = temp['A_motor']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg prądów silnika w odpowiedzi na stan przejściowy')
	plt.plot(t,A_mot_obc,label='Tryb regulacji napięcia')
	plt.plot(t,A_mot,label = 'Tryb regulacji prędkości')
	plt.xlabel('Czas [s]')
	plt.ylabel('Prąd [A]')
	plt.xlim(0.1,0.5)
	plt.legend()
	plt.show()
def voltage_temporary_motor():
	n_obc,obc,temp,temp1 = read()
	U_mot = temp1['U_motor']
	U_mot_obc = temp['U_motor']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg napięć na silniku w odpowiedzi na stan przejściowy')
	plt.plot(t,U_mot_obc,label='Tryb regulacji napięcia')
	plt.plot(t,U_mot,label = 'Tryb regulacji prędkości')
	plt.xlabel('Czas [s]')
	plt.ylabel('Napięcie [V]')
	plt.xlim(0.1,0.12)
	plt.legend()
	plt.show()
def current_temporary_gen():
	n_obc,obc,temp,temp1 = read()
	A_gen = temp1['A_gen']
	A_gen_obc = temp['A_gen']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg prądów generatora w odpowiedzi na stan przejściowy')
	plt.plot(t,A_gen_obc,label='Tryb zadawania napięcia')
	plt.plot(t,A_gen,label = 'Trby zadawania prędkości')
	plt.xlabel('Czas [s]')
	plt.ylabel('Prąd [A]')
	plt.xlim(0.1,0.5)
	plt.legend()
	plt.show()
def voltage_temporary_gen():
	n_obc,obc,temp,temp1 = read()
	U_gen = temp1['U_gen']
	U_gen_obc = temp['U_gen']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg napięć na generatorze w odpowiedzi na stan przejściowy')
	plt.plot(t,U_gen_obc,label='Tryb zadawania napięcia')
	plt.plot(t,U_gen,label = 'Tryb zadawania prędkości')
	plt.xlabel('Czas [s]')
	plt.ylabel('Napięcie [V]')
	plt.xlim(0.1,0.5)
	plt.legend()
	plt.show()
def Isk_temporary():
	n_obc,obc,temp,temp1 = read()
	I = temp1['Isk']
	I_obc = temp['Isk']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg wartości skutecznej prądu w stanie przejściowym')
	plt.plot(t,I,label='Trby zadawania napięcia')
	plt.plot(t,I_obc,label = 'Trby zadawania prędkości')
	plt.xlabel('Czas [s]')
	plt.ylabel('Prąd*10 [A]')
	#plt.xlim(0.1,0.5)
	plt.legend()
	plt.show()
def motor_speed_temporary():
	n_obc,obc,temp,temp1 = read()
	I = temp1['engine_speed']
	I_obc = temp['engine_speed']
	t = n_obc['Time']
	plt.figure(1)
	plt.style.use('seaborn')
	plt.title('Przebieg prędkości obrotowej w stanie przejściowym')
	plt.plot(t,I,label='Tryb zadawania napięcia')
	plt.plot(t,I_obc,label = 'Tryb zadawania prędkości')
	plt.xlabel('Czas [s]')
	plt.ylabel('Prędkość obrotowa*1000 [obr/min]')
	plt.legend()
	plt.show()

Isk_pernament()