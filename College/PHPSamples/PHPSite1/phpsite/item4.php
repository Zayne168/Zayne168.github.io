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
    if (isset($_SESSION['shinguards']))
    $_SESSION['shinguards'] += $_POST['shinguards'];
    else
    $_SESSION['shinguards'] = $_POST['shinguards'];
}

?>
</head>
<body>
<?php require("library/header.php"); ?>

This is the soccer shinguards's page.<br>
In cart: <?php echoSession("shinguards") ?>

<form method='POST'>
<input type='number' name='shinguards' value='<?php echoPost("shinguards");?> '>
<input type='submit' name='choice' value='Buy'>
</form>

<?php readfile("library/footer.html"); ?>
</body>