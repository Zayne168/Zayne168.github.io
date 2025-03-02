
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logout</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body class="w3-light-gray">
<?php
session_start();
echo "<h3 class='w3-monospace w3-center'>".$_SESSION["username"].", you are logging out. redirecting now...</h3>";

$_SESSION["validLOG"]=false;
$_SESSION=array();

session_destroy();
header('Refresh:3; url=index.php');

?>
</body>
</html>
