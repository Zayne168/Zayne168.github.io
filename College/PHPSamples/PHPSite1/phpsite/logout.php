<!--  I honor Parkland's core values by affirming that I have 
followed all academic integrity guidelines for this work.
Zayne Bonner  
CSC 155 -->

<html>
<head>
<?php
require("library/phpfunctions.php"); 
session_start();
checklogin();
session_destroy();
header('Refresh:5; url=login.php');
?>

<style>
button{
background-color: #89CFF0;
  border: none;
  padding: 30px 60px;
  text-align: center;
  display: inline-block;
  font-size: 15px;
}
button:hover {
  border: 5px solid blue;
  padding: 25px 55px;
}

</style>
</head>
<body>
<?php require("library/header.php"); ?>
adios!
<?phpreadfile("library/footer.html"); ?>
</body>