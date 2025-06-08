import pyodbc



conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                        "Server=10.44.140.92, 21433;"
                        "Database=db223435;"
                        "Encrypt=no;"
                        "uid=st223435;pwd=p223435"
                        )
cur = conn.cursor()
def czy_istnieje_pracownik(id_pracownika):
    cur.execute("SELECT 1 FROM Pracownicy WHERE id_pracownika = ?", (id_pracownika,))
    wynik = cur.fetchone()
    
    return wynik is not None

def pobierz_pracownika(id_pracownika):
    
    cur.execute("SELECT * FROM Pracownicy WHERE id_pracownika = ?", (id_pracownika,))
    wynik = cur.fetchone()
    return wynik

def pobierz_pracownika_ze_specjalizacja(id_pracownika):

    cur.execute('''
        SELECT 
            Pracownicy.id_pracownika,
            Pracownicy.imię,
            Pracownicy.nazwisko,
            Specjalizacje.nazwa AS specjalizacja
        FROM Pracownicy
        JOIN Specjalizacje ON Pracownicy.id_specjalizacji = Specjalizacje.id_specjalizacji
        WHERE Pracownicy.id_pracownika = ?
    ''', (id_pracownika,))

    wynik = cur.fetchone()


    if wynik:
        print(f"ID: {wynik[0]}")
        print(f"Imię: {wynik[1]}")
        print(f"Nazwisko: {wynik[2]}")
        print(f"Specjalizacja: {wynik[3]}")
    else:
        print("Nie znaleziono pracownika o podanym ID.")
            
def zamowienia_menu():
    while True:
        print("\n--- Menu Zamówienia ---")
        print("1. Wyświetl wszystkie zamówienia")
        print("2. Dodaj nowe zamówienie")
        print("3. Usuń zamówienie")
        print("4. Edytuj daty zamówienia")
        print("0. Powrót do głównego menu")

        wybor = input("Podaj numer opcji: ")

        try:
            if wybor == '1':
                cur.execute("SELECT * FROM Zamówienia")
                zamowienia = cur.fetchall()
                for zamowienie in zamowienia:
                    print(zamowienie)
            elif wybor == '2':
                id_goscia = input("Podaj ID gościa: ")
                data_zlozenia = input("Podaj datę złożenia (YYYY-MM-DD): ")
                data_zakonczenia = input("Podaj datę zakończenia (YYYY-MM-DD) lub pozostaw puste: ")
                cur.execute(
                    "INSERT INTO Zamowienia (id_gościa, data_złożenia, data_zakończenia) VALUES (?, ?, ?)",
                    (id_goscia, data_zlozenia, data_zakonczenia if data_zakonczenia else None)
                )
                conn.commit()
                print("Dodano nowe zamówienie.")
            elif wybor == '3':
                id_zamowienia = input("Podaj ID zamówienia do usunięcia: ")
                cur.execute("DELETE FROM Zamowienia WHERE id_zamówienia = ?", (id_zamowienia,))
                conn.commit()
                print("Usunięto zamówienie.")
            elif wybor == '4':
                id_zamowienia = input("Podaj ID zamówienia do edycji: ")
                nowa_data_zlozenia = input("Podaj nową datę złożenia (YYYY-MM-DD): ")
                nowa_data_zakonczenia = input("Podaj nową datę zakończenia (YYYY-MM-DD) lub pozostaw puste: ")
                cur.execute(
                    "UPDATE Zamowienia SET data_złożenia = ?, data_zakończenia = ? WHERE id_zamówienia = ?",
                    (nowa_data_zlozenia, nowa_data_zakonczenia if nowa_data_zakonczenia else None, id_zamowienia)
                )
                conn.commit()
                print("Zaktualizowano daty zamówienia.")
            elif wybor == '0':
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
        except Exception as e:
            print(f"Błąd: {e}")

def goscie_menu():
    while True:
        print("\n--- Menu Goście ---")
        print("1. Wyświetl wszystkich gości")
        print("2. Dodaj nowego gościa")
        print("3. Usuń gościa")
        print("0. Powrót do głównego menu")

        wybor = input("Podaj numer opcji: ")

        try:
            if wybor == '1':
                cur.execute("SELECT * FROM Goście")
                goscie = cur.fetchall()
                for gosc in goscie:
                    print(gosc)
            elif wybor == '2':
                imie = input("Podaj imię gościa: ")
                nazwisko = input("Podaj nazwisko gościa: ")
                telefon = input("Podaj numer telefonu gościa: ")
                cur.execute(
                    "INSERT INTO Goście (imię, nazwisko, telefon) VALUES (?, ?, ?)",
                    (imie, nazwisko, telefon)
                )
                conn.commit()
                print("Dodano nowego gościa.")
            elif wybor == '3':
                id_goscia = input("Podaj ID gościa do usunięcia: ")
                cur.execute("DELETE FROM Goście WHERE id_gościa = ?", (id_goscia,))
                conn.commit()
                print("Usunięto gościa.")
            elif wybor == '0':
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
        except Exception as e:
            print(f"Błąd: {e}")

