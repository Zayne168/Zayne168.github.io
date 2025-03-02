<?php 
function checkContent($username,$password){
    global $pdo;
    $sql="SELECT password FROM my_accounts WHERE username=?";
    $stmt=$pdo->prepare($sql);
    $stmt->execute([$username]);
    $info=$stmt->fetch();
    if($info){
        $hashPass=$info['password'];
        if(password_verify($password,$hashPass)){return true;}
        else {return false;}
    }else {return false;}

}
echo "<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>";
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        $username=$_POST["username"];
        $password=$_POST["password"];
    
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

$account=checkContent($username,$password);
if($account){
echo "<h1 class='w3-monospace w3-center'>Logging in...<h1>";
session_start();
$_SESSION["username"]=$username;
$_SESSION["validLOG"]=true;
$pdo=null;
header('Refresh:2; url=home.php');
}
else{
echo "<h1 class='w3-monospace w3-center'>Invalid username or password. redirecting...<h1>";
$pdo=null;
header('Refresh:2; url=index.php');
}


   //$pdo=null;
}
//header("Location:home.php");
?>