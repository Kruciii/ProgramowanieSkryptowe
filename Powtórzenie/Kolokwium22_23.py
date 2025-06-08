import random
from sys import exit
import math
#Zad 1
#a
''' Napisz funkcje usunpodzielne5(a) oraz liczbadodatnich(a), które odpowiadają za
usunięcie z listy a wszystkich liczb podzielnych przez 5 i zwrócenie zmienionej listy
(funkcja ma zawierać słowo return, powinna zwracać zmodyfikowaną listę, nie
wykorzystywać list pomocniczych!) oraz obliczanie liczby liczb dodatnich (również
ta druga funkcja musi zawierać słowo return) '''


def usunpodzielne5(a):
    try:
        if(isinstance(a,list)):
            for i in range(len(a)-11,-1,-1):
                if(a[i]%5==0):
                    del a[i]
        else:
            raise ValueError

        return a
    except ValueError:
        print("Błąd,Prosze podać listę")
    except:
        print("lista powinna zawierać cyfry.")
        


def liczbadodatnich(a):
    try:
        d=0
        if(isinstance(a,list)):
            for i in range(len(a)-1,-1,-1):
                if(a[i]>0):
                    d+=1
        else:
            raise ValueError
        return d
    except ValueError:
        print("Należy podać liste")
    except:
        print("Podano niepoprawną liczbe w liście")
        
    
lista = list()
for i in range(50):
    lista.append(random.randint(-15,14))
print(f"Oto lista {len(lista)} liczb")
print(lista)
print(f"zawiera ona {liczbadodatnich(lista)} liczb dodatnich")
print("To natomiast ta sama lista ale bez liczb podzielnych na 5")
print(usunpodzielne5(list(lista)))

with open("liczby.txt","a") as f:
    for i in range(len(lista)-1):
        f.write(str(lista[i]))
        f.write("\t")
        if((i+1)%10==0):
            f.write("\n")
        
#Zadanie 2
class Kolo:
    def __init__(self,R):
        if(R<=0): exit(1)
        self.R =R
        
    def pole(self):
        return math.pi *self.R**2
    
    def obwod(self):
        return 2*math.pi*self.R
    
    def __str__(self):
        return (f"To jest kółko. Ma ono pole {self.pole()} oraz obwod {self.obwod()}")
    
class Polkole(Kolo):
    def __init__(self,R):
        super().__init__(R)
        
    def pole(self):
        return super().pole()/2
    
    def obwod(self):
        return super().obwod()/2 + 2*self.R
    
    def __str__(self):
        return (f"To jest Polkole. Ma ono pole {self.pole()} oraz obwod {self.obwod()}")

kolko = Kolo(2)
polkolko = Polkole(4)
print(kolko)
print(polkolko)
    
