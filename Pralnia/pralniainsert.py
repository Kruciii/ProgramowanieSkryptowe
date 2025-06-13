import sqlite3
conn = sqlite3.connect('pralnia.db')
cur = conn.cursor()
def wykonaj_wstawianie_danych():
    conn = sqlite3.connect('pralnia.db')
    cur = conn.cursor()

    # Włączenie obsługi kluczy obcych
    cur.execute("PRAGMA foreign_keys = ON;")

    try:
        # Hotele
        cur.executemany("INSERT INTO Hotele (nazwa, adres) VALUES (?, ?)", [
            ('Hotel Wawel', 'Kraków, ul. Grodzka 12'),
            ('Hotel Bałtyk', 'Gdynia, ul. Morska 45')
        ])

        # Pralnie
        cur.executemany("INSERT INTO Pralnie (opis, id_hotelu) VALUES (?, ?)", [
            ('Pralnia główna', 1),
            ('Pralnia nadmorska', 2)
        ])

        # Specjalizacje
        cur.executemany("INSERT INTO Specjalizacje (nazwa) VALUES (?)", [
            ('Pranie chemiczne',),
            ('Prasowanie',),
            ('Czyszczenie parowe',)
        ])

        # Pracownicy
        cur.executemany("INSERT INTO Pracownicy (imię, nazwisko, id_specjalizacji) VALUES (?, ?, ?)", [
            ('Anna', 'Kowalska', 1),
            ('Jan', 'Nowak', 2),
            ('Maria', 'Szpak', 3)
        ])

        # Pracownicy_w_pralni
        cur.executemany("INSERT INTO Pracownicy_w_pralni (id_pracownika, id_pralni) VALUES (?, ?)", [
            (1, 1),
            (2, 1),
            (3, 2)
        ])

        # Goście
        cur.executemany("INSERT INTO Goście (imię, nazwisko, telefon) VALUES (?, ?, ?)", [
            ('Piotr', 'Malinowski', '501234567'),
            ('Katarzyna', 'Lis', '502345678')
        ])

        # Zamówienia
        cur.executemany("INSERT INTO Zamówienia (data_złożenia, data_zakończenia, id_gościa) VALUES (?, ?, ?)", [
            ('2025-06-01', '2025-06-02', 1),
            ('2025-06-03', None, 2)
        ])

        # Typy_ubrania
        cur.executemany("INSERT INTO Typy_ubrania (nazwa) VALUES (?)", [
            ('Koszula',),
            ('Spódnica',),
            ('Garnitur',)
        ])

        # Ubrania
        cur.executemany("INSERT INTO Ubrania (id_zamówienia, id_typu_ubrania) VALUES (?, ?)", [
            (1, 1),
            (1, 3),
            (2, 2)
        ])

        # Typy_usługi
        cur.executemany("INSERT INTO Typy_usługi (nazwa, cena) VALUES (?, ?)", [
            ('Pranie', 25.00),
            ('Prasowanie', 15.00),
            ('Czyszczenie parowe', 30.00)
        ])

        # Usługi
        cur.executemany("INSERT INTO Usługi (id_typu_usługi, id_pracownika, id_ubrania) VALUES (?, ?, ?)", [
            (1, 1, 1),
            (2, 2, 1),
            (3, 3, 3)
        ])

        conn.commit()
        print("Dane zostały pomyślnie dodane.")
    except sqlite3.Error as e:
        print("Błąd podczas wstawiania danych:", e)
        conn.rollback()
    finally:
        conn.close()

# Wywołanie funkcji
wykonaj_wstawianie_danych()
