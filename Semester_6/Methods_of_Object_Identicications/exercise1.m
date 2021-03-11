%% Pierwszy program Mis
% Generacja liczb o rozkladzie normalnym
%
%Autor: S.Serafin
%Data modyfikacji: 3.11.2021

%%Głowna czesc programu
clear all; close all; clc;

N = 20000;
myData = randn(1,N);
meanVal = mean(myData)
stdVal = std(myData)
r1 = sum((myData(:)>=-1 & myData(:)<=1))
r2 = sum((myData(:)>=-2 & myData(:)<=2))

percent1 = r1/N*100
percent1 = r2/N*100

figure(1)
histogram(myData)
legend("My data")
title("Histogram")
ylabel("Ilosc wystapien")
xlabel("Wartosc wylosowana")

newVal = myData.^2;
figure(2)
subplot(2,1,1)
histogram(myData)
title('x')
subplot(2,1,2)
histogram(newVal)
title('x^2');