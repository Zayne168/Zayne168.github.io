<!--  I honor Parkland's core values by affirming that I have 
followed all academic integrity guidelines for this work.
Zayne Bonner  
CSC 155 -->

<html>
<head>
<?php

require('library/phpfunctions.php');
// local functions
$conn=connectDB();
session_start();
$message = '';
$sql = "SELECT * FROM users";
$result = $conn->query($sql);

?>
</head>
<body>
<?php require('library/header.php'); ?>
<h2><?php echo $message;?></h2>
<?php if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. "<br>";
	echo "username: " . $row["username"]. "<br>";
	echo "Encrypted Password: " . $row["encrypted_password"]. "<br>";
	echo "<hr>";
    }
} else {
    echo "0 results";
}?></body>
</html>