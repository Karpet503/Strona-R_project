// Funkcja, która wykonuje zapytanie AJAX co 10 sekund
function getActiveUsers() {
    $.ajax({
        url: 'active_users.json',  // Lokalny plik JSON, który zawiera dane użytkowników
        method: 'GET',
        success: function(data) {
            // Aktualizujemy listę użytkowników na stronie
            var usersList = $('#users-list');
            usersList.empty();  // Czyścimy poprzednią listę
            data.forEach(function(user) {
                usersList.append('<li>' + user + '</li>');  // Dodajemy nowych użytkowników
            });
        }
    });
}

// Wykonujemy zapytanie co 10 sekund
setInterval(getActiveUsers, 10000);  // 10000 ms = 10 sekund

// Naładowanie danych po pierwszym załadowaniu strony
$(document).ready(function() {
    getActiveUsers();
});