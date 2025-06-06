#zadanie 10
'''n = int(input("Podaj liczbe wierszy"))
m = int(input("Podaj liczbe kolumn"))
macierz1 = [[int(input(f"Podaj element {i+1} {j+i}")) for i in range(m)] for i in range(n)]
macierz2 = [[int(input(f"Podaj element {i+1} {j+i}")) for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(macierz1[i][j],end="\t")
    print()
for i in range(n):
    for j in range(m):
        print(macierz2[i][j],end="\t")
    print()
for i in range(n):
    for j in range(m):
        print(macierz1[i][j]+macierz2[i][j],end = "\t")
    print()
    
'''
'''# zad 13
a = int(input("Podaj dlugosc boku kwadratu"))
charakterystyki = {"p":f"Pole wynosi{a*a}","o":f"obwod wynosi {4*a}","d":f"Przekatna wynosi {a*2**0.5}"}
i = "z"
while i.lower() not in charakterystyki:
    i = input("Wpisz aby byla charakterystyka")
print(charakterystyki[i])
'''
# zad 15
'''a) wszystkie liczby czterocyfrowe o niepowtarzających się cyfrach;'''
cyfry ={0,1,2,3,4,5,6,7,8,9}
licznik =0
for i in cyfry - {0}:
    for j in cyfry -{i}:
        for k in cyfry-{i,j}:
            for l in cyfry-{i,j,k}:
                print(1000*i+100*j+10*k)
                licznik+=1
print(9*8*9*7)
print(licznik)