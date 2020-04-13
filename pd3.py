import matplotlib.pyplot as plt
import math

def modulFk(a, w):
  ww = 2*math.pi*w
  mian = math.pow(a,2)+ math.pow(ww,2)
  z2 = math.pow(a/mian,2) + math.pow(-ww/mian,2)
  return math.sqrt(z2)

f = list(range(1,10000))

y1 = [modulFk(1,i) for i in f]
y2 = [modulFk(10,i) for i in f]
y3 = [modulFk(30,i) for i in f]

plt.plot(f,y1, label='a = 1')
plt.plot(f,y2, label='a = 10')
plt.plot(f,y3, label='a = 30')
plt.xscale('log')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Moduł F")
plt.legend()
plt.show()