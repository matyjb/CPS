/**
 * Klasa służąca do przechowywania liczb zespolonych
 */
public class complex
{
    private final double a;
    private final double b;
    
    private double moduł;
    private double faza;
    
    
    public complex(double a, double b)
    {
        this.a = a;
        this.b = b;
        
        faza = 0;
        
        ObliczModuł();
        ObliczFazę();
    }//Koniec konstruktora
    
    private void ObliczModuł()
    {
        moduł = Math.sqrt((a*a) + (b*b));
    }//Koniec obliczania modułu;
    
    private void ObliczFazę()
    {
        if(a == 0 && b == 0)
        {
            faza = 0;
        }else if(a == 0 && b > 0)
        {
            faza = Math.PI/2;
        }else if(a == 0 && b < 0)
        {
            faza = 3 * Math.PI/2;
        }else if(a != 0 && b == 0)
        {
            faza = 0;
        }else if(a > 0 && b != 0)
        {
            faza = Math.atan(b/a);
        }else if(a < 0 && b != 0)
        {
            faza = Math.atan(b/a) + Math.PI;
        }//end if
    }//Koniec obliczania fazy
    
    public double getA()
    {
        return a;
    }
    
    public double getB()
    {
        return b;
    }
    
    public double getModuł()
    {
        return moduł;
    }
    
    public double getFazę()
    {
        return faza;
    }
    
}//Koniec klasy
