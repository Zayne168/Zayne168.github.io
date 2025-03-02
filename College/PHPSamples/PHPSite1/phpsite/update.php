<html>
<head>
<?php
// load the libraries
require("library/phpfunctions.php");



 
$conn = connectDB();

if (isset($_POST['choice']))
{
    $choice = getPost('choice');
    if ($choice == 'edit')
    {
    $row = getRow($conn, $_POST['id']);   // id came from table.php
    }
    else if ($choice == 'Cancel')
    {
    header("Location: createAcc.php");
    }
    else if ($choice == 'Save and Update')
    {
    $stmt = $conn->prepare("UPDATE users SET username=?, email=? WHERE id=?");
    $stmt->bind_param("sss", $username, $email, $id);

    // set parameters and execute
    $username = getPost('155username');
    $email = getPost('155email');
    $id = getPost('id');

    echo "UPDATE users SET username=$username, email=$email WHERE id=$id";

    $stmt->execute();
    header("Location: createAcc.php");
    }

}
?>
</head>
<body>
Update here

<form method='POST'>
<table >
<tr>
<td>ID:</td>
<td><?php echoPost("id");?>
<input type='hidden' name='id' value='<?php echo $row['id'];?>'></td>
</tr><tr>
<td>Username:</td>
<td><input type='text' name='155username' value='<?php echo $row['username'];?>'></td>
</tr><tr>
<td>Email:</td>
<td><input type='text' name='155email' value='<?php echo $row['email'];?>'></td>
</tr><tr>
<td colspan='2'>
<input type='submit' name='choice' value='Save and Update'>
<input type='submit' name='choice' value='Cancel'>
</td>

</table>
</form>
</body>