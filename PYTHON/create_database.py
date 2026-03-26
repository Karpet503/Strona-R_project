import sqlite3

# Połączenie z bazą danych (baza zostanie utworzona, jeśli nie istnieje)
conn = sqlite3.connect('app_data.db')
cursor = conn.cursor()

# Tworzymy tabelę 'Customers' (jeśli nie istnieje)
cursor.execute('''CREATE TABLE IF NOT EXISTS "Customers" (
  id integer PRIMARY KEY,
  username varchar(100) UNIQUE,
  computer varchar(100),
  email varchar(50),
  telefon_num VARCHAR(12),
  last_log date,
  active bool
)''')

# Tworzymy tabelę 'Owner' (jeśli nie istnieje)
cursor.execute('''CREATE TABLE IF NOT EXISTS "Owner" (
  id integer PRIMARY KEY,
  computer varchar(100) UNIQUE,
  owner varchar(100)
)''')

# Tworzymy tabelę 'Usage' (jeśli nie istnieje)
cursor.execute('''CREATE TABLE IF NOT EXISTS "Usage" (
  computer varchar(100) PRIMARY KEY,
  cpu_usage varchar(15),
  cpu_core_all varchar(4),
  ram_in_use varchar(10),
  ram_avaible varchar(10),
  ram_total varchar(10),
  disk_usage varchar(10),
  owner_id INTEGER,
  user_id INTEGER,
  FOREIGN KEY(owner_id) REFERENCES "Owner"(id),
  FOREIGN KEY(user_id) REFERENCES "Customers"(id)
)''')

# Dodajemy przykładowych użytkowników do tabeli 'Customers'
cursor.execute('''INSERT INTO "Customers" (username, computer, email, telefon_num, last_log, active) 
    VALUES ('Testowus_ruchomus', 'Pc_nr_one', 'test@test.pl', '123321123', '2026-03-26', TRUE)''')

# Zapisujemy zmiany
conn.commit()

# Zamykamy połączenie
conn.close()