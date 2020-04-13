# Napisz implementację transformaty DFT w wybranym przez siebie języku programowania.
# Kod przetestuj na różnych sygnałach.
# Można dopisać również rysowanie widma amplitudowego
# (za to można zdobyć ekstra 2 punkty, w zależności od jakości rysunku).

import math, numpy as np, matplotlib.pyplot as plt

class Sygnal:
  @staticmethod
  def sinus(freq, amplitude, fs, n):
    omega = 2 * math.pi * freq
    Ts = 1 / fs
    return [amplitude * math.sin(omega * Ts * i) for i in range(n)]

  @staticmethod
  def prostokat(duration, amplitude, fs, n):
    Ts = 1 / fs
    return [amplitude if Ts * i < duration / 2 else 0 for i in range(n)]
  
  @staticmethod
  def spadekWykładniczy(wspolczynnik, amplitude, fs, n):
    Ts = 1 / fs
    return [amplitude * math.exp(-wspolczynnik * Ts * i) for i in range(n)]

  @staticmethod
  def okresowyProstokąt2(amplitude, ileOkresow, n):
    okres = int(n/ileOkresow/2)
    return [-amplitude if int(i / okres) % 2 != 0 else amplitude for i in range(n)]

def dft(p):
  N = len(p)
  # return [np.sum([probki[n] * np.exp((-2*k*math.pi*n)/N * 1j) for n in range(N)]) for k in range(N)]
  wynik = []
  for k in range(N):
    xk = []
    for m in range(N):
      xk.append(p[m]*np.exp(1j*(-2*math.pi*m*k/N)))
    wynik.append(np.sum(xk))
  return wynik
    

# sinus(freq, amplitude, fs, n)
out = dft(Sygnal.sinus(20, 2, 1000, 50))
out = [np.absolute(i) for i in out] # absolute(real+imaginary) = moduł
plt.plot(range(len(out)),out)
plt.yscale('log')
plt.show()
# print(out)