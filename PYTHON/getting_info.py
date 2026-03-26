import sqlite3

def get_active_users():
    """Funkcja do pobierania aktywnych użytkowników z bazy danych"""
    conn = sqlite3.connect('app_data.db')  # Używamy bazy w folderze 'DB'
    cursor = conn.cursor()
    cursor.execute('''SELECT username FROM "Customers" WHERE active = TRUE''')  # Wybieramy aktywnych użytkowników
    active_users = cursor.fetchall()  # Zwraca listę krotek z nickami
    conn.close()
    
    # Zwracamy tylko nicki użytkowników
    return [user[0] for user in active_users]

# Przykładowe wywołanie funkcji
active_users = get_active_users()
print(active_users)  # Wypisanie aktywnych użytkowników