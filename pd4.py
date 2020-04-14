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

def mirror(arr):
  # łączenie tablicy odwróconej z oryginalną (bez powtarzania arr[0])
  return [arr[-i] for i in range(1,len(arr))] + arr

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
  ax2.plot(x1, y1, color=c2)
  ax2.set_title('Widmo amplitudowe')
  ax2.set_ylabel('amplituda', color=c2)
  ax2.set_xlabel('freq [Hz]', color=c2)
  ax2.tick_params(axis='y', labelcolor=c2)
  ax2.grid(True, linestyle='--', linewidth=0.5)

  plt.show()

# czy odbijać wykres widma amplitudowego względem OY
isMirror = True

n = 600
Ts = 1 / 800.0
fstop = n*Ts
x = np.linspace(0,fstop,n)

# dwa sygnały dla rozrywki
s1 = Sygnal.sinus(50.0,1.0,Ts,n)
s2 = Sygnal.sinus(80.0,0.5,Ts,n)
# s1 = Sygnal.prostokat(0.05,2,Ts,n)
# s2 = Sygnal.prostokat(0.35,3,Ts,n)
# s1 = Sygnal.okresowyProstokąt2(2,3,n)
# s2 = Sygnal.okresowyProstokąt2(3,7,n)
# s1 = Sygnal.spadekWykładniczy(2,3,Ts,n)
# s2 = Sygnal.spadekWykładniczy(5,7,Ts,n)

# suma sygnałów
s = np.array(s1) + np.array(s2)

yf = dft(s)
# obliczanie widma
yf = 2.0/n * np.abs(yf[:n//2])

# rysowanie
if(isMirror):
  xf = np.linspace(-1.0/(2.0*Ts), 1.0/(2.0*Ts), n-1)
  draw(x,s,xf,mirror(yf.tolist()))
else:
  xf = np.linspace(0, 1.0/(2.0*Ts), n/2)
  draw(x,s,xf,yf)
