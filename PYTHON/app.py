import os
import sqlite3
from flask import Flask, render_template, request, jsonify, send_from_directory
#zabezpieczenie hasła biblioteka
#from werkzeug.security import generate_password_hash, check_password_hash
# Skróty pod ścieżki, BASE_DIR - z automaty podnosi o poziom foldery, by łatwiej się wpisywało ścieżki reszty folderów.
#BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#ścieżka do folderu  
DATABASE = os.path.join(BASE_DIR, "../app_data.db")
#ścieżka do folderu template
TEMPLATE_DIR = os.path.join(BASE_DIR, "../templates")
#ścieżka do folderu JS
JS_DIR = os.path.join(BASE_DIR, "../JS")
#ścieżka do folderu CSS
CSS_DIR = os.path.join(BASE_DIR, "../CSS")
#ścieżka do folderu IMAGES
IMG_DIR = os.path.join(BASE_DIR, "../IMAGES")

app = Flask(__name__, template_folder=TEMPLATE_DIR)



def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Poniżej ścieżki do folderów, każda wskazuje do czego ma się co odwoływać na http://adres:port:ścieżka.
#@app.route("/rejestracja.html")
#def index():
    #return render_template("rejestracja.html")


@app.route("/body.html")
def body():
    return render_template("body.html")


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

# Nasłuch na komende "/SelectUSers" z metodą POST. Jak wygryje to wybiera podstawowe dane z tabeli CUSTOMERS.
""" @app.route("/SelectUsers", methods=["GET"])
def SelectUsers():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, computer, email, telefon_num FROM Customers")
    items = cursor.fetchall()

    items_list = [{'id': item['id'], 'username': item['username'], 'computer': item['computer'], 'email': item['email'], 'telefon_num': item['telefon_num']} for item in items]

    conn.close()

    return jsonify(items_list)
"""
if __name__ == "__main__":
    app.run(debug=True) 