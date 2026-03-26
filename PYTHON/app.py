from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Funkcja do pobierania aktywnych użytkowników
def get_active_users():
    conn = sqlite3.connect('DB/app_data.db')  # Połączenie z bazą danych
    cursor = conn.cursor()
    cursor.execute('''SELECT username FROM "Customers" WHERE active = TRUE''')
    active_users = cursor.fetchall()
    conn.close()
    
    # Zwracamy listę samych nicków
    return [user[0] for user in active_users]

@app.route('/')
def index():
    active_users = get_active_users()  # Pobieramy aktywnych użytkowników
    return render_template('index.html', users=active_users)  # Przekazujemy do HTML

@app.route('/get_active_users', methods=['GET'])
def get_active_users_json():
    """Endpoint, który zwraca aktywnych użytkowników w formacie JSON"""
    active_users = get_active_users()  # Pobieramy aktywnych użytkowników
    return jsonify(active_users)  # Zwracamy dane w formacie JSON

if __name__ == "__main__":
    app.run(debug=True)