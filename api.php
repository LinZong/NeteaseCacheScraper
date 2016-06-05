<!DOCTYPE html>
<html>
<head lang="zh">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<?php
$musicid = $_GET['id'];
$neteaseapi = "http://music.163.com/api/song/detail/?id=".$musicid."&ids=%5B".$musicid."%5D";
$rawjson = file_get_contents($neteaseapi);
$de_json = json_decode($rawjson,TRUE);
echo "歌名:".$de_json['songs']['0']['name']."<br>";
echo "歌手:".$de_json['songs']['0']['album']['artists']['0']['name']."<br>";
$rawdownload = $de_json['songs']['0']['mp3Url'];
$downloadProcesser = str_replace("http://m", "http://p", $rawdownload);
echo "下载地址(复制进下载工具下载):<a href='".$downloadProcesser."'>".$downloadProcesser."</a><br>你甚至可以试听一下<br>";

?>
<audio src="<?php echo $downloadProcesser?>" controls="controls"></audio>

</body>
</html>
