import sqlite3

# Tworzy (lub otwiera) plik bazy danych
conn = sqlite3.connect('pralnia.db')
cur = conn.cursor()

# Włącza obsługę kluczy obcych (domyślnie wyłączona w SQLite)
cur.execute("PRAGMA foreign_keys = ON;")

# Tworzenie tabel
cur.executescript('''
CREATE TABLE IF NOT EXISTS Hotele (
    id_hotelu INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT NOT NULL,
    adres TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Pralnie (
    id_pralni INTEGER PRIMARY KEY AUTOINCREMENT,
    opis TEXT,
    id_hotelu INTEGER NOT NULL,
    FOREIGN KEY (id_hotelu) REFERENCES Hotele(id_hotelu)
);

CREATE TABLE IF NOT EXISTS Specjalizacje (
    id_specjalizacji INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Pracownicy (
    id_pracownika INTEGER PRIMARY KEY AUTOINCREMENT,
    imię TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    id_specjalizacji INTEGER NOT NULL,
    FOREIGN KEY (id_specjalizacji) REFERENCES Specjalizacje(id_specjalizacji)
);

CREATE TABLE IF NOT EXISTS Pracownicy_w_pralni (
    id_pracownika_w_pralni INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pracownika INTEGER NOT NULL,
    id_pralni INTEGER NOT NULL,
    FOREIGN KEY (id_pracownika) REFERENCES Pracownicy(id_pracownika),
    FOREIGN KEY (id_pralni) REFERENCES Pralnie(id_pralni)
);

CREATE TABLE IF NOT EXISTS Goście (
    id_gościa INTEGER PRIMARY KEY AUTOINCREMENT,
    imię TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    telefon TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Zamówienia (
    id_zamówienia INTEGER PRIMARY KEY AUTOINCREMENT,
    data_złożenia DATE NOT NULL,
    data_zakończenia DATE,
    id_gościa INTEGER NOT NULL,
    FOREIGN KEY (id_gościa) REFERENCES Goście(id_gościa)
);

CREATE TABLE IF NOT EXISTS Typy_ubrania (
    id_typu_ubrania INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Ubrania (
    id_ubrania INTEGER PRIMARY KEY AUTOINCREMENT,
    id_zamówienia INTEGER NOT NULL,
    id_typu_ubrania INTEGER NOT NULL,
    FOREIGN KEY (id_zamówienia) REFERENCES Zamówienia(id_zamówienia),
    FOREIGN KEY (id_typu_ubrania) REFERENCES Typy_ubrania(id_typu_ubrania)
);

CREATE TABLE IF NOT EXISTS Typy_usługi (
    id_typu_usługi INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT NOT NULL,
    cena DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Usługi (
    id_usługi INTEGER PRIMARY KEY AUTOINCREMENT,
    id_typu_usługi INTEGER NOT NULL,
    id_pracownika INTEGER NOT NULL,
    id_ubrania INTEGER NOT NULL,
    FOREIGN KEY (id_typu_usługi) REFERENCES Typy_usługi(id_typu_usługi),
    FOREIGN KEY (id_pracownika) REFERENCES Pracownicy(id_pracownika),
    FOREIGN KEY (id_ubrania) REFERENCES Ubrania(id_ubrania)
);
''')

# Zatwierdza zmiany i zamyka połączenie
conn.commit()
conn.close()
