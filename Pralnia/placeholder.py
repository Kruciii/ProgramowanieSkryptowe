
def goscie():
    cur.execute("SELECT * FROM Goście")
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak gości w bazie danych.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Imię: {w[1]}, Nazwisko: {w[2]}, Telefon: {w[3]}")
def goscie_id(id_gościa):
    cur.execute("SELECT * FROM Goście WHERE id_gościa = ?", (id_gościa,))
    wynik = cur.fetchone()
    
    if wynik:
        print(f"ID: {wynik[0]}, Imię: {wynik[1]}, Nazwisko: {wynik[2]}, Telefon: {wynik[3]}")
    else:
        print("Nie znaleziono gościa o podanym ID.")
def goscie_naziwsko(nazwisko):
    cur.execute("SELECT * FROM Goście WHERE nazwisko = ?", (nazwisko,))
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak gości o podanym nazwisku.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Imię: {w[1]}, Nazwisko: {w[2]}, Telefon: {w[3]}")
def goscie_edytuj(id_gościa, imię, nazwisko, telefon):
    cur.execute("UPDATE Goście SET imię = ?, nazwisko = ?, telefon = ? WHERE id_gościa = ?", (imię, nazwisko, telefon, id_gościa))
    conn.commit()
    print("Dane gościa zostały zaktualizowane.")
def goscie_dodaj(imię, nazwisko, telefon):
    cur.execute("INSERT INTO Goście (imię, nazwisko, telefon) VALUES (?, ?, ?)", (imię, nazwisko, telefon))
    conn.commit()
    print("Nowy gość został dodany.")
def goscie_usun(id_gościa):
    cur.execute("DELETE FROM Goście WHERE id_gościa = ?", (id_gościa,))
    conn.commit()
    print("Gość został usunięty z bazy danych.")
def goscie_menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Wyświetl wszystkich gości")
        print("2. Wyświetl gościa po ID")
        print("3. Wyświetl gościa po nazwisku")
        print("4. Edytuj dane gościa")
        print("5. Dodaj nowego gościa")
        print("6. Usuń gościa")
        print("0. Powrót do menu głównego")

        wybor = input("Podaj numer opcji: ")

        if wybor == '1':
            goscie()
        elif wybor == '2':
            id_gościa = int(input("Podaj ID gościa: "))
            goscie_id(id_gościa)
        elif wybor == '3':
            nazwisko = input("Podaj nazwisko gościa: ")
            goscie_naziwsko(nazwisko)
        elif wybor == '4':
            id_gościa = int(input("Podaj ID gościa do edycji: "))
            imię = input("Podaj nowe imię: ")
            nazwisko = input("Podaj nowe nazwisko: ")
            telefon = input("Podaj nowy telefon: ")
            goscie_edytuj(id_gościa, imię, nazwisko, telefon)
        elif wybor == '5':
            imię = input("Podaj imię nowego gościa: ")
            nazwisko = input("Podaj nazwisko nowego gościa: ")
            telefon = input("Podaj telefon nowego gościa: ")
            goscie_dodaj(imię, nazwisko, telefon)
        elif wybor == '6':
            id_gościa = int(input("Podaj ID gościa do usunięcia: "))
            goscie_usun(id_gościa)
        elif wybor == '0':
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
def pracownicy():
    cur.execute("SELECT * FROM Pracownicy")
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak pracowników w bazie danych.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Imię: {w[1]}, Nazwisko: {w[2]}, Specjalizacja ID: {w[3]}")
def pracownicy_id(id_pracownika):
    cur.execute("SELECT * FROM Pracownicy WHERE id_pracownika = ?", (id_pracownika,))
    wynik = cur.fetchone()
    
    if wynik:
        print(f"ID: {wynik[0]}, Imię: {wynik[1]}, Nazwisko: {wynik[2]}, Specjalizacja ID: {wynik[3]}")
    else:
        print("Nie znaleziono pracownika o podanym ID.")
