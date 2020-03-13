class FIR:
  def __init__(self, wsp):
    self.wsp = wsp
    self.data = [0 for i in range(len(wsp))]

  def MulAndSum(self):
    return sum([self.wsp[i]*self.data[i] for i in range(len(self.wsp))])
  
  def Append(self, x):
    self.data = [x] + self.data

  def Wylicz(self, x):
    self.Append(x)
    return self.MulAndSum()

wsp = [8,4,2,1]
f = FIR(wsp)
s_in = [1,0,0,0,0,0,0,0]
s_out = [f.Wylicz(s_in[i]) for i in range(len(s_in))]

for i in range(len(s_out)):
  print("Odpowiedź FIR ["+str(i)+"] = "+ str(s_out[i]))