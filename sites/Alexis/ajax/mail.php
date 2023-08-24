<?php
	$message = '<html>
               <head>
                     <title>Call me back</title>
                 </head>
             <body>
                 <p><b>user:</b> '.$_POST['user'].'</p>
                 <p><b>subject:</b> '.$_POST['subject'].'</p>
                 <p><b>YourEmail:</b> '.$_POST['YourEmail'].'</p>
                 <p><b>ProjectBudget:</b> '.$_POST['ProjectBudget'].'</p>
                 <p><b>YourMessage:</b> '.$_POST['YourMessage'].'</p>
             </body>
         </html>';
	$email = "apocryph575@gmail.com";
	$subject = "=?utf-8?B?".base64_encode("Client from KAWIK")."?=";
	$headers = "From: $email\r\nReply-to: $email\r\nContent-type:text/html; charset=utf-8\r\n";

  	$success = mail($email, $subject, $message, $headers);
  	echo $success;

?>;