def pracownicy_nazwisko(nazwisko):
    cur.execute("SELECT * FROM Pracownicy WHERE nazwisko = ?", (nazwisko,))
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak pracowników o podanym nazwisku.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Imię: {w[1]}, Nazwisko: {w[2]}, Specjalizacja ID: {w[3]}")
def pracownicy_edytuj(id_pracownika, imię, nazwisko, id_specjalizacji):
    cur.execute("UPDATE Pracownicy SET imię = ?, nazwisko = ?, id_specjalizacji = ? WHERE id_pracownika = ?", (imię, nazwisko, id_specjalizacji, id_pracownika))
    conn.commit()
    print("Dane pracownika zostały zaktualizowane.")
def pracownicy_dodaj(imię, nazwisko, id_specjalizacji):
    cur.execute("INSERT INTO Pracownicy (imię, nazwisko, id_specjalizacji) VALUES (?, ?, ?)", (imię, nazwisko, id_specjalizacji))
    conn.commit()
    print("Nowy pracownik został dodany.")
def pracownicy_usun(id_pracownika):
    cur.execute("DELETE FROM Pracownicy WHERE id_pracownika = ?", (id_pracownika,))
    conn.commit()
    print("Pracownik został usunięty z bazy danych.")
def pracownicy_menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Wyświetl wszystkich pracowników")
        print("2. Wyświetl pracownika po ID")
        print("3. Wyświetl pracownika po nazwisku")
        print("4. Edytuj dane pracownika")
        print("5. Dodaj nowego pracownika")
        print("6. Usuń pracownika")
        print("0. Powrót do menu głównego")

        wybor = input("Podaj numer opcji: ")

        if wybor == '1':
            pracownicy()
        elif wybor == '2':
            id_pracownika = int(input("Podaj ID pracownika: "))
            pracownicy_id(id_pracownika)
        elif wybor == '3':
            nazwisko = input("Podaj nazwisko pracownika: ")
            pracownicy_nazwisko(nazwisko)
        elif wybor == '4':
            id_pracownika = int(input("Podaj ID pracownika do edycji: "))
            imię = input("Podaj nowe imię: ")
            nazwisko = input("Podaj nowe nazwisko: ")
            id_specjalizacji = int(input("Podaj ID specjalizacji: "))
            pracownicy_edytuj(id_pracownika, imię, nazwisko, id_specjalizacji)
        elif wybor == '5':
            imię = input("Podaj imię nowego pracownika: ")
            nazwisko = input("Podaj nazwisko nowego pracownika: ")
            id_specjalizacji = int(input("Podaj ID specjalizacji nowego pracownika: "))
            pracownicy_dodaj(imię, nazwisko, id_specjalizacji)
        elif wybor == '6':
            id_pracownika = int(input("Podaj ID pracownika do usunięcia: "))
            pracownicy_usun(id_pracownika)
        elif wybor == '0':
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
def specjalizacje():
    cur.execute("SELECT * FROM Specjalizacje")
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak specjalizacji w bazie danych.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Nazwa: {w[1]}")
def specjalizacje_id(id_specjalizacji):
    cur.execute("SELECT * FROM Specjalizacje WHERE id_specjalizacji = ?", (id_specjalizacji,))
    wynik = cur.fetchone()
    
    if wynik:
        print(f"ID: {wynik[0]}, Nazwa: {wynik[1]}")
    else:
        print("Nie znaleziono specjalizacji o podanym ID.")
def specjalizacje_nazwa(nazwa):
    cur.execute("SELECT * FROM Specjalizacje WHERE nazwa = ?", (nazwa,))
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak specjalizacji o podanej nazwie.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Nazwa: {w[1]}")
def specjalizacje_edytuj(id_specjalizacji, nazwa):
    cur.execute("UPDATE Specjalizacje SET nazwa = ? WHERE id_specjalizacji = ?", (nazwa, id_specjalizacji))
    conn.commit()
    print("Dane specjalizacji zostały zaktualizowane.")
def specjalizacje_dodaj(nazwa):
    cur.execute("INSERT INTO Specjalizacje (nazwa) VALUES (?)", (nazwa,))
    conn.commit()
    print("Nowa specjalizacja została dodana.")
