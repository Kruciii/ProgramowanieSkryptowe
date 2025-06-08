from sys import exit
def usun12(l):
    nowy =""
    try:
        if(not isinstance(l,str)):
            raise TypeError
        for i in range(len(l)):
            if not(l[i] == '1' or l[i]=='2'):
                nowy+=l[i]
    except TypeError:
        print("przekazana zmienna nie jest łańuchem znaków")
    except:
        print("Nastapil nieokreślony błąd")
    else:
        return nowy
        
def liczbasamoglosek(l):
    liczba =0
    samogloski = "aeiouyąęó"
    try:
        if(not isinstance(l,str)):
            raise TypeError
        for i in l:
            if i in samogloski:
                liczba+=1
    except TypeError:
        print("podano zmienna która nie jest łańcuchem znaków")
    except:
        print("Nastąpił niekoreślony błąd")
    else:
        return liczba
data = input("Proszę podać łańcuch znaków")
print(data)
print(liczbasamoglosek(data))
print(usun12(data))

with open("znaki.txt","w") as f:
    for i in range(len(data)):
        if i%4==0 and not i==0:
            f.write("\n")
        f.write(data[i])
        f.write("\t")

#Zadanie 2
class Szescian:
    def __init__(self,a):
        try:
            if(a<=0):
                exit()
            self.a = float(a)
        except ValueError:
            print("Podana wartość nie jest liczbą")    
        except Exception as e:
            print("inny błąd",e)
    def pole(self):
        return self.a**2
    
    def obowd(self):
        return self.a*4
    
    def __str__(self):
        print(f"jestem szczecianem i mam pole {self.pole()} oraz obdowd {self.obwod()}")