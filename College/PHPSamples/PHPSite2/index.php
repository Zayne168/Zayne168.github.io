<?php
//header('Refresh:3; url=createACC.php');
session_start();
$_SESSION["validLOG"]=false;
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body class="w3-bar w3-light-gray w3-monospace  w3-center">
    <h1>Log In</h1>
    <form  action="login.php" method="POST" >
        <label for="user">Input Username</label>
        <input type="text" id="user" name="username"></input>
        <br>
        <label for="pass">Input Password</label>
        <input type="password" id="pass" name="password"></input> 
    <hr>
       <input type="submit" value="Log In"></input>
       <input type="submit" formaction="connect.php" value="Create Account"></input> 
       
    </form>

</body>
</html>