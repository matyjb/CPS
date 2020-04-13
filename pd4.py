# Napisz implementację transformaty DFT w wybranym przez siebie języku programowania.
# Kod przetestuj na różnych sygnałach.
# Można dopisać również rysowanie widma amplitudowego
# (za to można zdobyć ekstra 2 punkty, w zależności od jakości rysunku).

import math

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

  # @staticmethod
  # def okresowyProstokąt1(amplitude, ileOkresow, n):
  #   okres = int(n/ileOkresow/2)
  #   k = 0
  #   wartość = amplitude
  #   wynik = []

  #   for i in range(n):
  #     wynik.append(wartość)
      
  #     k+=1
      
  #     if(k == okres):
  #       if(wartość > 0):
  #         wartość = -amplitude
  #       else:
  #         wartość = amplitude
  #       k = 0
  #   return wynik
