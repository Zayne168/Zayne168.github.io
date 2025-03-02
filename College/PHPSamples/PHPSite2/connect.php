<?php
function user_exist($username,$password){
    global $pdo;
    $sql="SELECT password FROM my_accounts WHERE username=?";
    $stmt=$pdo->prepare($sql);
    $stmt->execute([$username]);
    $info=$stmt->fetch();
    if($info){
        /*$hashPass=$info['password'];
        if(password_verify($password,$hashPass)){return true;}
        <else>return false;</else>*/
        return true;
    }else{ return false;}

}

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
    echo "<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>";
$stmt=$pdo->prepare($sql);

if ($stmt->execute()){
    //echo "table created successfully";//execute through if statement;
}else {
    echo "error in creating the table".$stmt->error;
}
$user_exist_bool=user_exist($username,$password);
if($username=="" ||$password==""){
    echo "<h1 class='w3-monospace w3-center'>Username and password must not be blank.</h1>";
    header('Refresh:3; url=index.php');

}else if($user_exist_bool){
    echo "<h1 class='w3-monospace w3-center'>User Already Exists Try Again!</h1>";
    header('Refresh:3; url=index.php');

}else{

   $sql="INSERT INTO my_accounts(username,password) VALUES (:username,:password)";
   $stmt=$pdo->prepare($sql);
   $hashPass=password_hash($password,PASSWORD_BCRYPT);
   $stmt->bindParam(":username",$username);
   $stmt->bindParam(":password",$hashPass);
   $stmt->execute();
   echo "<h1 class='w3-monospace w3-center'>Account Created! Automatically logging in and redirecting now.<h1>";
   session_start();
    $_SESSION["username"]=$username;
    $_SESSION["validLOG"]=true;
   $pdo=null;
   header('Refresh:2; url=home.php');
}
   $pdo=null;
}

?>