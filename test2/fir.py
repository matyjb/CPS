#Przykład implementacji FIR jako klasy


class systemFIR:
    
    def __init__(self,wspolczynniki):
        self.wspolczynniki = wspolczynniki
        self.dane = []
        
        for i in range(len(wspolczynniki)):
            self.dane.append(0)
    
    
    def MnozISumuj(self):
        
        suma = 0
        
        for i in range(len(self.wspolczynniki)):
            a = self.wspolczynniki[i]
            x = self.dane[i]
            suma += (a * x)
        
        return suma
    
    def WpiszNowa(self,x):
        
        indeks = len(self.wspolczynniki) - 1
        
        for i in range(len(self.wspolczynniki)):
            if(i < len(self.wspolczynniki)):
                self.dane[indeks] = self.dane[indeks - 1]
                indeks -= 1
                
        self.dane[0] = x
    
    
    def Wylicz(self,x):
        
        self.WpiszNowa(x)
        wynik = self.MnozISumuj()
        
        return wynik
    

