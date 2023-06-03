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

		 //depostiing the credentials into the databse
	 	$sql = "INSERT INTO credentials (firstname, lastname, username, password, email) VALUES ('{$conn->real_escape_string($_POST['firstname'])}', '{$conn->real_escape_string($_POST['lastname'])}','{$conn->real_escape_string($_POST['username'])}','{$conn->real_escape_string($_POST['password'])}','{$conn->real_escape_string($_POST['email'])}')";

	 	$insert = $conn->query($sql);

	 	//insertion query successful or not
	 	if($insert == TRUE) {
	 		echo"<h3>Success! You are now registered! </h3> <br> <a href = 'Login.html'> Log In </a>";
	 		exit();
	 	}
	 	else {
	 		die("Error: {$conn->errno} : {$conn->error}");
	 		exit();
	 	}
	 }
?>