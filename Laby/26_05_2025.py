class Wektor(object):
    def __init__(self,x,y,z):
        if isinstance(x,(int,float)) and isinstance(y,(int,float))\
            and isinstance(z,(int,float)):
                self.__x = x
                self.__y= y
                self.__z = z
        else:
            print("Błedne dane!")
            exit(0)
            
    def __str__ (self):
        return f"[{self.__x},{self.__y},{self.__z}]"
    def dlugosc(self):
        return (self.__x**2+self.__y**2+self.__z**2)**0.5
    def pomnoz(self,a):
        return Wektor(a*self.__x,a*self.__y,a*self.__z)
    

v = Wektor(1,2,3)
z = v.pomnoz(3)
print(z)
                
class Czlowiek(object):
    def __init__(self,wiek,waga,wzrost):
        if(isinstance(wiek,int) and isinstance(waga,int) and isinstance(wzrost,int) and waga>0 and wzrost>0 ):
            self.__wiek = wiek
            self._wzrost = wzrost
            self.__waga = waga
            self.__sumaWzrostow += wzrost
            self.__sumaWag += waga
            
        else: 
            print("niepoprawne dane")
            return(0)
    def BMI(self):
        return round(self.__waga/(self.__wzrost/100)**2,2)
    def opis(self):
        if self.__wiek == 0:
            print("niemowlak")
        elif self.__wiek <=2:
            print("Poniemowlak")
        elif self.__wiek <5:
            print("Przedszkolak")
    @staticmethod 
    def SumaWzrostow():
        return Czlowiek.SumaWag
    def SumaWag():
        return Czlowiek.SumaWzrostow
    
'''Zadanie 4. Stwórz klasę dat rozumianych jako obiekty posiadające trzy publiczne atrybuty
(dzień, miesiąc, rok). Klasa powinna zawierać konstruktor, metodę str() oraz metodę
dosylwestra(), która odpowiada za obliczenie liczby dni do końca danego roku.
W konstruktorze zabezpieczyć moment tworzenia daty (ma być poprawna). W zadaniu nie
wykorzystujemy modułu datetime. '''
from sys import exit 
class Data(object):
    def __init__(self,dzien,miesiac,rok):
        self.__miesiace = [31,28,31,30,31,30,31,31,30,31,30,30]
        
        if(isinstance(rok,int) and rok>0 and rok%4==0 and ((rok%4==0 and rok%100!=0) or rok%400==0)):
            self.__miesiace[1]= 29
            self.rok = rok
        elif isinstance(rok,int) and rok>0:
            self.rok = rok
        else:
            print("Niepoprawny rok!")
            exit(0)
        if isinstance(miesiac,int) and miesiac>0 and miesiac <13 :
            self.miesiac = miesiac
        else:
            print("niepoprawn miesiac")
            exit(0)
        if(isinstance(dzien,int) and dzien>0 and dzien<=self.__miesiace[miesiac-1]):
            self.dzien=dzien
        else:
            print("niepoorawny dzien")
            exit(0)
    def __str__(self):
        return f"{self.dzien}.{self.miesiac}.{self.rok}"
    def dosylwestra(self):
        return sum(self.__miesiace)- sum(self.__miesiace[:self.miesiac-1]) - self.dzien
        
d = Data(12,9,2024)
print(d)
print(d.dosylwestra())
'''Zadanie 6. Stwórz klasę kwadratów rozumianych jako obiekty posiadające jeden atrybut
(długość boku kwadratu - atrybut ten może być publiczny lub chroniony). Klasa powinna
zawierać jednoparametryczny zabezpieczony konstruktor oraz metody pole() oraz obwod()
odpowiedzialne za obliczanie pola oraz obwodu kwadratu. Następnie napisać program
sprawdzający poprawność napisanej klasy. W dalszej kolejności utworzyć pochodną klasę
prostokątów, która zawiera dodatkowo drugi atrybut (długość drugiego boku prostokąta)
oraz zmienione metody: konstruktora, a także metody pole() i obwod(). W klasie pochodnej
zmodyfikować konstruktor i wspomniane metody, używając słowa kluczowego super(). '''
class Kwadrat(object):
    def __init__(self,a):
        if(isinstance(a,int) or isinstance(a,float)):
            self.a = a
            
    def  Pole(self):
        return self.a**2
    def Obwod(self):
        return self.a*4
class Prostokat(Kwadrat):
    def __init__(self,a,b):
        super().__init__(a)
        if isinstance(b,(int,float)) and b>0:
            self.__b=b
        else:
            print("niepprawne dane")
            exit(0)
    def Pole(self):
        return super().Pole()/self.a*self.__b
    def Obwod(self):
        return super().Obwod()/2+2*self.__b
    
'''Zadanie 8. Zdefiniuj klasę PracownikKolei, która zawiera trójparametryczny konstruktor
(imię i nazwisko pracownika oraz jego stanowisko) oraz metodę __str__, a następnie klasę
IC, która zawiera konstruktor bezparametryczny, lecz w jego ciele definiuje dodatkowe pole
zawierające listę pracowników (początkowo pustą) oraz metodę przyjmij(p), która dodaje
pracownika p do tej listy, a także metodę str() odpowiedzialną za wyświetlenie wszystkich
pracowników. Następnie w programie głównym stworzyć kilku pracowników, zatrudnić ich
w firmie IC i wyświetlić dane wszystkich pracowników oraz stworzyć ich zestawienie w
pliku tekstowym.'''

class PracownikKoleji(object):
    