def specjalizacje_usun(id_specjalizacji):
    cur.execute("DELETE FROM Specjalizacje WHERE id_specjalizacji = ?", (id_specjalizacji,))
    conn.commit()
    print("Specjalizacja została usunięta z bazy danych.")
def specjalizacje_menu():
    
    while True:
        print("\nWybierz opcję:")
        print("1. Wyświetl wszystkie specjalizacje")
        print("2. Wyświetl specjalizację po ID")
        print("3. Wyświetl specjalizację po nazwie")
        print("4. Edytuj dane specjalizacji")
        print("5. Dodaj nową specjalizację")
        print("6. Usuń specjalizację")
        print("0. Powrót do menu głównego")

        wybor = input("Podaj numer opcji: ")

        if wybor == '1':
            specjalizacje()
        elif wybor == '2':
            id_specjalizacji = int(input("Podaj ID specjalizacji: "))
            specjalizacje_id(id_specjalizacji)
        elif wybor == '3':
            nazwa = input("Podaj nazwę specjalizacji: ")
            specjalizacje_nazwa(nazwa)
        elif wybor == '4':
            id_specjalizacji = int(input("Podaj ID specjalizacji do edycji: "))
            nazwa = input("Podaj nową nazwę: ")
            specjalizacje_edytuj(id_specjalizacji, nazwa)
        elif wybor == '5':
            nazwa = input("Podaj nazwę nowej specjalizacji: ")
            specjalizacje_dodaj(nazwa)
        elif wybor == '6':
            id_specjalizacji = int(input("Podaj ID specjalizacji do usunięcia: "))
            specjalizacje_usun(id_specjalizacji)
        elif wybor == '0':
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
def typy_ubrania():
    cur.execute("SELECT * FROM Typy_ubrania")
    wyniki = cur.fetchall()
    if not wyniki:
        print("Brak typów ubrań w bazie danych.")
        return
    for w in wyniki:
        print(f"ID: {w[0]}, Nazwa: {w[1]}")
def typy_ubrania_id(id_typu_ubrania):
    cur.execute("SELECT * FROM Typy_ubrania WHERE id_typu_ubrania = ?", (id_typu_ubrania,))
    wynik = cur.fetchone()
    
    if wynik:
        print(f"ID: {wynik[0]}, Nazwa: {wynik[1]}")
    else:
        print("Nie znaleziono typu ubrania o podanym ID.")
def typy_ubrania_nazwa(nazwa):
    cur.execute("SELECT * FROM Typy_ubrania WHERE nazwa = ?", (nazwa,))
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak typów ubrań o podanej nazwie.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Nazwa: {w[1]}")
def typy_ubrania_edytuj(id_typu_ubrania, nazwa):
    cur.execute("UPDATE Typy_ubrania SET nazwa = ? WHERE id_typu_ubrania = ?", (nazwa, id_typu_ubrania))
    conn.commit()
    print("Dane typu ubrania zostały zaktualizowane.")
def typy_ubrania_dodaj(nazwa):
    cur.execute("INSERT INTO Typy_ubrania (nazwa) VALUES (?)", (nazwa,))
    conn.commit()
    print("Nowy typ ubrania został dodany.")
def typy_ubrania_usun(id_typu_ubrania):
    cur.execute("DELETE FROM Typy_ubrania WHERE id_typu_ubrania = ?", (id_typu_ubrania,))
    conn.commit()
    print("Typ ubrania został usunięty z bazy danych.")
