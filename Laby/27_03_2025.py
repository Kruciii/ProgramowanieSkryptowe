'''Zadanie 1. Napisz program, który losuje n liczb naturalnych z przedziału [1,8], wyświetla
je na ekranie, a następnie wyświetla sumę tych liczb oraz ich iloczyn, n jest całkowitą liczbą
dodatnią większą od jeden wprowadzoną przez użytkownika. Wykorzystaj pętlę WHILE
(również do zabezpieczenia wprowadzania odpowiedniej wartości liczby n). '''
'''
import random
i = -1
suma =0
iloczyn=1

while (i< 1 or i%1!=0 ):
    i = float(input("Wprowadz liczbe"))
 
i = int(i)

while i>0:
    liczba= random.randint(1,8)
    suma+=liczba
    iloczyn*=liczba
    print(liczba)
    i-=1
print("Suma to: ",suma)
print("Iloczyn to:",iloczyn)'''
#tutaj wersja for
'''
for x in range(i):
    liczba= random.randint(1,8)
    suma+=liczba
    iloczyn*=liczba
    print(liczba)
'''
'''Zadanie 2.
a) Dany jest ciąg arytmetyczny o pierwszym wyrazie 6 i różnicy 9. Wypisz elementy tego
ciągu mniejsze od 2000 i oblicz ich sumę. Wykorzystaj pętlę FOR.
b) Dany jest ciąg arytmetyczny o pierwszym wyrazie 10 i różnicy -6. Wypisz elementy tego
ciągu większe od -2000 i oblicz ich iloczyn. Wykorzystaj pętlę FOR. '''
#a
'''
a = 6
r =9
suma =0
for i in range(6,2000,9):
    print(i)
    suma+=i
    
print("Suma to: ",suma)'''
#b
'''iloczyn=1
for i in range(10,-2000,-6):
    print(i)
    iloczyn*=i
print("Iloczyn to: ",iloczyn)'''
'''Zadanie 3. Dany jest ciąg geometryczny o pierwszym wyrazie 3 i ilorazie 4. Wypisz
elementy tego ciągu mniejsze od 100000 i oblicz ich iloczyn oraz sumę. Wykorzystaj pętlę
WHILE'''
'''i= 3
suma=3
iloczyn = 3
print(i)
while(i<100000):
    i *=4
    iloczyn *=i
    suma+=i
    print(i)
print("Iloczyn to:",iloczyn," Suma to:",suma)
    '''
