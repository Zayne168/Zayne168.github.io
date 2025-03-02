<html>
<head>
<?php
require("library/phpfunctions.php");
session_start();
checkcreds();

 

if (!isset($_POST['choice']))
{}
else if ($_POST['choice'] == 'Buy')
{
    if (isset($_SESSION['cleats']))
    $_SESSION['cleats'] += $_POST['cleats'];
    else
    $_SESSION['cleats'] = $_POST['cleats'];
}

?>
</head>
<body>
<?php require("library/header.php"); ?>

This is the soccer cleats/boots's page.<br>
In cart: <?php echoSession("cleats") ?>

<form method='POST'>
<input type='number' name='cleats' value='<?php echoPost("cleats");?> '>
<input type='submit' name='choice' value='Buy'>
</form>

<?php readfile("library/footer.html"); ?>
</body>