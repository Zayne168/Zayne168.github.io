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

if (!isset($_POST['choice']))// grab input from form to put in session -->
{}
else if ($_POST['choice'] == 'set')
{
	$_SESSION['theName'] = $_POST['theName'];
}
?>
</head>
<body>
<?php require("library/header.php"); ?>

Your Name: <?php echoSession("theName"); ?>

<form method='POST'>
<input type='text' name='theName' value='<?php echoPost("theName");?>'> <!-- form collecting name-->
<input type='submit' name='choice' value='set'>
</form>

<?php readfile("library/footer.html"); ?>
</body>