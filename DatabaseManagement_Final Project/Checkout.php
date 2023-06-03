<?php
if(!empty($_POST)){
	
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "project";

	$conn = mysqli_connect($servername, $username, $password, $dbname);

	if(!$conn) {
		die("Connection failed: ".mysqli_connect_error());
	}
	else {
		 $sql = "INSERT INTO shipping (name, address, postalCode, city, country, email, phoneNumber) VALUES ('{$conn->real_escape_string($_POST['name'])}','{$conn->real_escape_string($_POST['address'])}','{$conn->real_escape_string($_POST['postal'])}','{$conn->real_escape_string($_POST['city'])}','{$conn->real_escape_string($_POST['country'])}','{$conn->real_escape_string($_POST['email'])}','{$conn->real_escape_string($_POST['phone'])}')";

		 $insert = $conn->query($sql);

		 if($insert == TRUE) {
		 	header("location: Reciept.php");
		 	exit();
		 }
		 else {
	 		die("Error: {$conn->errno} : {$conn->error}");
	 		exit();
	 	}
	}
}
?>