<?php
$servername = "100.113.36.12:3307";
$username = "project";
$password = "paw0rd123";
$dbname = "BazaTestowa";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>