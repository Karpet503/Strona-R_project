const button_reje = document.getElementsByClassName('login rejestracja');

// Funckja dodająca usera do tabeli Customer
function addCustomer() {
  // Inputy z formularza na stronie rejestracja.html
  const username = document.getElementById("username").value;
  const computer = document.getElementById("computer").value;
  const email = document.getElementById("email").value;
  const telefon_num = document.getElementById("telefon_num").value;

  // Sprawdzenie, czy wszystko jest uzupełnione
  if (!username || !computer || !email || !telefon_num ){
    alert("Wypełnij wszystkie pola");
    return;
  }

  // Utworzenie obiektu z wszystkimi danymi. Domyślnie konto aktywne
  const customerData = {
    username: username,
    computer: computer,
    email: email,
    telefon_num: telefon_num,
    last_log: Date.now,
    active: true
  };

  // Wysłanie requestu POST do serwera by dodal usera
  fetch('/addCustomer', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(customerData)
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert("Klient został dodany pomyślnie!");
      closeTab(); // Zamknięcie formsa po udanym dodaniu
    } else {
      alert("Wystąpił błąd podczas dodawania klienta.");
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert("Wystąpił błąd. Spróbuj ponownie.");
  });
}

// Po udanej rejestracji pokazujemy userowi komunikat i przenosimy do głównej
function closeTab() {
  alert("Rejestracja udana!");
  window.location.href = "body";
}

// Pobranie z bazy danych userów
function showUsers() {
  fetch('/SelectUsers')
    .then(response => response.json())
    .then(data => {
      let userslist = '';

      data.forEach(item => {
          userslist += `id: ${item.id}, username: ${item.username}, computer: ${item.computer}, email: ${item.email}, telefon_num: ${item.telefon_num}<br>`;
      });

      document.getElementById('showus').innerHTML = userslist;
    })
}