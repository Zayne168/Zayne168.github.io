
<?php
session_start();
    if($_POST['username']==$_SESSION['username']){
        $_SESSION['username']=$_POST['newname'];
    }
    
    $dsn='mysql:host=localhost;dbname=project';
    $user="root";
    $pass="root";

try{
    $pdo= new PDO($dsn,$user,$pass);
}catch(PDOException $e){
    die("connection error".$e->getMessage());
}

    $hashPass=password_hash($_POST['newpass'],PASSWORD_BCRYPT);
    $username=$_POST['newname'];
    $sql="UPDATE my_accounts SET username='".$username."',password='".$hashPass."'
            WHERE id=".$_POST['id'].";";
    echo $sql;
    $stmt=$pdo->prepare($sql);
    $stmt->execute();
    $pdo=null;
    header("Location:../admin.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>Updating</title>
</head>
<body class="w3-light-gray w3-center w3-monospace ">
    


</body>
</html>