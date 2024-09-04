
<style>
    body{
        background-color: #212121;
    }
</style>
<font color='#ffffff'>
<?php
$jok = file_get_contents('http://Api.codebazan.ir/jok/');
$bio = file_get_contents('http://Api.codebazan.ir/bio/');
$zekr = file_get_contents('http://Api.codebazan.ir/zekr/');
$dans = file_get_contents('http://Api.codebazan.ir/danestani/');
$hadis = file_get_contents('http://Api.codebazan.ir/hadis/');
$dialog = file_get_contents('http://Api.codebazan.ir/dialog/');
$array = "{
    'jok':'$jok',
    'bio':'$bio',
    'zekr':'$zekr',
    'danestani':'$dans',
    'hadis':'$hadis',
    'dialog':'$dialog'
}";
echo $array;
?>
</font>