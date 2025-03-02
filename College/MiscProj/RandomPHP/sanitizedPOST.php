
 <?php
    // Turn on error reporting.
    error_reporting(E_ALL);
    ini_set('display_errors', '1');
    

    $year = date('Y');
    
?>

<!-- HTML rendered as is. Note the PHP drop-ins, i.e. PHP tags. -->
 <!DOCTYPE html>
 <html>
     <head>
         <title>p4-sanitizedPOST</title>
         <meta charset="utf-8">
         <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
     </head>

     <body class="w3-panel">
         <header class="w3-container w3-khaki"><h1>p4 - Sanitized POST</h1></header>
        
        <main class="w3-container">
            <!-- Abbreviation to Name form -->
            <form action="process.php" method="POST">

                <!-- Text box -->
                <p>
                    <label>Month</label>
                    <input class="w3-input w3-border w3-light-gray" type="text" name="month" placeholder="Enter current month">
                </p>

                <!-- Radio buttons -->
                <p>
                    <label>Marital status: </label>
                    <input class="w3-radio" type="radio" name='maritalStatus' value="married">
                    <label>Married</label>

                    <input class="w3-radio" type="radio" name='maritalStatus' value="single">
                    <label>Single</label>
                </p>
                
                <!-- Check boxes -->
                <p>
                    <label>Favorite music genre: </label>
                    <input class="w3-check" type="checkbox" name="favoriteMusicGenre[]" value="Pop">
                    <label>Pop</label>

                    <input class="w3-check" type="checkbox" name="favoriteMusicGenre[]" value="Reggae">
                    <label>Reggae</label>

                    <input class="w3-check" type="checkbox" name="favoriteMusicGenre[]" value="Rock">
                    <label>Rock</label>
                </p>
                <!-- Select element -->
                <p>
                    <label>State: </label>
                    <select class="w3-input" name="state">
                        <option selected disabled>Select state</option>
                        <option value="IL">Illinois</option>
                        <option value="MO">Missouri</option>
                        <option value="AZ">Arizona</option>
                        <option value="AR">Arkansas</option>
                        <option value="CA">California</option>
                    </select>
                </p>

                <button class="w3-button w3-green w3-block w3-round">Process Form</button>
            </form>

        </main>

         <footer class="w3-panel w3-center w3-text-gray w3-small">
             &copy; <?php echo $year; ?> Zayne Bonner
        </footer>
     </body>
 </html>