'''Zadanie 4. Napisz program, który losuje 10 par liczb dodatnich z przedziału [2,9],
a następnie dla każdej wylosowanej pary pyta o iloczyn liczb znajdujących się w parze. Jeśli
użytkownik poda dobry wynik, program dodaje mu 1 pkt. Na końcu program ma wyświetlić
wynik gracza i ocenę. Inaczej mówiąc – napisać program sprawdzający znajomość tabliczki
mnożenia, który podaje 10 losowych przykładów i ocenia użytkownika (ucznia). 
'''
'''
import random
suma =0
for i in range(10):
    liczba = (random.randint(2,9),random.randint(2,9))
    uz = int(input(f"podaj wynik mnożenia liczb{liczba}"))
    if(uz == liczba[0]*liczba[1]):
        suma+=1
    else:
        print("Zły wynik bambusie, znowu się nie uczyłeś!!")
print("Twój wynik to:",suma)
if(suma<5):
    print("Do niczego sie juz nie nadajesz. Jesteś nikim i nigdy niczego nie osiagniesz")
elif(suma<7):
    print("Jeszcze długa droga przed tobą padawanie ale debilem nie jesteś")
elif(suma<9):
    print("jesteś już blisko, podążaj tą drogą")
elif(suma==10):
    print("kujon")
'''
'''Zadanie 5. Napisz program, który pobiera od użytkownika dodatnią liczbę całkowitą,
a następnie wypisuje naturalne dzielniki wprowadzonej przez użytkownika liczby.
Zabezpieczyć program przed wprowadzaniem błędnych danych wejściowych
(wykorzystując pętlę WHILE). '''
'''putin =-1
while(putin<1 or putin%1!=0):
    putin = int(input("podaj liczbe bracie"))
for i in range(1,putin+1):
    if putin%i==0:
        print(i)
print(putin)'''
'''Zadanie 6. Napisz program, który oblicza NWW dwóch liczb naturalnych dodatnich
wprowadzonych przez użytkownika. W programie wykorzystać następujący algorytm
obliczania NWW: wybieramy większą z liczb, a następnie mnożymy ją przez kolejne liczby
naturalne począwszy od  jedności. Algorytm kończy się, gdy analizowany iloczyn podzieli
się przez drugą z liczb np. NWW(8,6)=24, gdyż ,
a 24 dzieli się już przez 6, więc ta liczba (ostatni iloczyn - 24) jest najmniejszą wspólną
wielokrotnością. Zabezpiecz moment wprowadzania danych (obie wprowadzane liczby
mają być dodatnie), używając pętli WHILE.'''
'''a = -1
b = -1
while( a<=0 or b<0 or a%1!=0 or b%1!=0):
    a = int(input("Wprowadz pierwsza liczbe"))
    b = int(input("Wprowadz druga liczbe"))
if(a>b):
    x = a
    y=b
else:
    x=b
    y=a
i=1
while((x*i)%y!=0):
    i+=1
print(x*i)
'''
'''
Zadanie 7. Napisz program, który oblicza NWD dwóch liczb naturalnych dodatnich
wprowadzonych przez użytkownika. W programie wykorzystać algorytm Euklidesa oparty
o odejmowanie liczb (lub dzielenie modulo) oraz zabezpieczyć moment wprowadzania
danych. '''
'''a=-1
b=-1
while(a<0 or b<0):
    a = int(input("wprowadz 1 liczbe"))
    b = int(input("wprowadz druga liczbe"))
if(b>a):
    tmp = a
    a = b
    b = tmp
r=1
rp=0
while(r !=0):
    rp = r
    r=a%b
    a=b
    b=r
print(rp)'''
'''Zadanie 8. Napisz program, który wypisuje liczby pierwsze mniejsze od wprowadzonej
przez użytkownika liczby całkowitej większej od dwóch. Wykorzystać zagnieżdżoną
(podwójną) instrukcję iteracyjną oraz zabezpieczyć moment wprowadzania danych'''
'''''''''
i =-1
while(i<=2):
    i = int(input("Wprowadz liczbe: "))
for x in range(1,i):
    for y in range(1,x+1):
      
        if(x%y==0 and y!= 1 and y!=x): break  
        if(y==x): print(y)
''''''
Zadanie 9. Napisz program, który wypisuje pierwsze n liczb ciągu Fibonacciego, n jest
liczbą naturalną dodatnią wprowadzoną przez użytkownika. Zabezpieczyć moment
wprowadzania danych. '''
'''n =-1 
n1 = 0
n2=1

while(n<= 0):
    try:
        n = int(input("wprowadz ilosc liczb fibonaciego"))
    except ValueError:
        print("To nie liczba całkowita")
a, b = 0, 1
for _ in range(n):
    print(a)  
    a, b = b, a + b  
'''
'''Zadanie 10. Napisz program, który oblicza silnię (n!) dla liczby naturalnej n wprowadzonej
przez użytkownika. Zabezpieczyć moment wprowadzania danych. '''
'''n = -1
while(n<=0):
    try:
        n = int(input("Podaj silnie"))
    except ValueError:
        print("Kolego miała byc liczba naturalna")
silna = 1
for i in range(1,n+1):
    silna*=i
    
print(silna)'''
'''Zadanie 11. Napisz program, który oblicza podwójną silnię (n!!) dla liczby naturalnej n
wprowadzonej przez użytkownika. '''
'''n = -1
while(n<=0):
    try:
        n = int(input("Podaj silnie"))
    except ValueError:
        print("Kolego miała byc liczba naturalna")
silna = 1
if(n%2 == 0):
    for i in range(2,n+1,2):
        silna*=i
else:
     for i in range(1,n+1,2):
        silna*=i
print(silna)'''
'''Zadanie 12. Napisz program, który dla wprowadzonej przez użytkownika liczby naturalnej
dodatniej większej od jedności dokonuje jej rozkładu na czynniki pierwsze. Na przykład dla
liczby 60 powinien być zwrócony wynik: 2, 2, 3, 5. 
''''''
i = -1
while(i<=0):
    try: 
        i = int(input("wprowadz liczbe"))
    except ValueError:
        print("ale całkowita wprowadz baranie")

while(i>1):
    for x in range(2,i+1):
        if(i%x==0):
            i = i//x
            print(x)
            break
        
'''

