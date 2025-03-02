<?php
//header('Refresh:3; url=createACC.php');
session_start();

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<div class="w3-bar w3-blue-gray w3-card">
  <a href="../home.php" class="w3-bar-item w3-button w3-mobile">Home</a>
  <a href="../admin.php" class="w3-bar-item w3-button w3-mobile">Admin Page</a>
  <a href="../logout.php" class="w3-bar-item w3-button w3-mobile w3-right">Logout</a>
</div>
<body class="w3-bar w3-light-gray w3-monospace  w3-center">
    <h1>Create Account</h1>
    <form  action="adduser.php" method="POST" >
        <label for="user">Input Username</label>
        <input type="text" id="user" name="username"></input>
        <br>
        <label for="pass">Input Password</label>
        <input type="text" id="pass" name="password"></input> 
    <hr>
       <input type="submit" value="Create Account"></input>
       
    </form>

</body>
</html>