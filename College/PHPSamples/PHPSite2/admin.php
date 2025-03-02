<?php
 session_start();
 if(!$_SESSION["validLOG"]){
 header("Location: index.php");
 }
function echoList()
{
    $dsn='mysql:host=localhost;dbname=project';
    $user="root";
    $pass="root";

try{
    $pdo= new PDO($dsn,$user,$pass);
}catch(PDOException $e){
    die("connection error".$e->getMessage());
}

$sql="CREATE TABLE IF NOT EXISTS my_accounts (
    id INT(7) NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    PRIMARY KEY(id)
)";

$stmt=$pdo->prepare($sql);

if ($stmt->execute()){
    //echo "table created successfully";//execute through if statement;
}else {
    echo "error in creating the table".$stmt->error;
}
    $sql = "SELECT * FROM my_accounts;";
    $pdo_statement = $pdo->query($sql);
    $results=$pdo_statement->fetchALL();
    echo "<div>";
        foreach($results as $result){
            
            echo    "Username: ".$result['username']."</br>";
            echo    "id: ".$result['id']."</br>";
            // update button
            echo "\n<form method='POST' action='admin/update.php'>";
            echo "<input type='hidden' name='id' value='" . $result['id'] . "'>";
            echo "<input type='hidden' name='user' value='" . $result['username'] . "'>";
            echo "<input type='submit'  value='update'>";
            echo "</form>";
            
            // delete button
            echo "\n<form method='POST' action='admin/delete.php'>";
            echo "<input type='hidden' name='id' value='" . $result['id'] . "'>";
            echo "<input type='hidden' name='user' value='" . $result['username'] . "'>";
            echo "<input type='submit'  value='delete'>";
            echo "</form>";            
            echo  "<br>";
            
        }
    echo "</div>";
            // add button
            echo"<div class='w3-bar'>";
            echo "\n<form method='POST' action='admin/create.php'>";
            echo "<input type='submit'   value='Add Account'>";
            echo "</form>";
            echo"</div>";


}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>Admin Page</title>
    <div class="w3-bar w3-blue-gray w3-card">
  <a href="home.php" class="w3-bar-item w3-button w3-mobile">Home</a>
  <a href="admin.php" class="w3-bar-item w3-button w3-mobile">Admin Page</a>
  <a href="logout.php" class="w3-bar-item w3-button w3-mobile w3-right">Logout</a>
</div>
</head>
<header>

</header>
<body class="w3-light-gray w3-center w3-monospace ">

    <?php 
    echoList();
    ?>
</body>
</html>