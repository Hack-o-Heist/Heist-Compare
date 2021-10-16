<?php
$name = $_POST['name'];
$visitor_email = $_POST['email'];
$message = $_POST['message'];

$email_from = 'hackoheist2021@gmail.com';
$email_subject="Hack-o-Heist Heist Compare";
$email_body="User Name: $name.\n",
  "User Message: $message.\n";
  $to="hackoheist2021@gmail.com";
  $headers="From: $email_form \r\n";
  $headers="Reply-To: $visitor_email \c\n";
  mail($to,$email_subject,$email_body,$headers);
  header("Location: contact.html");
  ?>