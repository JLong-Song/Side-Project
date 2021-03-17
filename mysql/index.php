<?
    $conn = new mysqli('localhost', 'JustForUserLogIn', 'JustForUserLogIn', 'jlong');
    if(!$conn)die(mysqli_error());

    $result = $conn->query('SELECT * FROM users');
    $row = $result->fetch_row();
    print_r($row);
?>