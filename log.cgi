#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$id = param("username");chomp($id);
$pass = param("password");chomp($pass);
$l = 0;
print header();
$len = length $id;
$lenpass = length $pass;
$lenline = length $line;

$users=0;
$i=0;
$str="uid,uid2,uid3";


print<<EOP;
<html class="gr__widit_knu_ac_kr"><head>
    <title>Source Code</title>
<link href="https://fonts.googleapis.com/css?family=Ubuntu:300" rel="stylesheet">
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
input{
	margin:5%;
	padding: 11px 25px;
	margin-right:10px;	
	font-family: 'Ubuntu', serif;
	font-weight: 300;
	font-size: 18px;
	color: #fff;
	text-shadow: 0px 1px 0 rgba(0,0,0,0.25);
	
	background: #56c2e1;
	border: 1px solid #46b3d3;
	border-radius: 5px;
	cursor: pointer;
	
	box-shadow: inset 0 0 2px rgba(256,256,256,0.75);
	-moz-box-shadow: inset 0 0 2px rgba(256,256,256,0.75);
	-webkit-box-shadow: inset 0 0 2px rgba(256,256,256,0.75);
}
input:hover{
	background: #3f9db8;
	border: 1px solid rgba(256,256,256,0.75);
	
	box-shadow: inset 0 1px 3px rgba(0,0,0,0.5);
	-moz-box-shadow: inset 0 1px 3px rgba(0,0,0,0.5);
	-webkit-box-shadow: inset 0 1px 3px rgba(0,0,0,0.5);
}
</style>
<body>
<div id="wrap">
EOP

open(IN,"abc.out") || die "can't read file";
while($line=<IN>){
        chomp($line);
        my @array = split(' ',$line);
          if(@array[0] eq $id){
                if(@array[1] eq $pass){
			
                        print "<h3>Login Confirmation</h3><br>";
                        print "your id is <font color=red>$id </font><br>";
                        print "your email is<font color=red> @array[2]</font><br>";
                        print "your First Name is <font color=red>@array[3]</font><br>";
                        print "your Last Name is <font color=red>@array[4]</font><br>";
                        print "your Date Of Birth is <font color=red>@array[5]&nbsp;@array[6]&nbsp;@array[7]</font><br>";
                        print "your Mobile Number is <font color=red>@array[8]</font><br>";
                        print "your Gender is <font color=red>@array[9]</font><br>";
                        print "your Hobbies are <font color=red>@array[10]&nbsp;@array[11]&nbsp;@array[12]</font><br>";
                        print "<form action=\"engage.cgi\" method=\"POST\">";
			print " <input type=\"hidden\" value=\"@array[3],@array[10],@array[11],@array[12]\" name=\"hobbies\">";
                        print "<a href=\"login.html\"> <input type=\"button\" value=\"Back to Login\" onClick=\"\login.html\"></a>";
                        print "<input type=\"Submit\" style=\"background-color:#DB4437\" value=\"ENGAGE\"/>";
			print "</form>";
                        last;
                }else{
                        print "Wrong password";
                        last;
               }
        
     }
}
close(IN);

print<<EOP;
</div>
</body>
</html>
EOP