def typy_ubrania_menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Wyświetl wszystkie typy ubrań")
        print("2. Wyświetl typ ubrania po ID")
        print("3. Wyświetl typ ubrania po nazwie")
        print("4. Edytuj dane typu ubrania")
        print("5. Dodaj nowy typ ubrania")
        print("6. Usuń typ ubrania")
        print("0. Powrót do menu głównego")

        wybor = input("Podaj numer opcji: ")

        if wybor == '1':
            typy_ubrania()
        elif wybor == '2':
            id_typu_ubrania = int(input("Podaj ID typu ubrania: "))
            typy_ubrania_id(id_typu_ubrania)
        elif wybor == '3':
            nazwa = input("Podaj nazwę typu ubrania: ")
            typy_ubrania_nazwa(nazwa)
        elif wybor == '4':
            id_typu_ubrania = int(input("Podaj ID typu ubrania do edycji: "))
            nazwa = input("Podaj nową nazwę: ")
            typy_ubrania_edytuj(id_typu_ubrania, nazwa)
        elif wybor == '5':
            nazwa = input("Podaj nazwę nowego typu ubrania: ")
            typy_ubrania_dodaj(nazwa)
        elif wybor == '6':
            id_typu_ubrania = int(input("Podaj ID typu ubrania do usunięcia: "))
            typy_ubrania_usun(id_typu_ubrania)
        elif wybor == '0':
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
def ubrania():
    cur.execute("SELECT * FROM Ubrania")
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak ubrań w bazie danych.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Zamówienie ID: {w[1]}, Typ ubrania ID: {w[2]}")
def ubrania_id(id_ubrania):
    cur.execute("SELECT * FROM Ubrania WHERE id_ubrania = ?", (id_ubrania,))
    wynik = cur.fetchone()
    
    if wynik:
        print(f"ID: {wynik[0]}, Zamówienie ID: {wynik[1]}, Typ ubrania ID: {wynik[2]}")
    else:
        print("Nie znaleziono ubrania o podanym ID.")
def ubrania_zamowienie_id(id_zamówienia):
    cur.execute("SELECT * FROM Ubrania WHERE id_zamówienia = ?", (id_zamówienia,))
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak ubrań dla podanego zamówienia.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Zamówienie ID: {w[1]}, Typ ubrania ID: {w[2]}")
def ubrania_typ_id(id_typu_ubrania):
    cur.execute("SELECT * FROM Ubrania WHERE id_typu_ubrania = ?", (id_typu_ubrania,))
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak ubrań dla podanego typu ubrania.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Zamówienie ID: {w[1]}, Typ ubrania ID: {w[2]}")
def ubrania_edytuj(id_ubrania, id_zamówienia, id_typu_ubrania):
    cur.execute("UPDATE Ubrania SET id_zamówienia = ?, id_typu_ubrania = ? WHERE id_ubrania = ?", (id_zamówienia, id_typu_ubrania, id_ubrania))
    conn.commit()
    print("Dane ubrania zostały zaktualizowane.")

def ubrania_dodaj(id_zamówienia, id_typu_ubrania):
    cur.execute("INSERT INTO Ubrania (id_zamówienia, id_typu_ubrania) VALUES (?, ?)", (id_zamówienia, id_typu_ubrania))
    conn.commit()
    print("Nowe ubranie zostało dodane.")
def ubrania_usun(id_ubrania):
    cur.execute("DELETE FROM Ubrania WHERE id_ubrania = ?", (id_ubrania,))
    conn.commit()
    print("Ubranie zostało usunięte z bazy danych.")
