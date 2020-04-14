# Napisz implementację transformaty DFT w wybranym przez siebie języku programowania.
# Kod przetestuj na różnych sygnałach.
# Można dopisać również rysowanie widma amplitudowego
# (za to można zdobyć ekstra 2 punkty, w zależności od jakości rysunku).

import math, numpy as np, matplotlib.pyplot as plt

class Sygnal:
  @staticmethod
  def sinus(freq, amplitude, Ts, n):
    omega = 2 * math.pi * freq
    return [amplitude * np.sin(omega * Ts * i) for i in range(n)]

  @staticmethod
  def prostokat(duration, amplitude, Ts, n):
    return [amplitude if Ts * i < duration / 2 else 0 for i in range(n)]
  
  @staticmethod
  def spadekWykładniczy(wspolczynnik, amplitude, Ts, n):
    return [amplitude * math.exp(-wspolczynnik * Ts * i) for i in range(n)]

  @staticmethod
  def okresowyProstokąt2(amplitude, ileOkresow, n):
    okres = int(n/ileOkresow/2)
    return [-amplitude if int(i / okres) % 2 != 0 else amplitude for i in range(n)]

def dft(p):
  N = len(p)
  return [np.sum([p[n] * np.exp((-2*k*math.pi*n)/N * 1j) for n in range(N)]) for k in range(N)]
  # wynik = []
  # for k in range(N):
  #   xk = []
  #   for m in range(N):
  #     xk.append(p[m]*np.exp(1j*(-2*math.pi*m*k/N)))
  #   wynik.append(np.sum(xk))
  # return wynik

def mirror(array):
  return [array[-i] for i in range(1,len(array))] + array

def draw(x0, y0, x1, y1):
  fig, (ax1,ax2) = plt.subplots(ncols=2,figsize=(17,6))
  c1 = 'tab:blue'
  ax1.plot(x0,y0, color=c1)
  ax1.set_title('sygnał')
  ax1.set_ylabel('amplituda', color=c1)
  ax1.set_xlabel('czas [s]', color=c1)
  ax1.tick_params(axis='y', labelcolor=c1)
  ax1.grid(True, linestyle='--', linewidth=0.5)

  c2 = 'tab:red'
  # ax2.set_yscale('log')
  ax2.plot(x1, y1, color=c2)
  ax2.set_title('DFT')
  ax2.set_ylabel('amplituda', color=c2)
  ax2.set_xlabel('freq [Hz]', color=c2)
  ax2.tick_params(axis='y', labelcolor=c2)
  ax2.grid(True, linestyle='--', linewidth=0.5)

  plt.show()

### ze stack overflow
# N = 600
# # sample spacing
# T = 1.0 / 800.0
# x = np.linspace(0.0, N*T, N)
# # print(x)
# y = Sygnal.okresowyProstokąt2(2,3,N)
# yf = dft(y)
# xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
# fig, ax = plt.subplots()
# ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
# plt.show()

n = 600
Ts = 1 / 800.0
fstop = n*Ts
x = np.linspace(0,fstop,n)
sygnal1 = Sygnal.sinus(50.0,1.0,Ts,n)
sygnal2 = Sygnal.sinus(80.0,0.5,Ts,n)
# sygnal1 = Sygnal.prostokat(0.05,2,Ts,n)
# sygnal2 = Sygnal.prostokat(0.35,3,Ts,n)
# sygnal1 = Sygnal.okresowyProstokąt2(2,3,n)
# sygnal2 = Sygnal.okresowyProstokąt2(3,7,n)
# sygnal1 = Sygnal.spadekWykładniczy(2,3,Ts,n)
# sygnal2 = Sygnal.spadekWykładniczy(5,7,Ts,n)


sygnal = np.array(sygnal1) + np.array(sygnal2)

yf = dft(sygnal)
xf = np.linspace(0, 1.0/(2.0*Ts), n/2)

yf = 2.0/n * np.abs(yf[:n//2])

draw(x,sygnal,xf,yf)