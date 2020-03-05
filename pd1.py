import math;
import sys;
import matplotlib.pyplot as plt
import numpy as np 

# delay = float(input("Podaj opóznienie w sekundach: "))
# freq = float(input("Podaj częstotliwość w hz: "))
# lvl0 = float(input("Podaj poziom sygnalu: "))
# lvl1 = float(input("Podaj poziom sygnalu opóźnionego: "))
# samples = float(input("Podaj ilosc probek na okres: "))
delay = float(sys.argv[1])
freq = float(sys.argv[2])
lvl0 = float(sys.argv[3])
lvl1 = float(sys.argv[4])
samples = float(sys.argv[5])
# samples = 44100; #per second

lenght = delay + 1

x = np.linspace(0 , lenght, samples*lenght)
y = np.sin(x*freq)

x0 = x.copy()
y0 = lvl0*y

x1 = x+delay
y1 = lvl1*y

z = y0.copy()
for i in range(math.floor(len(y1)-samples*delay)):
  z[math.floor(samples*delay) + i] += y1[i]


plt.plot(x0,y0, "-b", label="wejściowy")
plt.plot(x1,y1, "-r", label="opóźniony")
plt.plot(x0,z, "-g", label="wynikowy")
plt.legend(loc="upper left")
plt.xlim(0,lenght)
plt.show()