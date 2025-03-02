<html>
<head>
<?php
require("library/phpfunctions.php");



//session_start();
//checkcredentials();   // bounce if not logged in  
$conn = connectDB();

// process which submit button was presses

if (isset($_POST['choice']))
{
    $choice = getPost('choice');
    if ($choice == 'delete')
    {
    $row = getRow($conn, $_POST['id']);   // id came from table.php
    }
    else if ($choice == 'Cancel')
    {
    header("Location: createAcc.php");
    }
    else if ($choice == 'Delete Record')
    {
    $stmt = $conn->prepare("DELETE FROM users WHERE id=?");
    $stmt->bind_param("s", $id);

    // set parameters and execute
    $id = getPost('id');

    $stmt->execute();
    header("Location: createAcc.php");
    }

}
?>
</head>
<body>

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
<input type='submit' name='choice' value='Delete Record'>
<input type='submit' name='choice' value='Cancel'>
</td>
</table>
</form>


</body>