import matplotlib.pyplot as plt

class FIR:
  def __init__(self, wsp):
    self.wsp = wsp
    self.data = [0 for i in range(len(wsp))]

  def MulAndSum(self):
    return sum([self.wsp[i]*self.data[i] for i in range(len(self.wsp))])
  
  def Append(self, x):
    self.data = [x] + self.data
    self.data = self.data[:-1]

  def Wylicz(self, x):
    self.Append(x)
    return self.MulAndSum()

class IIR:
  def __init__(self, wspA, wspB):
    self.firA = FIR(wspA)
    self.firB = FIR(wspB)
    self.lastY = 0

  def Wylicz(self, x):
    a = self.firA.Wylicz(x)
    y = a + self.lastY
    self.lastY = self.firB.Wylicz(y)
    return y

# przyklad z wikipedii
# wspA = [0.5]
# wspB = [0.5]
# f = IIR(wspA, wspB)
# s_in = [24, 27, 31, 59, 33, 37]
# s_out = [f.Wylicz(s_in[i]) for i in range(len(s_in))] + [f.Wylicz(0) for i in range(15)] 
# plt.plot(range(len(s_in)), s_in, 'b.-', label='sygnał wejściowy')
# plt.plot(range(len(s_out)), s_out, 'r.-', label="sygnał wyjściowy")
# plt.legend()
# plt.xlabel("próbki")
# plt.ylabel("wartość sygnału")
# plt.show()

s_in = [24, 27, 31, 59, 33, 37]

wspA1 = [0.8, 0.4, 0.2]
wspB1 = [0.1, 0.3, 0.05]
f1 = IIR(wspA1, wspB1)
s_out1 = [f1.Wylicz(s_in[i]) for i in range(len(s_in))] + [f1.Wylicz(0) for i in range(15)] 

wspA2 = [1, 0.5, 2]
wspB2 = [0.5, 1, 1.5]
f2 = IIR(wspA2, wspB2)
s_out2 = [f2.Wylicz(s_in[i]) for i in range(len(s_in))] + [f2.Wylicz(0) for i in range(15)] 

#plot
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(14,6))

ax1.plot(range(len(s_in)), s_in, 'b.-', label='sygnał wejściowy')
ax1.plot(range(len(s_out1)), s_out1, 'r.-', label="sygnał wyjściowy")
ax1.legend()
ax1.set_xlabel("próbka")
ax1.set_ylabel("wartość sygnału")

ax2.plot(range(len(s_in)), s_in, 'b.-', label='sygnał wejściowy')
ax2.plot(range(len(s_out2)), s_out2, 'r.-', label="sygnał wyjściowy")
ax2.legend()
ax2.set_xlabel("próbka")
ax2.set_ylabel("wartość sygnału")

plt.show()
# przykład 2 jest niestabilny