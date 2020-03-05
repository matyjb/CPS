import math;
import sys;
import matplotlib.pyplot as plt
import numpy as np 

delay = float(sys.argv[1])
freq = float(sys.argv[2])
lvl0 = float(sys.argv[3])
lvl1 = float(sys.argv[4])
samples = float(sys.argv[5])
# samples = 44100; #per second

#help values
y1StartIndex = math.floor(samples*delay)
lenght = delay + 1

x = np.linspace(0 , lenght, samples*lenght)
y0 = lvl0 * np.sin(x*freq)
y1 = lvl1 * np.sin((x+delay)*freq)
#sygnał opozniony nie istnieje az do momentu opoznienia
#(=0 by dało sie dodać do wynikowego)
#przy plotowaniu te zera są ucinane tej tablicy
y1[:y1StartIndex] = 0
# suma sygnałów
y2 = y0 + y1

fig, (ax, ax_table) = plt.subplots(nrows=2,figsize=(12,8), gridspec_kw=dict(height_ratios=[7,1])) #)
ax_table.axis("off")

ax.plot(x,y0, "-b", label="wejściowy")
#przycinanie sygnału opoznionego (bo nie itnieje aż do momentu opoznienia)
ax.plot(x[y1StartIndex:],y1[y1StartIndex:], "-r", label="opóźniony")
ax.plot(x,y2, "-g", label="wynikowy")
ax.legend(loc="upper left")
ax.set_xlim(0,lenght)
ax.set_xlabel("czas [s]")

cellText=[[delay, freq, lvl0, lvl1, samples]]
colLabels=['opóźnienie [s]','częstotliwość [Hz]','poziom wejściowy', 'poziom opóźnienia', 'ilość próbek na sekunde']
ax_table.table(colLabels=colLabels,cellText=cellText)

plt.show()