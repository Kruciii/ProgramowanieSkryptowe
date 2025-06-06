'''from pizzeria import *
from sys import argv
from srednie import *
print("Rachunek",rachunek(),"sł")
try:
    match argv[1]:
        case "A":
            print(arytmetyczna(argv))
        case "G":
            print(geometryczna(argv))
        case "H":
            print(harmoniczna())
        case _:
            print("bledna popcja") 
except:
    print("Błędne dane")
    
    
poleprostokata = lambda a,b:a*b if a>0 and b>0 else "Bledne dane"
poleiobwodkwadratu = lambda a:(a*a,4*a) if a>0 else "Błędny bok!"
sumairoznica = lambda x,y:(x**2+y**2,x**2-y**2)
komunikat = lambda :print("pupcia")
kwadratliczby = lambda a:print(a**2)
wprowadzenie = lambda :input("Podaj imie")

print(poleprostokata(5,7))
'''

'''pracownicy = [("Adam","Nowak",30,5),("Karolina","Kowalska",50,25),("Adam","Urban",60,36),("Barbara","Adamiec",60,36)]
pracownicy.sort(key= lambda x:(x[1],x[0]))
print(pracownicy)
'''

from functools import wraps
#Dekorator
def binarny(f):
    @wraps(f)
    def call(*args):
        return str(bin(f(*args)))[2:]
    return call
def oktalny(f):
    @wraps(f)
    def call(*args):
        return str(oct(f(*args)))[2:]
    return call
def hexadecymalny(f):
    @wraps(f)
    def call(*args):
        return str(hex(f(*args)))[2:]
    return call
@hexadecymalny
def suma(a,b):
    return a+b

print(suma(4,5))
