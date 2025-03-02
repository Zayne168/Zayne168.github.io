<?php
    $month=$_POST['month'];
    $maritalS=$_POST['maritalStatus'];
    $favMusic=$_POST['favoriteMusicGenre'];
    $state=$_POST['state'];
    function getValue($key){
            if(isset($key)){
                $key=htmlspecialchars($key);
                $key=trim($key);
                return $key;
            }else{
                return "";
            
            }
    }
?>
 <!DOCTYPE html>
 <html>
    <?php 
    
    $month=getValue($month);
    echo "<p>Month: ";
    if($month=="")
        $month="Not provided";
    echo $month;
    echo "</p>";

    $maritalS=getValue($maritalS);
    echo "<p>Marital status: ";
    if($maritalS=="")
        $maritalS="Not provided";
    echo $maritalS;
    echo "</p>";

    echo "<p>Favorite music genre: <ul>";
        foreach($favMusic as $count)
            echo "<li>$count</li>";
    echo "</ul>";
        
    $state=getValue($state);
        echo "<p>State: ";
            if($state=="")
                $state="Not provided";
            echo $state;
            echo "</p>";
    ?>
 </html>