#!/usr/bin/perl -w
use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);


$id = param("U_Name");chomp($id);
$pass = param("Password");chomp($pass);
$branch = param("Branch");chomp($branch);
$email = param("Email_Id");chomp($email);
$fname = param("First_Name");chomp($fname);
$lname = param("Last_Name");chomp($lname);
$bday = param("Birthday_day");chomp($bday);
$bmonth = param("Birthday_Month");chomp($bmonth);
$byear = param("Birthday_Year");chomp($byear);
$mobile = param("Mobile_Number");chomp($mobile);
$gender = param("Gender");chomp($gender);
$address = param("Address");chomp($address);
$city = param("City");chomp($city);
$pincode = param("Pin_Code");chomp($pincode);
$state = param("State");chomp($state);
$country = param("Country");chomp($country);
$hobbie1 = param("one");chomp($hobbie1);
$hobbie2 = param("two");chomp($hobbie2);
$hobbie3 = param("three");chomp($hobbie3);


$outf="abc.out"; 

print header();

print<<EOP;
<!DOCTYPE html>
<html>
<head>
    <title>Source Code</title>
<link href="https://fonts.googleapis.com/css?family=Ubuntu:300" rel="stylesheet">
</head>
<style type="text/css">
body{
	background:url(http://www.demo.amitjakhu.com/login-form/images/bg.png);
}    
#wrap {
    font-family:Ubuntu;
    margin: 70px auto;
    background-color:#f3f3f3;
	text-align:center;
width:30%;
-webkit-box-shadow: 10px 10px 10px rgba(0,0,0,0.4)
}
</style>
<body>
<div id="wrap">

EOP



if(!$id || !$pass || !$branch || !$email || !$fname || !$lname || !$bday || !$bmonth || !$byear || !$mobile || !$gender || !$address || !$city || !$pincode || !$state || !$country || !$hobbie1 || !$hobbie2 || !$hobbie3){
    print "<h3> Invalid Input</h3><br>You did not enter<br><br>";
    if(!$id){
        print "<p style=\"color:red;\">--User ID</p>";
    }      
    if(!$pass){
        print "<p style=\"color:red;\">--Password</p>";
    }   
    if(!$branch){
        print "<p style=\"color:red;\">--Branch</p>";
    }      
    if(!$email){
        print "<p style=\"color:red;\">--Email Address</p>";
    }  
     if(!$fname){
        print "<p style=\"color:red;\">--First Name</p>";
    }   
     if(!$lname){
        print "<p style=\"color:red;\">--Last Name</p>";
    }   
     if(!$bday){
        print "<p style=\"color:red;\">--Date of Birth</p>";
    }   
     if(!$bmonth){
        print "<p style=\"color:red;\">--Date of Birth</p>";
    }   
     if(!$byear){
        print "<p style=\"color:red;\">--Date of Birth</p>";
    }   
     if(!$mobile){
        print "<p style=\"color:red;\">--Mobile Number</p>";
    }   
     if(!$gender){
        print "<p style=\"color:red;\">--Gender</p>";
    }   
     if(!$address){
        print "<p style=\"color:red;\">--Address</p>";
    }    
    if(!$city){
        print "<p style=\"color:red;\">--City</p>";
    }  
    if(!$pincode){
        print "<p style=\"color:red;\">--Pincode</p>";
    }  
    if(!$state){
        print "<p style=\"color:red;\">--State</p>";
    }  
    if(!$country){
        print "<p style=\"color:red;\">--Country</p>";
    }  
    if(!$hobbie1){
        print "<p style=\"color:red;\">--Hobbies</p>";
    }  
    if(!$hobbie2){
        print "<p style=\"color:red;\">--Hobbies</p>";
    } 
    if(!$hobbie3){
        print "<p style=\"color:red;\">--Hobbies</p>";
    } 
    print "<br>please <a href=\"signup.html\">go back and try again</a>";
}
else
{
open(IN,"abc.out") || die "can't read file";
$flag=0;
while($line=<IN>){
        chomp($line);
        @array = split(' ',$line);
	
         if(@array[0] eq $id){
		$flag=1;
	}
}
close OUT;
     if($flag == 1){
           print "<p>Uid Already Taken</p>";
         print "<br>Go Back to<a href=\"signup.html\">SIGNUP_PAGE</a>";

       }
else {
	print "<p> Thanks for registering</p>";
         print "<br>Go Back to<a href=\"login.html\">LOGIN_PAGE</a>";
	open(OUT,">>$outf") || die "can't append to $outf";
        print OUT "\n$id $pass $email $fname $lname $bday $bmonth $byear $mobile $gender $hobbie1 $hobbie2 $hobbie3";
	close(OUT);
}
}
print<<EOP;
</div>
</body>
</html>

EOP



