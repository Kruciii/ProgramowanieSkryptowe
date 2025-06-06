#Zadanie 1. Napisz program, który losuje n liczb naturalnych z przedziału [1,8], wyświetla
#je na ekranie, a następnie wyświetla sumę tych liczb oraz ich iloczyn, n jest całkowitą liczbą
#dodatnią większą od jeden wprowadzoną przez użytkownika. Wykorzystaj pętlę WHILE
#(również do zabezpieczenia wprowadzania odpowiedniej wartości liczby n). 
import random
n = float(input("Wpisz ile licz wylosować"))
suma = 0
iloczyn = 1
while (n>0 and n%1==0):

    x = random.randint(1,8)
    suma+=x
    iloczyn*=x
    print(f"Liczba {n+1}: {x}")
    
    n-=1
else: 
    print(f"Suma {suma} , Iloczyn: {iloczyn}")
input()
#Zad 17
d = float(input("jakie działanie"))
a= float(input("liczba 1: "))
b = float(input("Liczba 2: "))
match d:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "**":
        if (a==0 and b<=0) or (a<0 and b%1!=0):
            print(a**b)
    case "/":
        if  b!=0:
            print(a/b)
    case "//":
        print(a//b)
    case "%":
        print(a%b)