def ubrania_menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Wyświetl wszystkie ubrania")
        print("2. Wyświetl ubranie po ID")
        print("3. Wyświetl ubrania po ID zamówienia")
        print("4. Wyświetl ubrania po ID typu ubrania")
        print("5. Edytuj dane ubrania")
        print("6. Dodaj nowe ubranie")
        print("7. Usuń ubranie")
        print("0. Powrót do menu głównego")

        wybor = input("Podaj numer opcji: ")

        if wybor == '1':
            ubrania()
        elif wybor == '2':
            id_ubrania = int(input("Podaj ID ubrania: "))
            ubrania_id(id_ubrania)
        elif wybor == '3':
            id_zamówienia = int(input("Podaj ID zamówienia: "))
            ubrania_zamowienie_id(id_zamówienia)
        elif wybor == '4':
            id_typu_ubrania = int(input("Podaj ID typu ubrania: "))
            ubrania_typ_id(id_typu_ubrania)
        elif wybor == '5':
            id_ubrania = int(input("Podaj ID ubrania do edycji: "))
            id_zamówienia = int(input("Podaj nowe ID zamówienia: "))
            id_typu_ubrania = int(input("Podaj nowe ID typu ubrania: "))
            ubrania_edytuj(id_ubrania, id_zamówienia, id_typu_ubrania)
        elif wybor == '6':
            id_zamówienia = int(input("Podaj ID zamówienia nowego ubrania: "))
            id_typu_ubrania = int(input("Podaj ID typu nowego ubrania: "))
            ubrania_dodaj(id_zamówienia, id_typu_ubrania)
        elif wybor == '7':
            id_ubrania = int(input("Podaj ID ubrania do usunięcia: "))
            ubrania_usun(id_ubrania)
        elif wybor == '0':
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
def typy_uslugi():
    cur.execute("SELECT * FROM Typy_usługi")
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak typów usług w bazie danych.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Nazwa: {w[1]}, Cena: {w[2]}")
def typy_uslugi_id(id_typu_usługi):
    cur.execute("SELECT * FROM Typy_usługi WHERE id_typu_usługi = ?", (id_typu_usługi,))
    wynik = cur.fetchone()
    
    if wynik:
        print(f"ID: {wynik[0]}, Nazwa: {wynik[1]}, Cena: {wynik[2]}")
    else:
        print("Nie znaleziono typu usługi o podanym ID.")
def typy_uslugi_nazwa(nazwa):
    cur.execute("SELECT * FROM Typy_usługi WHERE nazwa = ?", (nazwa,))
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak typów usług o podanej nazwie.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Nazwa: {w[1]}, Cena: {w[2]}")
def typy_uslugi_edytuj(id_typu_usługi, nazwa, cena):
    cur.execute("UPDATE Typy_usługi SET nazwa = ?, cena = ? WHERE id_typu_usługi = ?", (nazwa, cena, id_typu_usługi))
    conn.commit()
    print("Dane typu usługi zostały zaktualizowane.")
def typy_uslugi_dodaj(nazwa, cena):
    cur.execute("INSERT INTO Typy_usługi (nazwa, cena) VALUES (?, ?)", (nazwa, cena))
    conn.commit()
    print("Nowy typ usługi został dodany.")
def typy_uslugi_usun(id_typu_usługi):
    cur.execute("DELETE FROM Typy_usługi WHERE id_typu_usługi = ?", (id_typu_usługi,))
    conn.commit()
    print("Typ usługi został usunięty z bazy danych.")
def typy_uslugi_menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Wyświetl wszystkie typy usług")
        print("2. Wyświetl typ usługi po ID")
        print("3. Wyświetl typ usługi po nazwie")
        print("4. Edytuj dane typu usługi")
        print("5. Dodaj nowy typ usługi")
        print("6. Usuń typ usługi")
        print("0. Powrót do menu głównego")

        wybor = input("Podaj numer opcji: ")

        if wybor == '1':
            typy_uslugi()
        elif wybor == '2':
            id_typu_usługi = int(input("Podaj ID typu usługi: "))
            typy_uslugi_id(id_typu_usługi)
        elif wybor == '3':
            nazwa = input("Podaj nazwę typu usługi: ")
            typy_uslugi_nazwa(nazwa)
        elif wybor == '4':
            id_typu_usługi = int(input("Podaj ID typu usługi do edycji: "))
            nazwa = input("Podaj nową nazwę: ")
            cena = float(input("Podaj nową cenę: "))
            typy_uslugi_edytuj(id_typu_usługi, nazwa, cena)
        elif wybor == '5':
            nazwa = input("Podaj nazwę nowego typu usługi: ")
            cena = float(input("Podaj cenę nowego typu usługi: "))
            typy_uslugi_dodaj(nazwa, cena)
        elif wybor == '6':
            id_typu_usługi = int(input("Podaj ID typu usługi do usunięcia: "))
            typy_uslugi_usun(id_typu_usługi)
        elif wybor == '0':
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
def uslugi():
    cur.execute("SELECT * FROM Usługi")
    wyniki = cur.fetchall()
    
    if not wyniki:
        print("Brak usług w bazie danych.")
        return
    
    for w in wyniki:
        print(f"ID: {w[0]}, Typ usługi ID: {w[1]}, Pracownik ID: {w[2]}, Ubranie ID: {w[3]}")
        
