import sqlite3
import os
import socket
from data import memory_total, memory_available, memory_usage, cpu_usage

# Połączenie z bazą danych (baza zostanie utworzona, jeśli nie istnieje)
conn = sqlite3.connect('app_data.db')
cursor = conn.cursor()

username = os.getlogin()
device_name = socket.gethostname()

# Tworzymy tabelę 'Customers' (jeśli nie istnieje)
cursor.execute('''CREATE TABLE IF NOT EXISTS "Customers" (
  id INTEGER PRIMARY KEY,
  username VARCHAR(100) UNIQUE,
  computer VARCHAR(100),
  email VARCHAR(50),
  telefon_num VARCHAR(12),
  last_log DATE,
  active BOOL
)''')

# Tworzymy tabelę 'Owner' (jeśli nie istnieje)
cursor.execute('''CREATE TABLE IF NOT EXISTS "Owner" (
  id INTEGER PRIMARY KEY,
  computer VARCHAR(100) UNIQUE,
  owner VARCHAR(100)
)''')

# Tworzymy tabelę 'Usage' (jeśli nie istnieje)
cursor.execute('''CREATE TABLE IF NOT EXISTS "Usage" (
  computer VARCHAR(100) PRIMARY KEY,
  cpu_usage VARCHAR(15),
  memory_total VARCHAR(10),
  memory_available VARCHAR(10),
  memory_usage VARCHAR(10)
)''')

# Zapytanie do dodania danych do tabeli 'Usage'
query_system_stats = '''
INSERT INTO Usage (computer, cpu_usage, memory_total, memory_available, memory_usage)
VALUES (?, ?, ?, ?, ?)
'''

# Dodajemy przykładowych użytkowników do tabeli 'Customers'
cursor.execute('''INSERT INTO "Customers" (username, computer, email, telefon_num, last_log, active) 
    VALUES (?, ?, ?, ?, ?, ?)''', ('User', device_name, 'test@test.pl', '123321123', '2026-03-26', True))

# Dodajemy właściciela komputera do tabeli 'Owner'
cursor.execute('''INSERT INTO "Owner" (computer, owner) 
    VALUES (?, ?)''', (device_name, 'Owner Name'))

# Wstawiamy dane do tabeli 'Usage' - używamy zmiennych przekazanych z `data.py`
cursor.execute(query_system_stats, (device_name, cpu_usage, memory_total, memory_available, memory_usage))

# Zapisujemy zmiany
conn.commit()

# Zamykamy połączenie
conn.close()

print("Dane zostały zapisane do bazy danych.")