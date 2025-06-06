'''Zadanie 5. Użytkownik wprowadza współrzędne dwóch wektorów trójwymiarowych
w postaci 3-elementowych krotek. Napisać program, który sprawdza czy wektory są
prostopadłe oraz czy wektory są równoległe, a także dodaje te wektory i zwraca wynik
dodawania. '''
x1 = float(input("X1"))
x2 = float(input("X2"))
x3 = float(input("X3"))
y1 = float(input("Y1"))
y2 = float(input("Y2"))
y3 = float(input("Y3"))
x = (x1,x2,x3)
y = (y1,y2,y3)
wynik = (y1+x1,y2+x2,y3+x3)
iloczyn_pros = (x1*y1+x2*y2+x3*y3)
iloczyn_row = (x2*y3-x3*y2,)