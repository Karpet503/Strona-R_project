import sqlite3
import json

def get_active_users():
    """Pobiera aktywnych użytkowników z bazy danych i zapisuje je w formacie JSON"""
    conn = sqlite3.connect('app_data.db')  # Połączenie z bazą danych
    cursor = conn.cursor()
    cursor.execute('''SELECT username FROM "Customers" WHERE active = TRUE''')  # Wybieramy aktywnych użytkowników
    active_users = cursor.fetchall()  # Pobieramy wszystkich aktywnych użytkowników
    conn.close()
    
    # Zwracamy tylko nicki użytkowników
    return [user[0] for user in active_users]

def save_active_users_to_file():
    """Zapisuje dane aktywnych użytkowników do pliku JSON"""
    active_users = get_active_users()
    
    with open('../JS/active_users.json', 'w') as f:
        json.dump(active_users, f)

# Wywołanie funkcji, żeby od razu zapisać dane
save_active_users_to_file()