#znaki  = '''Zadanie 13. Napisz program, w którym zdefiniujesz dowolny łańcuch znaków zawierający
#kilka linii (wykorzystaj potrójny cudzysłów). Następnie program ma wypisać liczbę
#znaków, słów oraz linii tego łańcucha. '''
#liczba_slow = len(znaki.split())
#liczba_znakow=len(znaki)
#liczba_lini = len(znaki.split("\n"))
#print("Liczba znaków:", liczba_znakow)
#print("Liczba słów:", liczba_slow)
#print("Liczba linii:", liczba_lini)
'''Zadanie 14. Użytkownik wprowadza dowolny łańcuch znaków. Napisać program, który
wypisuje wszystkie znaki zawarte w łańcuchu, oblicza jego długość, wypisuje liczbę
wystąpień litery a (niezależnie od wielkości) oraz sprawdza, czy łańcuch ten jest
palindromem. Wykorzystać jedynie pętle iteracyjne, nie wykorzystywać dodatkowych
funkcji wbudowanych klasy str. '''
'''a = input("putin")
suma = 0
czy = True
for i in a:
    print(i)
    if(i.lower() =="a"): suma+=1
print(len(a))
print(suma)
for i in range(len(a)):
    if(a[i]!=a[len(a)-i-1]):
        czy = False
print(czy)
'''
'''n = int(input("podaj ilosc pierwiastkow kolego"))
i =0
while(i:=i+1)<n+1:
    print(round(i**0.5,2))
    
''''''
n=-1
while(n<=0):
    try:
        n = int(input("Podaj liczbe"))
    except ValueError:
        print("calkowita podaj")
i=1 
liczba = 0
while(i<=n):
    if(liczba>=1000000):
        print("liczba za duza")
        break
    liczba+= i**2
    i+=1
else:
    print(liczba)
'''
'''n=-1
while(n<=0):
    try:
        n = int(input("Podaj liczbe"))
    except ValueError:
        print("calkowita podaj")
'''
#Lista 2
'''Zadanie 1. Napisz program, który losuje n liczb naturalnych z przedziału [1,8], wyświetla
je na ekranie, a następnie wyświetla sumę tych liczb oraz ich iloczyn, n jest całkowitą liczbą
dodatnią większą od jeden wprowadzoną przez użytkownika. Wykorzystaj pętlę WHILE
(również do zabezpieczenia wprowadzania odpowiedniej wartości liczby n). '''
'''import random
n =-1
while(n<=0):
    try:
        n = int(input("Podaj liczbe"))
    except ValueError:
        print("Podaj liczbe całkowita")
suma =0
iloczyn =1
i=0
while(i<n):
    liczba = random.randint(1,8)
    print(liczba)
    suma += liczba
    iloczyn *=liczba
    i+=1
print(suma,iloczyn)'''
'''Zadanie 2.
a) Dany jest ciąg arytmetyczny o pierwszym wyrazie 6 i różnicy 9. Wypisz elementy tego
ciągu mniejsze od 2000 i oblicz ich sumę. Wykorzystaj pętlę FOR.
b) Dany jest ciąg arytmetyczny o pierwszym wyrazie 10 i różnicy -6. Wypisz elementy tego
ciągu większe od -2000 i oblicz ich iloczyn. Wykorzystaj pętlę FOR. '''
'''sum = 0
for i in range(6,2000,9):
    print(i)
    sum += i
print(sum)
iloczyn =1
for i in range(10,-2000,-6):
    print(i)
    iloczyn *= i
print(iloczyn)
'''
'''Zadanie 3. Dany jest ciąg geometryczny o pierwszym wyrazie 3 i ilorazie 4. Wypisz
elementy tego ciągu mniejsze od 100000 i oblicz ich iloczyn oraz sumę. Wykorzystaj pętlę
WHILE. '''
'''iloczyn =1
suma =0
r = 4
wynik = 3
while(wynik<100000):
    suma+=wynik
    iloczyn*=wynik
    print(wynik)
    wynik*=r
    
print(iloczyn)
print(suma)
'''
'''Zadanie 1. Napisz program, który pobiera od użytkownika dowolny łańcuch znaków,
zwraca długość tego łańcucha oraz wypisuje wszystkie samogłoski (niezależnie od
wielkości) występujące w łańcuchu (można zastanowić się nad tym, aby samogłoski były
wypisywane bez powtórzeń np. dla łańcucha „Abecadło” zostanie wypisany ciąg: a, e, o),
a następnie wypisuje elementy łańcucha w odwrotnej kolejności, w tym przypadku
wykorzystać pętlę FOR oraz dwie wersje indeksowania – liczbami nieujemnymi oraz
liczbami ujemnymi. '''
'''znak = input("podaj lancuch znakow")
print(len(znak))
samogloski = "aeiou"
for i in znak:
    if i.lower() in samogloski:
        print(i)
for i in range(len(znak)-1,-1,-1):
    print(znak[i])
    '''
