import os
import sqlite3
from flask import Flask, render_template, request, jsonify, send_from_directory
import threading
import time
import subprocess
import data
#zabezpieczenie hasła biblioteka
#from werkzeug.security import generate_password_hash, check_password_hash
# Skróty pod ścieżki, BASE_DIR - z automaty podnosi o poziom foldery, by łatwiej się wpisywało ścieżki reszty folderów.
#BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#ścieżka do folderu  
DATABASE = os.path.join(BASE_DIR, "app_data.db")
#ścieżka do folderu template
TEMPLATE_DIR = os.path.join(BASE_DIR, "../templates")
#ścieżka do folderu JS
JS_DIR = os.path.join(BASE_DIR, "../JS")
#ścieżka do folderu CSS
CSS_DIR = os.path.join(BASE_DIR, "../CSS")
#ścieżka do folderu IMAGES
IMG_DIR = os.path.join(BASE_DIR, "../IMAGES")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

def run_script():
    while True:
        subprocess.run(["python", "info_usage.py"])
        time.sleep(5)

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/body.html")
def body():
    return render_template("/body.html")


@app.route("/JS/<path:filename>")
def serve_js(filename):
    return send_from_directory(JS_DIR, filename)


@app.route("/CSS/<path:filename>")
def serve_css(filename):
    return send_from_directory(CSS_DIR, filename)


@app.route("/IMAGES/<path:filename>")
def serve_img(filename):
    return send_from_directory(IMG_DIR, filename)

# Nasłuch na komende "/addCustomer" z metodą POST. Jak wygryje to dodaje to tabeli CUSTOMERS.
@app.route("/addCustomer", methods=["POST"])
def add_customer():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")


    if not username or not password or not email:
        return jsonify({
            "success": False,
            "message": "Brak danych we wszsytkich polach."
        }), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Customers (username, password, email, active)
            VALUES (?, ?, ?, ?)
        """, (username, password, email, True))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Rejestracja udana."
        })

    except sqlite3.IntegrityError:
        return jsonify({
            "success": False,
            "message": "Użytkownik już istnieje."
        }), 400

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
    }), 500

@app.route("/Login", methods=["POST"])
def login():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        data = request.get_json()
        email_login = data.get("email_login")
        password_login = data.get("password_login")

        cursor.execute("""
            SELECT username, email, active
            FROM Customers
            WHERE email = ? AND password = ?
        """, (email_login, password_login))

        result = cursor.fetchone()

        if result:
            username = result[0]
            active = result[2]

            return jsonify({
                "success": True,
                "message": "Logowanie poprawne",
                "username": username,
                "active": active
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Niepoprawny email lub hasło"
            }), 401

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:
        conn.close()

thread = threading.Thread(target=run_script, daemon=True)
thread.start()

@app.route("/get_usage")
def get_usage():
    return jsonify({
        "memory_total": data.memory_total,
        "memory_available": data.memory_available,
        "memory_usage": data.memory_usage,
        "cpu_usage": data.cpu_usage
    })

if __name__ == "__main__":
    app.run(debug=True) 