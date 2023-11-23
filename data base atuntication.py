CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
<?php
host = "localhost";
user = "your_username";
password = "your_password";
database = "agriculture_db";

conn = new mysqli(host, user, password, database);

if (conn->connect_error) {
    die("Connection failed: " . conn->connect_error);
}
?>
<?php
session_start();
include("config.php");

function isLoggedIn()
{
    return isset($_SESSION['user_id']);
}

function login(username, password)
{
    global conn;

    hashed_password = sha1(password); // Use a more secure hashing algorithm in a production environment.

    query = "SELECT * FROM users WHERE username='$username' AND password='$hashed_password'";
    result = conn->query(query);

    if (result->num_rows > 0) {
        user = result->fetch_assoc();
        _SESSION['user_id'] = user['id'];
        return true;
    } else {
        return false;
    }
}

function logout()
{
    session_unset();
    session_destroy();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <form id="loginForm" action="login.php" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <button type="submit">Login</button>
        </form>
    </div>
    <script src="scripts.js"></script>
</body>
</html>
body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    text-align: center;
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 5px;
}

button {
    margin-top: 10px;
}
document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Perform client-side validation if needed

    // Send data to the server for authentication
    fetch('login.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = 'dashboard.php';
        } else {
            alert('Login failed. Please check your username and password.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
< ?php
include("auth.php");

if (!isLoggedIn()) {
header("Location: index.html");
exit();
}
? >

< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Dashboard < / title >
< link
rel = "stylesheet"
href = "styles.css" >
< / head >
< body >
< div


class ="container" >

< h2 > Welcome
to
the
Dashboard < / h2 >
< p > < a
href = "logout.php" > Logout < / a > < / p >
< / div >
< / body >
< / html >
<?php
include("auth.php");
logout();
header("Location: index.html");
exit();
?>