'''Zadanie 2. Napisz program, który pobiera od użytkownika dowolny łańcuch znaków,
a następnie szyfruje go, zamieniając litery a na cyfry 7, litery d na cyfry 1 oraz litery f na
cyfry 9 (niezależnie od wielkości liter) i zwraca tak uzyskany szyfrogram w postaci
łańcucha znaków. Jak wykorzystać to zadanie do stworzenia podobnego programu, który
usuwa z łańcucha znaków wskazaną przez użytkownika literę? '''
'''lancuch = input("podaj lanuch do zaszyfrowania")
zaszyfrowany =""
for i in lancuch:
    if(i.lower() =="a"):
        zaszyfrowany +=str(7)
    elif(i.lower()=="d"):
        zaszyfrowany +=str(1)
    elif(i.lower()=="f"):
        zaszyfrowany+=str(9)
    else:
        zaszyfrowany+=i
print("Zaszyfrowany",zaszyfrowany)
'''
'''Zadanie 3. Użytkownik wprowadza dowolny łańcuch znaków oraz liczbę naturalną
dodatnią n. Napisać program, który wypisuje wszystkie n-elementowe słowa będące
podsłowami wprowadzonego łańcucha znaków. Wykorzystać pętlę FOR i operację
wycinania. Na przykład dla słowa kajak i liczby n = 3 powinny być zwrócone podsłowa:
kaj, aja, jak. '''
'''lancuch = input("wprowadz lancuch")
n = -1
while(n<=0):
    try:
        n = int(input("wprowadzliczbe naturalna"))
    except ValueError:
        print("nie taka")
for i in range(len(lancuch)-n+1):
    lancuch[i:i+n]'''
'''Zadanie 4.
a) Napisać program, który generuje 49-elementową krotkę, której elementami są kolejne
liczby całkowite od 1 do 49, a następnie losuje z tej krotki liczbę, usuwa ją i losuje
kolejną aż do uzyskania zestawu sześciu różnych liczb losowych (gra liczbowa
LOTTO). W efekcie końcowym program ma zwrócić krotkę wylosowanych liczb.
Następnie zmodyfikować program tak, aby losował n 6-elementowych krotek
(zakładów), gdzie n jest liczbą wprowadzoną przez użytkownika;
b) Napisać analogiczny program, w którym zamiast krotek używamy list.
Zastanowić się nad wypisywaniem zakładów w sposób uporządkowany (wykorzystać
sortowanie elementów krotek lub list). '''
'''import random 
losowanie = list(range(1,50))
wylosowanie =[]
for _ in range(6):
    wybrana = random.choice(losowanie)
    wylosowanie.append(wybrana)
    losowanie.remove(wybrana)
wylosowanie = tuple(wylosowanie)
print(wylosowanie)
    
n = int(input("ile zakladów"))
for _ in range(n):
    losowanie = list(range(1,49))
    wylosowanie =[]
    for _ in range(6):
        wybrana = random.choice(losowanie)
        wylosowanie.append(wybrana)
        losowanie.remove(wybrana)
    wylosowanie = tuple(wylosowanie)
    print(wylosowanie)
    
    '''
