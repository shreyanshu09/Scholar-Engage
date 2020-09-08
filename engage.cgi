#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

my @params = param();

my $id = param('hobbies');chomp $id;
@hobbies = split(',',$id);
#$name = param('name');

$l = 1;
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
$flag=0;
print"<h3>Your Match List Is Here</h3><br>";
while($line=<IN>){
	$flag=0;
        chomp($line);
	@array = split(' ',$line);
#	print "@array";

	for($q=1;$q<4;$q+=1){
        for($w=10;$w<13;$w+=1){
		if($flag == 0){
                if(@hobbies[$q] eq @array[$w]){
			$flag = 1;
			if(!(@hobbies[0] eq @array[3])){
                        
			print "@array[3]<br>";
			}
                       else{
                        print "Sorry no other  match found";
                           }
		}
		}		
         }
	}

}
close OUT;


print<<EOP;
<a href=\"http://widit.knu.ac.kr/~joseph/unite/index.html"> <input type=\"button\" value=\"Chat with friends! using Unite!\" onClick=\"\login.html\"></a>
</div>
</body>
</html>
EOP

