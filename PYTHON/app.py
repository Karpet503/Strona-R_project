import os
import sqlite3
from flask import Flask, render_template, request, jsonify, send_from_directory

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATABASE = os.path.join(BASE_DIR, "app_data.db")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
JS_DIR = os.path.join(BASE_DIR, "JS")
CSS_DIR = os.path.join(BASE_DIR, "CSS")

app = Flask(__name__, template_folder=TEMPLATE_DIR)


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return render_template("rejestracja.html")


@app.route("/body")
def body():
    return render_template("body.html")


@app.route("/addCustomer", methods=["POST"])
def add_customer():
    data = request.get_json()

    username = data.get("username")
    computer = data.get("computer")
    email = data.get("email")
    telefon_num = data.get("telefon_num")

    if not username or not computer or not email or not telefon_num:
        return jsonify({
            "success": False,
            "message": "Missing required fields."
        }), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Customers (username, computer, email, telefon_num, active)
            VALUES (?, ?, ?, ?, ?)
        """, (username, computer, email, telefon_num, True))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Customer added successfully."
        })

    except sqlite3.IntegrityError:
        return jsonify({
            "success": False,
            "message": "Username already exists."
        }), 400

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@app.route("/JS/<path:filename>")
def serve_js(filename):
    return send_from_directory(JS_DIR, filename)


@app.route("/CSS/<path:filename>")
def serve_css(filename):
    return send_from_directory(CSS_DIR, filename)


if __name__ == "__main__":
    app.run(debug=True)