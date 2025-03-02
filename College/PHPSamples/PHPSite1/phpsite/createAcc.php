<html>
<head>
<?php
require("library/phpfunctions.php");

function echoTable($conn)
{
    $sql = "SELECT * FROM users;";
    $result = $conn->query($sql);


    if ($result->num_rows > 0) 
    {
    echo "<table align='left'>";
    while($row = $result->fetch_assoc()){
        echo "<tr>";

        echo "<td>";
            echo $row["id"];
        echo "</td>";

        echo "<td>";
            echo $row["username"];
        echo "</td>";

        echo "<td>";
            echo $row["email"];
        echo "</td>";



    // edit button
        echo "\n<form method='POST' action='update.php'>";
        echo "<td>";
        echo "<input type='hidden' name='id' value='" . $row["id"] . "'>";
            echo "<input type='submit' name='choice' value='edit'>";
        echo "</td>";
        echo "</form>";

    // delete button
        echo "\n<form method='POST' action='delete.php'>";
        echo "<td>";
        echo "<input type='hidden' name='id' value='" . $row["id"] . "'>";
        echo "<input type='submit' name='choice' value='delete'>";
        echo "</td>";
        echo "</form>";

        echo "</tr>";
    }
    echo "</table>";
    } 
    
    else 
    {
    echo "No results";
    }

}


 
$conn = connectDB();
$message = '';

// process which submit button was presses

if (isset($_POST['choice']))
{
    $choice = getPost('choice');
    if ($choice == 'Create Account')
    {
    $password=$_POST['155password'];
    $confirm=$_POST['155confirm'];
    if (checkForUpper($password))
    {
    }
    else
    {
        echo "There is NO uppercase letter!";
    }
    if ($password == $confirm) 
    {

        $stmt = $conn->prepare("INSERT INTO users (username, email, encrypted_password, usergroup) 
                                                VALUES (?,?,?,?)");
        $stmt->bind_param("ssss", $username, $email, $encryptedpassword, $usergroup);

        $username = getPost('155username');
        $email = getPost('155email');
        $encryptedpassword = password_hash($password, PASSWORD_DEFAULT);
        $usergroup = getPost('usergroup');

        $stmt->execute();
        $message = 'Account Created';
	header("login.php");
    }
    else 
    {        
        $message = "Passwords don't match";
    }
    }
    
}

?>
</head>
<body>

<form method='POST'>
<table align='left'>
<tr>
<td>Username:</td>
<td><input type='text' name='155username' value='<?php echoPost("155username");?>'></td>
</tr>
<tr>
<td>Email:</td>
<td><input type='text' name='155email' value='<?php echoPost("155email");?>'></td>
</tr>

<tr>
<td>Password:</td>
<td><input type='password' name='155password' value='<?php echoPost("155password");?>'></td>
</tr>

<tr>
<td>Confirm Password:</td>
<td><input type='password' name='155confirm' value='<?php echoPost("155confirm");?>'></td>
</tr>

<tr>
<td>Usergroup</td>
<td><input type='text' name='usergroup' value='<?php echoPost("usergroup");?>'></td>
</tr>

<tr>
<td colspan='2'><?php echo $message;?></td>
</tr>

<tr>
<td colspan='2'>
<input type='submit' name='choice' value='Create Account'>
</form>
<form action="login.php">
<input type="submit" value="Log In Page"></input>
</td>
</table>
</form>

<?php echoTable($conn); ?>


</body>