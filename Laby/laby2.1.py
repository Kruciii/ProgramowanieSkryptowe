import random
n = float(input("Wpisz ile licz wylosować"))
suma = 0
iloczyn = 1
while (n>0 and n%1==0):

    x = random.randint(1,8)
    suma+=x
    iloczyn*=x
    print(f"Liczba {n}: {x}")
    
    n-=1
else: 
    print(f"Suma {suma} , Iloczyn: {iloczyn}")
input()

