import math
from sys import exit
# Zadanie 1
def usunsamogloski(a):
    samogloski = "aeiouyęąó"
    wynik= ""
    for i in a:
        if(i.lower() not in samogloski):
            wynik+=i
    return wynik
a = input("Proszę wprowadzić łańcuch znaków: ")
b = usunsamogloski(a)
print(f"liczba samoglosek to {len(a)-len(b)}")
print(f"Przekształcony łańcuch: {b}")
#Zadanie 2
class Prostokąt:
    def __init__(self,a,b):
        if(a>0 and b>0):
            self.a = a
            self.b =b
        else:
            exit()
    def pole(self):
        return self.a * self.b
    def przekatna(self):
        return (self.a ** 2 + self.b ** 2) ** (1/2)
    
class Rownoleglobok(Prostokąt):
    def __init__(self,a,b,alpha):
        if(not(alpha>0 and alpha<90)):
            exit()  
        super().__init__(self,a,b)
        self.alpha = alpha
    def pole(self):
        return (self.a*self.b*math.sin(self.a*math.pi/180))
        
    def przekatna(self):
        return (self.a**2+self.b**2-2*self.a*self.b*math.cos(self.alpha*math.pi/180))
    