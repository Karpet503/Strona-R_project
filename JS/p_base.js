// Funckja dodająca usera do tabeli Customer
function addCustomer() {
  // Inputy z formularza na stronie body (dawniej rejestracja)
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  //const computer = document.getElementById("computer").value;
  //const telefon_num = document.getElementById("telefon_num").value;

  // Sprawdzenie, czy wszystko jest uzupełnione
  if (!username || !email || !password){
    alert("Wypełnij wszystkie pola");
    return;
  }

  // Utworzenie obiektu z wszystkimi danymi. Domyślnie konto aktywne
  const customerData = {
    username: username,
    password: password,
    email: email,
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

function loginUser() {
  const email_login = document.getElementById("email_login").value;
  const password_login = document.getElementById("password_login").value;

  const loginData = {
    email_login: email_login,
    password_login: password_login
  };

  fetch('/Login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(loginData)
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert("Logowanie poprawne!");
      console.log("Zalogowany użytkownik:", data.username);
      const success = data.success;
      const message = data.message;
      const username = data.username;
      const active = data.active;

      document.getElementById("show_username").textContent = username;
      document.getElementById("show_message").textContent = message;
      document.getElementById("show_active").textContent = active;
      // np. przekierowanie
      window.location.href = "/body.html";
    } else {
      alert(data.message || "Niepoprawny email lub hasło.");
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert("Wystąpił błąd. Spróbuj ponownie.");
  });
}

function loadUsage() {
  fetch('/get_usage')
    .then(response => response.json())
    .then(data => {
      document.getElementById("mem_total").textContent = data.memory_total;
      document.getElementById("mem_available").textContent = data.memory_available;
      document.getElementById("mem_usage").textContent = data.memory_usage;
      document.getElementById("cpu_usage").textContent = data.cpu_usage;
    })
    .catch(error => {
      console.error("Błąd:", error);
    });
}

loadUsage();
setInterval(loadUsage, 5000);