from random import randint
from os import system
wynik =0
for i in range(10):
    a = randint(2,9)
    b = randint(2,9)
    w = int(input(f"{a}*{b}="))
    if(w == a*b):
        wynik+=1
    system("cls")
print("twoja ocena to:")
if(wynik<3): print("1")    
elif(wynik<5): print("2")
elif(wynik<7): print("3")
elif(wynik<8): print("4")
elif(wynik<9): print("5")