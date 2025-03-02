<?php
 session_start();
if(!$_SESSION["validLOG"]){
header("Location: index.php");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

    <title>Home</title>
    
</head>
<body class="w3-light-gray">
<div class="w3-bar w3-blue-gray w3-monospace w3-card">
  <a href="#home" class="w3-bar-item w3-button w3-mobile">Home</a>
  <a href="#survey" class="w3-bar-item w3-button w3-mobile">Survey</a>
  <a href="#abtme" class="w3-bar-item w3-button w3-mobile">About Me</a>
  <a href="admin.php" class="w3-bar-item w3-button w3-mobile">Admin Page</a>
  <a href="logout.php" class="w3-bar-item w3-button w3-mobile w3-right">Logout</a>
</div>
<div class="w3-monospace w3-center">
<h2 id="home">Welcome <?php echo $_SESSION["username"];?>!</h2>
<p>Welcome to my website! 
    <br>This site is to be used as a project for CS234-002. 
    <br>For any questions feel free to contact me at zbonner@siue.edu</p>
    <hr>
    <br>
</div>
<div class="w3-monospace w3-center w3-border w3-blue-gray">
    <h2 id="survey">Survey</h2>
    <form method="POST">
        <label for="q1">What is something I could improve on this site? </label><br>
        <input class="w3-light-gray" name="q1" id="q1"></input><br>
        <label for="q2">Why are you visiting this site? </label><br>
        <input class="w3-light-gray" name="q2" id="q2"></input><br>
        <label for="q3">How was your day?</label><br>
        <input class="w3-light-gray" name="q3" id="q3"></input><br>
        <label for="q4">What is a book you would recommend I read? </label><br>
        <input class="w3-light-gray" name="q4" id="q4"></input><br>
    <br>
        <input class="w3-light-gray" type="submit" value ="Submit">
    </form>
</div>
<div class="w3-monospace w3-center">
<h2 id="abtme" >About me</h2>
<p class="w3-container">
    Hello! I am Zayne. I am a Computer Science major at Southern Illinois University. I have varying experience in computer science. In high school I took two courses in computer science. One was based around website development using CSS and HTML. It involved very basic code and was a general introduction to website development. I also took a computer operations course which taught me about computer hardware, how it works with software, and also how to code in Python. My Senior year of Unity High School I took dual-credit courses at Parkland College. I took a course in HTML and CSS, a course in Python, a course in Java, and a course identical to this one, which taught me PHP, SQL, and how to use them alongside python. You can find my other work here:
</p>
    <ul class="w3-container w3-ul w3-card" >
        <li><a href="//zayne168.github.io">HTML</a></li>
        <li><a href="//csit.parkland.edu/~zbonner1/final">PHP and SQL</a></li>
    </ul>
<p class="w3-container">
    I also really enjoy reading, here is a table of my favorite books:
</p>
    <?php 
    
    $dsn='mysql:host=localhost;dbname=project';
    $user="root";
    $pass="root";
    
    try{
        $pdo= new PDO($dsn,$user,$pass);
    }catch(PDOException $e){
        die("connection error".$e->getMessage());
    }
    $sql="SELECT books.book_name, authors.auth_name FROM books JOIN authors ON books.auth_id = authors.auth_id;";
    $stmt= $pdo->query($sql);
    $results=$stmt->fetchALL();
    echo "<table class='w3-table w3-hoverable w3-centered w3-bordered'>
        <th class='w3-center'>Author</th><th class='w3-center'>Title</th>";
    foreach($results as $result){
        echo"
        <tr>
        <td class='w3-center'>".$result['auth_name']."</td>
        <td class='w3-center'>".$result['book_name']."</td>
        </tr>
        ";
    }
    echo"</table>";
    ?>

</div>
</body>
</html>