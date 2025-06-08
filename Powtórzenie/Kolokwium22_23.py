import random
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
        
    
