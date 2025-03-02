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
    if (isset($_SESSION['soccer']))
    $_SESSION['soccer'] += $_POST['soccer'];
    else
    $_SESSION['soccer'] = $_POST['soccer'];
}

?>
</head>
<body>
<?php require("library/header.php"); ?>

This is the soccer ball's page.<br>
In cart: <?php echoSession("soccer") ?>

<form method='POST'>
<input type='number' name='soccer' value='<?php echoPost("soccer");?> '>
<input type='submit' name='choice' value='Buy'>
</form>

<?php readfile("library/footer.html"); ?>
</body>