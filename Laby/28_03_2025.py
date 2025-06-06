'''Zadanie 5. Użytkownik wprowadza współrzędne dwóch wektorów trójwymiarowych
w postaci 3-elementowych krotek. Napisać program, który sprawdza czy wektory są
prostopadłe oraz czy wektory są równoległe, a także dodaje te wektory i zwraca wynik
dodawania'''
'''
a = (1,2)
b= (1,2,3)
while len(a)!=len(b):
    try:
        a = tuple(map(int,input("wprowadz wartości pierwszego wekrotra odzzielone spacja").split()))
        b = tuple(map(int,input("wprowadz wartości pierwszego wekrotra odzzielone spacja").split()))
    except ValueError:
        print("Podaj liczby całkowite")
iloczyn_skalarny = 0

for i in range(len(a)):
    iloczyn_skalarny += a[i]*b[i]
if iloczyn_skalarny == 0:
    print("wektory są prostopadłe")
else:
    print("Wektory nie są prostopadłe")
proporcja = None

for i in range(len(a)):
    if a[i] == 0 and b[i] == 0:
        continue
    elif a[i] == 0 or b[i] == 0:
        print("wektory nie są równoległe")
        break
    nowa_proporcja = a[i]/b[i]
    if(proporcja is None):
        proporcja = nowa_proporcja
        continue
    elif(proporcja != nowa_proporcja):
        print("wektory nie są równoległe")
        break
else:
    print("wektory są równoległe")
    

'''
'''Zadanie 6. Napisać program, w którym użytkownik wprowadza pięć powitań (łańcuchów
znaków), które są zapisywane do krotki, a następnie losowo wybierane jest jedno z nich,
które zostaje wyświetlone na ekranie. '''
'''import random
krotka = tuple()
for i in range(5):
    krotka+=(input(f"wprowadz {i+1} powitanie"),)

print(random.choice(krotka))

'''
'''Zadanie 7. Napisz program, który wypełnia 30-elementową listę liczbami losowymi
z przedziału [1,10], a następnie znajduje element minimalny w tej liście oraz oblicza iloczyn
elementów listy, a następnie usuwa z listy wszystkie dwójki, a trójki zastępuje jedynkami
oraz wyświetla tak zmodyfikowaną listę na ekranie. Jaki problem pojawia się przy
sekwencyjnym (wielokrotnym) usuwaniu elementu z listy? '''
'''import random
lista = list()
for i in range(30):
    lista.append(random.randint(1,10))
orginal = lista.copy()
posortowana = sorted(lista)
print("najmniejszy element",posortowana[0])
iloczyn = 1
min(lista)

for i in lista:
    iloczyn *=i
for _ in range(lista.count(2)):
    
        lista.remove(2)
for _ in range(int(lista.count(3))):
    lista[lista.index(3)] = 1
print("stara lista to:",orginal)
print("nowa lista to:",lista)
print("iloczyn to",iloczyn)'''


'''Zadanie 8. Napisz program, który wypełnia 10-elementową listę imionami oraz
nazwiskami pracowników (dane w postaci dwuelementowych krotek (imię, nazwisko)
wprowadza użytkownik), następnie na pozycję trzecią wstawia pracownika ANDRZEJA
KALICKIEGO, sortuje listę (domyślnie lub np. według nazwiska), wreszcie z listy tej
usuwa wszystkich pracowników, których imię zaczyna się na literę B i wyświetla dane
pracowników po tej modyfikacji. '''

'''lista = []
for i in range(10):
    imie = input(f"Wprowadź imię pracownika {i+1}: ")
    nazwisko = input(f"Wprowadź nazwisko pracownika {i+1}: ")
    lista.append((imie, nazwisko))
lista.insert(2,("ANDRZEJ","KALICKI"))
lista.sort()
nowa_lista = []
for i in range(len(lista)-1,-1,-1):
    if(lista[i][0][0].lower() == "b" ):
        del lista[i]
print(lista)
print(nowa_lista)'''