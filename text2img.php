#!/usr/bin/php -f

<?php
// argv
parse_str(implode('&', array_slice($argv, 1)), $_GET);
//echo var_dump($_GET);

if ( !array_key_exists('text', $_GET) ) {
	echo "Please use with text=<text>\n Example ./text2img.php text='bob@mail.com'\n";
	exit(-1);
}

$text = $_GET['text'];
$filename = $text . ".png";

$im = imagecreate(300, 50);
$bg = imagecolorallocate($im, 0, 0, 0); // Black
// Add alpha
imagecolortransparent($im, $bg);
//$fg = imagecolorallocate($im, 255, 0, 0); // Red
$textcolor = imagecolorallocate($im, 45, 45, 45); // Grey

imagestring($im, 8, 8, 8, $text, $textcolor);
imagepng($im, $filename);

echo "Created $filename with $text";
?>


