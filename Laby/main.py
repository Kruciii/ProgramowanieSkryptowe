import sqlite3
import piwo

# Połączenie z bazą
con, cur = piwo.database_connect()

# Tworzenie tabeli i dodanie danych
piwo.database_table(cur, con)
#piwo.database_insert(cur, con)
#piwo.mocne_piwa(cur)
# Pobranie i wyświetlenie najmocniejszych piw
#cur.execute("DELETE FROM piwo")
#con.commit()

piwo.menu(cur)

# Zamknięcie połączenia
con.close()
