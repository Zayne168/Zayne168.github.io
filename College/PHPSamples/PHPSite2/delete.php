
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>deleting</title>
</head>
<body class="w3-light-gray w3-center w3-monospace ">
    

<?php 
    session_start();
    $dsn='mysql:host=localhost;dbname=project';
    $user="root";
    $pass="root";

try{
    $pdo= new PDO($dsn,$user,$pass);
}catch(PDOException $e){
    die("connection error".$e->getMessage());
}

$sql="DELETE FROM my_accounts WHERE id=".$_POST["id"].";";
$stmt=$pdo->prepare($sql);
$stmt->execute();

if($_POST["user"]==$_SESSION["username"]){
    echo "You have deleted your current account, you are being logged out now. Goodbye.";
    header('Refresh:2; url=../logout.php');
}else{
echo    "Account successfully deleted. Redirecting...";
header('Refresh:2; url=../admin.php');
}
$pdo=null;
?>
</body>
</html>