def typy_ubrania_menu():
    while True:
        print("\n--- Menu Typy Ubrania ---")
        print("1. Wyświetl wszystkie typy ubrań")
        print("2. Dodaj nowy typ ubrania")
        print("3. Usuń typ ubrania")
        print("0. Powrót do głównego menu")

        wybor = input("Podaj numer opcji: ")

        try:
            if wybor == '1':
                cur.execute("SELECT * FROM Typy_ubrania")
                typy = cur.fetchall()
                for typ in typy:
                    print(typ)
            elif wybor == '2':
                nazwa = input("Podaj nazwę nowego typu ubrania: ")
                cur.execute(
                    "INSERT INTO Typy_ubrania (nazwa) VALUES (?)",
                    (nazwa,)
                )
                conn.commit()
                print("Dodano nowy typ ubrania.")
            elif wybor == '3':
                id_typu = input("Podaj ID typu ubrania do usunięcia: ")
                cur.execute("DELETE FROM Typy_ubrania WHERE id_typu_ubrania = ?", (id_typu,))
                conn.commit()
                print("Usunięto typ ubrania.")
            elif wybor == '0':
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
        except Exception as e:
            print(f"Błąd: {e}")

def ubrania_menu():
    while True:
        print("\n--- Menu Ubrania ---")
        print("1. Wyświetl wszystkie ubrania")
        print("2. Dodaj nowe ubranie")
        print("3. Usuń ubranie")
        print("0. Powrót do głównego menu")

        wybor = input("Podaj numer opcji: ")

        try:
            if wybor == '1':
                cur.execute("SELECT * FROM Ubrania")
                ubrania = cur.fetchall()
                for ubranie in ubrania:
                    print(ubranie)
            elif wybor == '2':
                nazwa = input("Podaj nazwę nowego ubrania: ")
                id_typu = input("Podaj ID typu ubrania: ")
                cur.execute(
                    "INSERT INTO Ubrania (nazwa, id_typu) VALUES (?, ?)",
                    (nazwa, id_typu)
                )
                conn.commit()
                print("Dodano nowe ubranie.")
            elif wybor == '3':
                id_ubrania = input("Podaj ID ubrania do usunięcia: ")
                cur.execute("DELETE FROM Ubrania WHERE id_ubrania = ?", (id_ubrania,))
                conn.commit()
                print("Usunięto ubranie.")
            elif wybor == '0':
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
        except Exception as e:
            print(f"Błąd: {e}")

def typy_uslugi_menu():
    while True:
        print("\n--- Menu Typy Usługi ---")
        print("1. Wyświetl wszystkie typy usług")
        print("2. Dodaj nowy typ usługi")
        print("3. Usuń typ usługi")
        print("0. Powrót do głównego menu")

        wybor = input("Podaj numer opcji: ")

        try:
            if wybor == '1':
                cur.execute("SELECT * FROM Typy_uslugi")
                typy_uslugi = cur.fetchall()
                for typ in typy_uslugi:
                    print(typ)
            elif wybor == '2':
                nazwa = input("Podaj nazwę nowego typu usługi: ")
                cur.execute(
                    "INSERT INTO Typy_uslugi (nazwa) VALUES (?)",
                    (nazwa,)
                )
                conn.commit()
                print("Dodano nowy typ usługi.")
            elif wybor == '3':
                id_typu_uslugi = input("Podaj ID typu usługi do usunięcia: ")
                cur.execute("DELETE FROM Typy_uslugi WHERE id_typu_uslugi = ?", (id_typu_uslugi,))
                conn.commit()
                print("Usunięto typ usługi.")
            elif wybor == '0':
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
        except Exception as e:
            print(f"Błąd: {e}")

def uslugi_menu():
    while True:
        print("\n--- Menu Usługi ---")
        print("1. Wyświetl wszystkie usługi")
        print("2. Dodaj nową usługę")
        print("3. Usuń usługę")
        print("0. Powrót do głównego menu")

        wybor = input("Podaj numer opcji: ")

        try:
            if wybor == '1':
                cur.execute("SELECT * FROM Usługi")
                uslugi = cur.fetchall()
                for usluga in uslugi:
                    print(usluga)
            elif wybor == '2':
                nazwa = input("Podaj nazwę nowej usługi: ")
                id_typu_uslugi = input("Podaj ID typu usługi: ")
                cur.execute(
                    "INSERT INTO Usługi (nazwa, id_typu_uslugi) VALUES (?, ?)",
                    (nazwa, id_typu_uslugi)
                )
                conn.commit()
                print("Dodano nową usługę.")
            elif wybor == '3':
                id_uslugi = input("Podaj ID usługi do usunięcia: ")
                cur.execute("DELETE FROM Usługi WHERE id_usługi = ?", (id_uslugi,))
                conn.commit()
                print("Usunięto usługę.")
            elif wybor == '0':
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
        except Exception as e:
            print(f"Błąd: {e}")

def menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Zamówienia")
        print("2. Goście")
        print("3. Typy ubrania")
        print("4. Ubrania")
        print("5. Typy usługi")
        print("6. Usługi")
        print("0. Wyjście")

        wybor = input("Podaj numer opcji: ")

        if wybor == '1':
            print("Wybrano Zamówienia")
            zamowienia_menu()
        elif wybor == '2':
            print("Wybrano Goście")
            goscie_menu()
        elif wybor == '3':
            print("Wybrano Typy ubrania")
            typy_ubrania_menu()
        elif wybor == '4':
            print("Wybrano Ubrania")
            ubrania_menu()
        elif wybor == '5':
            print("Wybrano Typy usługi")
            typy_uslugi_menu()
        elif wybor == '6':
            print("Wybrano Usługi")
            uslugi_menu()
        elif wybor == '0':
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
menu()

conn.close()

