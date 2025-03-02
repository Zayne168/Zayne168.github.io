

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>Updating</title>
</head>
<body class="w3-light-gray w3-center w3-monospace ">
    

<?php 
session_start();

echo "
    <form method='POST' action='updatefunc.php'>
        <label for='newname'>New Username: </label>
        <input name='newname'id='newname'required></input><br>
        <label for='newpass'>New Password: </label>
        <input name='newpass' id='newpass'required></input><br>
        <input name='id' type='hidden' id='id' value='".$_POST['id']."'></input>
        <input name='username' type='hidden' id='username' value='".$_POST['user']."'></input>
        <input type='submit' id='sub' value='submit'></input>
    </form>

";

$pdo=null;
?>
</body>
</html>