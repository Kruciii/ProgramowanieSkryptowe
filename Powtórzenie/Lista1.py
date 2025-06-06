
class ZaMalaError(Exception):
    pass
#Zadanie 7
def liczkwadratiszescian(a):
    try:
        k = int(a)^2
        s = int(a)^2
    except:
        print("Nieporawnie podana liczba")
    else:
        return (k,s)
    
#Zadanie 8
def binocthex(a):
    try:
        a = int(a)
        b = bin(a)
        o = oct(a)
        h = hex(a)
    except:
        print("podano nieprawidłową liczbe")
    else:
        return (b,o,h)
#Zadanie 9
def isdevided4(a):
    a = int(a)
    if(a%4==0):
        print("liczba jest podzielna przez 4")
    else:
        print("liczba nie jest podziena przez 4")
#Zadanie 10
def czyrozwiazuje(x):
    x = int(x)
    if(x^3-5*x+4==0):
        print(True)
    else:
        print(False)
#Zadanie 11
def poleobwod(a,b):
    while(True):
        w = input("Jeśli chcesz policzyć pole wpisz p jesli obwod wpisz o")
        try:
            w = str.lower(w)
            a = float(a)
            b =float(b)
            if(a<0 or b<0):
                raise ZaMalaError
        
        except ZaMalaError:
            print("Prosze podac dodatnia liczbe")
        except:
            print("Proszę podać odpowednie")
        else:
            
            if(w =='p'):
                return a*b
            elif(w=='o'):
                return 2*a+2*b
            else:
                print("nie ma takiej opcji")
                