<?php
if(!empty($_POST)){
	
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "project";

	//create connection
	$conn = mysqli_connect($servername, $username, $password, $dbname);
	//check connection
	if (!$conn) {
		die("Connection failed: ".mysqli_connect_error());
	}

	if(isset($_POST['username'])){
		$username = $_POST['username'];
		$password = $_POST['password'];

		$sql = "SELECT * FROM credentials WHERE username='".$username."' AND password='".$password."' LIMIT 1";
		$res = mysqli_query($conn,$sql);

		if(mysqli_num_rows($res)==1) {
			echo "<h3>Welcome to Online Outlet! </h3> <br>";
			if (mysqli_num_rows($res) > 0) {
				while ($row = mysqli_fetch_assoc($res)) {
					echo "ID: ".$row['ID']."<br> Name: ".$row['firstname']." ".$row['lastname']."<br>Username: ".$row['username']."<br>Email: ".$row['email']."<br>";
				}
			}
			exit();
		}
		else {
			echo "<h3>Invalid login information. Please try again.</h3><br><a href='Login.php'>Log In</a><br><a href='SignUp.php'>Sign Up</a>";
			exit();
		}
	}
}
?>