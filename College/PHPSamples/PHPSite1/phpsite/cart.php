<!--  I honor Parkland's core values by affirming that I have 
followed all academic integrity guidelines for this work.
Zayne Bonner  
CSC 155 -->

<html>
<head>
<?php
require("library/phpfunctions.php"); 
session_start();
checkcreds();
if (!isset($_POST['choice']))
{}
else if ($_POST['choice'] == 'Purchase')
{
    echo 'Thank you for your purchase!, please allow for 3-10 business years for processing.';
    $_SESSION['goal'] = 0;
    $_SESSION['soccer'] = 0;
    $_SESSION['cleats'] = 0;
    $_SESSION['shinguards'] = 0;
}
else if ($_POST['choice'] == 'Clear cart')
{
    $_SESSION['goal'] = 0;
    $_SESSION['soccer'] = 0;
    $_SESSION['cleats'] = 0;
    $_SESSION['shinguards'] = 0;
}
?>
</head>
<body>
<?php require("library/header.php"); ?>
Your cart:<br>
Soccer Goals: <?php echoSession("goal") ?> <br>
Soccer Balls: <?php echoSession("soccer") ?> <br>
Cleats: <?php echoSession("cleats") ?> <br>
Shinguards: <?php echoSession("shinguards") ?> <br>
<form method='POST'>
<input type='submit' name='choice' value='Purchase'>
<input type='submit' name='choice' value='Clear cart'>
</form>
<?php readfile("library/footer.html"); ?>
</body>