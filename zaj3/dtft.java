public class dtft
{
    private final double CzęstotliwośćPoczątkowa;
    private final double CzęstotliwośćKońcowa;
    private final double KrokCzęstotliwości;
    private final int LiczbaPróbek;
    private final double CzęstotliwośćPróbkowania;
    
    
    public dtft(double początek, double koniec, double krok, double fs)
    {
        CzęstotliwośćPoczątkowa = początek;
        CzęstotliwośćKońcowa = koniec;
        KrokCzęstotliwości = krok;
        
        LiczbaPróbek = (int)((koniec - początek)/krok);
        
        CzęstotliwośćPróbkowania = fs;
        
    }//Koniec konstruktora
    
    private double pulsacja(double f)
    {
        double wynik;
        
        wynik = 2 * Math.PI * f;
        
        return wynik;
    }//Koniec obliczania pulsacji
    
    private complex ObliczPróbkęWidma(double f, double[] próbki)
    {
        int i;
        complex wynik;
        double a;
        double b;
        double omega;
        double ułamek;
        
        a = 0;
        b = 0;
        omega = pulsacja(f);
        
        for(i = 0; i < próbki.length; i++)
        {
            ułamek = (omega * (double)i)/CzęstotliwośćPróbkowania;
            
            a += próbki[i] * Math.cos(ułamek);
            b -= próbki[i] * Math.sin(ułamek);
        }//next i
        
        a = a/(double)próbki.length;
        b = b/(double)próbki.length;
        
        wynik = new complex(a,b);
        
        return wynik;
        
    }//Koniec obliczania pojedynczej próbki widma
    
    
    public widmo[] ObliczDTFT(double[] próbki)
    {
        widmo[] tablica;
        int i;
        double f;
        complex pojedynczy;
        double a;
        double b;
        
        tablica = new widmo[LiczbaPróbek];
        
        for(i = 0; i < LiczbaPróbek; i++)
        {
            f = CzęstotliwośćPoczątkowa + (KrokCzęstotliwości * ((double)i));
            
            pojedynczy = ObliczPróbkęWidma(f, próbki);
            
            a = pojedynczy.getA();
            b = pojedynczy.getB();
            
            tablica[i] = new widmo(a, b, f);
            
        }//next i
        
        return tablica;
        
    }//Koniec obliczania widma
    
}//Koniec klasy
