'''class NiewykonalneError(Exception):
    """Wyjątek zgłaszany, gdy nie można wykonać operacji."""
    pass


try: 
    a = float(input("Podaj podstawe: "))
    b = float(input("Podaj wykładnik: "))
    if (a==0 and b<=0) or (a<0 and b%1!=0):
        raise NiewykonalneError("Nie można obliczyć pierwiastka z liczby ujemnej.")
except NiewykonalneError :
    print("Nie można wykonać tej operacji.")
except ValueError:
    print("Podano błędne dane.")
else:
    print(f"Wynik: {a**b}")
finally:
    print("Koniec programu.")
    
    '''
    ## KOLOKWIUM 2 LUB 9 CZERWCA
    
'''Zadanie 3. Napisz program, który zapisuje do pliku tekstowego dzielniki liczby n
wprowadzonej przez użytkownika. Zadbaj o odpowiednie formatowanie (przetestuj różne
sposoby formatowania: fstringi, funkcja format czy formatowanie w starym stylu). Dzielniki
powinny zapisywać się maksymalnie po dziesięć w każdej linii. Program napisz w dwóch
wersjach: z wykorzystaniem instrukcji with oraz bez niej. Zabezpiecz program przed
nieodpowiednim argumentem wejściowym (n musi być liczbą naturalną dodatnią – wykorzystaj
instrukcję try - except - else). '''
'''import os
class NiedodatniaError(Exception):
    pass
try:
    n = int(input("Podaj liczbę naturalną dodatnią: "))
    if n <= 0:
        raise NiedodatniaError("Liczba musi być dodatnia.")
    
except NiedodatniaError:
    print("Podano liczbę nie dodatnią.")
except ValueError:
    print("Podano liczbę niecałkowitą.")
else:
    licznik = 0
    f = open("dzielniki2.txt", "w")
    for i in range(1, n + 1):
        if n % i == 0:
            f.write(str(i) + "\t\t\t")
            licznik += 1
            if licznik % 10 == 0:
                 f.write("\n")
    f.write("\n")
    f.close()
    
'''
'''import os
f2 = open("2.txt","r")
f1 = open("1.txt","a")
f1.write("\n")
f1.write(f2.read())

f1.close()
f2.close()'''
'''from pickle import dump, load
pracownicy = [
    ("Adam", "Nowak", 1980, 20, 6000, "1"),
    ("Ewa", "Kowalska", 1985, 15, 5500, "2"),
    ("Jan", "Wiśniewski", 1975, 25, 7000, "3"),
    ("Anna", "Wójcik", 1990, 10, 4800, "4"),
    ("Piotr", "Kowalczyk", 1982, 18, 6200, "5"),
    ("Katarzyna", "Kamińska", 1988, 12, 5100, "6"),
    ("Marek", "Lewandowski", 1978, 22, 6800, "7"),
    ("Agnieszka", "Zielińska", 1992, 8, 4500, "8"),
    ("Tomasz", "Szymański", 1983, 17, 6000, "9"),
    ("Magdalena", "Woźniak", 1986, 14, 5300, "10"),
]
f = open("pracownicy.bin","wb")
for i in range(len(pracownicy)):
    dump(pracownicy[i],f)
f.close()

haslo = input("Podaj haslo")
f = open("pracownicy.bin","rb")

i = True
while(i):
    try:
        x = load(f)
        if x[5] == haslo:
            print(x)
            
    except:
        print("Nie ma takiego pracownika")
        '''
        