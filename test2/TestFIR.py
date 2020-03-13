#Test układu FIR

import fir


wspolczynniki = []

wspolczynniki.append(8)
wspolczynniki.append(4)
wspolczynniki.append(2)
wspolczynniki.append(1)



sygnal_we = [1,0,0,0,0,0,0,0]
sygnal_wy = []


filtrFIR = fir.systemFIR(wspolczynniki)

for i in range(len(sygnal_we)):
    y = filtrFIR.Wylicz(sygnal_we[i])
    sygnal_wy.append(y)
    

for i in range(len(sygnal_wy)):
    
    print("Odpowiedz systemu FIR [" + str(i) + "] = " + str(sygnal_wy[i]))

