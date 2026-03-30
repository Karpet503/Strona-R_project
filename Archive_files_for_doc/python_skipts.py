
'''

Pobranie z bazy danych userów
function showUsers() {
  fetch('/SelectUsers')
    .then(response => response.json())
    .then(data => {
      let userslist = '';

      data.forEach(item => {
          userslist += `id: ${item.id}, username: ${item.username}, email: ${item.email},<br>`;
      });

      document.getElementById('showus').innerHTML = userslist;
    })
} */ 

'''

'''

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

'''

# Poniżej ścieżki do folderów, każda wskazuje do czego ma się co odwoływać na http://adres:port:ścieżka.
#@app.route("/rejestracja.html")
#def index():
    #return render_template("rejestracja.html")