while(True):
    uzytkownik =""
    id = int(input("Aby zalogować podaj id uzytkownika podaj id uzytkownika"))
    if(czy_istnieje_pracownik(id)):
        print("Zalogowano")
        pobierz_pracownika_ze_specjalizacja(id)
        break
    else:
        print("nie ma takiego użytkownika")
def zamowienia_menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Wyświetl wszystkie zamówienia")
        print("2. Wyświetl zamówienie po ID")
        print("3. Wyświetl zamówienia po ID gościa")
        print("4. Edytuj zamówienie")
        print("5. Dodaj nowe zamówienie")
        print("6. Usuń zamówienie")
        print("0. Powrót do menu głównego")

        wybor = input("Podaj numer opcji: ")

        if wybor == '1':
            cur.execute("SELECT * FROM Zamówienia")
            wyniki = cur.fetchall()
            if not wyniki:
                print("Brak zamówień w bazie danych.")
            else:
                for w in wyniki:
                    print(f"ID: {w[0]}, Gość ID: {w[1]}, Data przyjęcia: {w[2]}, Data odbioru: {w[3]}")
        elif wybor == '2':
            id_zamowienia = int(input("Podaj ID zamówienia: "))
            cur.execute("SELECT * FROM Zamówienia WHERE id_zamówienia = ?", (id_zamowienia,))
            wynik = cur.fetchone()
            if wynik:
                print(f"ID: {wynik[0]}, Gość ID: {wynik[1]}, Data przyjęcia: {wynik[2]}, Data odbioru: {wynik[3]}")
            else:
                print("Nie znaleziono zamówienia o podanym ID.")
        elif wybor == '3':
            id_goscia = int(input("Podaj ID gościa: "))
            cur.execute("SELECT * FROM Zamówienia WHERE id_gościa = ?", (id_goscia,))
            wyniki = cur.fetchall()
            if not wyniki:
                print("Brak zamówień dla podanego gościa.")
            else:
                for w in wyniki:
                    print(f"ID: {w[0]}, Gość ID: {w[1]}, Data przyjęcia: {w[2]}, Data odbioru: {w[3]}")
        elif wybor == '4':
            id_zamowienia = int(input("Podaj ID zamówienia do edycji: "))
            id_goscia = int(input("Podaj nowe ID gościa: "))
            data_przyjecia = input("Podaj nową datę przyjęcia (YYYY-MM-DD): ")
            data_odbioru = input("Podaj nową datę odbioru (YYYY-MM-DD): ")
            cur.execute("UPDATE Zamówienia SET id_gościa = ?, data_przyjęcia = ?, data_odbioru = ? WHERE id_zamówienia = ?",
                        (id_goscia, data_przyjecia, data_odbioru, id_zamowienia))
            conn.commit()
            print("Dane zamówienia zostały zaktualizowane.")
        elif wybor == '5':
            id_goscia = int(input("Podaj ID gościa: "))
            data_przyjecia = input("Podaj datę przyjęcia (YYYY-MM-DD): ")
            data_odbioru = input("Podaj datę odbioru (YYYY-MM-DD): ")
            cur.execute("INSERT INTO Zamówienia (id_gościa, data_przyjęcia, data_odbioru) VALUES (?, ?, ?)",
                        (id_goscia, data_przyjecia, data_odbioru))
            conn.commit()
            print("Nowe zamówienie zostało dodane.")
        elif wybor == '6':
            id_zamowienia = int(input("Podaj ID zamówienia do usunięcia: "))
            cur.execute("DELETE FROM Zamówienia WHERE id_zamówienia = ?", (id_zamowienia,))
            conn.commit()
            print("Zamówienie zostało usunięte z bazy danych.")
        elif wybor == '0':
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
