<html>
  <head>
  <?php 
function echoPost($name){
 if (isset($_POST[$name]))
  echo htmlspecialchars($_POST[$name]);
}


function echoSession($name) {
    if (isset($_SESSION[$name]))
    echo htmlspecialchars($_SESSION[$name]);
}

function connectDB(){
    $user = "zbonner1";  
    $conn = mysqli_connect("localhost",$user,$user,$user);
// Check connection
    if (mysqli_connect_errno()) 
    {
	echo "<b>Failed to connect to MySQL: " . mysqli_connect_error() . "</b>";
	// go to an error page
    }

    return $conn;
}

function getPost($name) {
    if (isset($_POST[$name])){
	return htmlspecialchars($_POST[$name]);}
    return '';
}

function getRow($conn, $id){
    $sql = "SELECT * FROM users WHERE id=?";
    $stmt = $conn->prepare($sql); 
    $stmt->bind_param("s", $id);
    $stmt->execute();
    
    $result = $stmt->get_result();

    if ($result->num_rows  == 1) 
    {
    return $result->fetch_assoc();
    }
    else
    {
    echo 'Data not found';
    return "";
    }
}
function getUserRow($conn, $user){
    $sql = "SELECT * FROM users WHERE username=?"; 
    $stmt = $conn->prepare($sql); 
    $stmt->bind_param("s", $user);
    $stmt->execute();
    
    $result = $stmt->get_result(); 

    if ($result->num_rows  == 1) 
    {
	return $result->fetch_assoc();
    }
    else
    {
	echo 'Login Failed';
	return "";
    }
}

function checkLogin($conn, $user, $pass){
    $row = getUserRow($conn, $user);
    if ($row=="failed") return false;
    if (password_verify($pass, $row['encrypted_password']))
    {
	return true;
    }
    return false;
}

function checkcreds(){
	if ( !isset( $_SESSION['username'] ) )
	{
		header("Location: loginpage.php");
	}
}

function checkForUpper($string){
    for ($i=0; $i<strlen($string); $i++)   
    {
    if (ctype_upper($string[$i]))  
    {
        return true;
    }
    }
    return false;
}


?>

  </head>
</html>
<!--  I honor Parkland's core values by affirming that I have 
followed all academic integrity guidelines for this work.
Your name 
Your section -->