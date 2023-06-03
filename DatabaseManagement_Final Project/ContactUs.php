<?php
	 if(!empty($_POST)) {

	 	//create database connection
	 	$servername = "localhost";
	 	$username = "root";
	 	$password = "";
	 	$dbname = "project";

	 	$conn = mysqli_connect($servername, $username, $password, $dbname);

        if(!$conn) {
            die("Connection failed: ".mysqli_connect_error());
        }

       
        mysqli_query($conn, "INSERT INTO contact_us (firstname, lastname,email, message) VALUES ('" . $firstname. "', '" . $lastname. "','" . $email. "','" . $message. "')");
        $insert_id = mysqli_insert_id($conn);
        if(!empty($insert_id)) {
        $message = "Your message has been sent successfully!";

?>

