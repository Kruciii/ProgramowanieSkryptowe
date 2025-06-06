#Zadanie 14. Napisz program, w którym tworzony jest zbiór pięcioelementowy {1,2,3,4,5},
#a następnie wypisywane są wszystkie 3-elementowe podzbiory (kombinacje) tego zbioru. 
'''zbior = set(range(1,6))
uzyte =[]
for i in zbior:
    for x in zbior -{i}:
        for y in zbior -{i,x}:
            if {i,x,y} not in uzyte:
                print({i,x,y})
                uzyte.append({i,x,y})'''
#Zadanie 16a
#TRZY + TRZY = SZEŚĆ
'''cyfry = set(range(0,9))
for T in cyfry -{0}:
    for R in cyfry -{T}:
        for Z in cyfry -{T,R}:
            for Y in cyfry -{T,R,Z,}:
                for S in cyfry - {T,R,Z,Y}:
                    for E in cyfry -{T,R,Z,Y,S}:
                        for Ś in cyfry -{T,R,Z,Y,S,E}:
                            for Ć in cyfry -{T,R,Z,Y,S,E,Ś}:
                                if(2*(1000*T+100*R+10*Z+Y)==Ć+Ś*10+100*E+1000*Z+10000*S):
                                    print(1000*T+100*R+10*Z+Y,"+",1000*T+100*R+10*Z+Y,"=",Ć+10*Ś+100*E+1000*Z+10000*S) # Coś jest źle
                                    '''

'''Zadanie 6. Napisz program, który oblicza objętość, pole powierzchni całkowitej oraz
przekątną prostopadłościanu o krawędziach a, b, c, których długości podaje użytkownik.
Program powinien zawierać funkcję pole_obj_prz(a,b,c), która zwraca charakterystyki
w postaci krotki. W programie głównym wyświetlić te charakterystyki osobno, używając
operacji indeksowania. '''
def pole_obj_prz(a,b,c):
    v = a*b*c
    p = 2*a*b + 2*a*c +2*b*c
    r = (a**2+b**2+c**2)**0.5 #(a**2+b**2+c**2)**0.5
    return v,p,r
    
print(pole_obj_prz(1,2,3))
print(pole_obj_prz(2,3,4)[1])
print(pole_obj_prz(2,3,4)[0])
print(pole_obj_prz(2,3,4)[2])
    
    # Zadania do zrobienia samodzielnie
    # Zadanie 4,8,9 i materiał 5
    
'''Zadanie 7. Napisać program, który oblicza średnią arytmetyczną liczb wprowadzonych
przez użytkownika. Program powinien zawierać funkcję srednia_ar(*lista), która
przyjmuje dowolną liczbę argumentów. Następnie w programie głównym wywołać tę
funkcję dla trzyelementowego oraz czteroelementowego ciągu danych oraz dla iteratora
range(a,b,c) przyjmującego dowolne parametry a, b oraz c. '''

def srednia_ar(*a):
    return sum(a)/len(a)

print("srednia ar liczb 1,2,3,4",srednia_ar(1,2,3,4))

'''Zadanie 2. Napisz program, który wyświetla n kolejnych przybliżeń tzw. złotej liczby,
która jest granicą ciągu określonego w sposób rekurencyjny:

Program powinien zawierać funkcję zlota(n), która zwraca n-te przybliżenie złotej liczby.
Rozważyć dwie wersje funkcji: rekurencyjną oraz iteracyjną. Wykorzystać również
adnotacje typów. 
'''
def zlota_rek(n):
    if(n==1):
        return 1
    return 1+1/zlota_rek(n-1)

def zlota_it(n):
    i=1
    for x in range(1,n):
        i = 1+1/i
        
    return i

print(zlota_it(5),zlota_rek(5))

'''Zadanie 1. Napisz program, który wypisuje uporządkowaną listę dzielników (naturalnych)
liczby naturalnej dodatniej n wprowadzonej przez użytkownika, wykorzystując algorytm
wypisywania dzielników parami. Program powinien zawierać funkcję dzielniki(n), która
zwraca posortowaną listę dzielników, a w przypadku błędnych danych wejściowych (liczba
n mniejsza od 1) powinnna zwracać odpowiedni komunikat ostrzegawczy. Program
powinien dodatkowo zawierać funkcję opis(), która informuje użytkownika, jaka jest
funkcja programu. '''
'''def dzielniki(n):
    lista =[]
    index =0
    for i in range(1,int((n)**0.5)+1):
        if(n%i==0 and i!=n/i):
            lista.insert(index,i)
            lista.insert(index+1,n//i)
            index +=1
        elif(n%i==0):
            lista.insert(index,i)
            index +=1
    return lista
n=int(input("podaj a"))
print(dzielniki(n))'''

#Zadanie 3. Napisz program, który dla wprowadzonej przez użytkownika liczby n wypisuje
#liczby pierwsze mniejsze od n. Wykorzystać algorytm sita Eratostenesa. Program powinien
#zawierać funkcję Eratostenes(n), która odpowiada za wypisanie liczb pierwszych
#mniejszych od n. 
'''def pierwsza_latwa(n):
    for i in range(2,n):
        d=2
        while i%d!=0:
            d+=1
        if d==i:
            print(i)
print(pierwsza_latwa(10000000))
'''
'''def eratostenes(n):
    lista = [0 for i in range(n)]
    for i in range(2,n):
        if lista[i] == 0:
            print(i)
            k=2
            while i*k<n:
                lista[i*k]=1
                k+=1
n = 10
eratostenes(100000000)'''
