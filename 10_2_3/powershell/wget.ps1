type wget.ps1
$storageDir = $pwd 
$webclient = New-Object System.Net.WebClient 
$url = "http://10.11.0.51/test.txt" 
$file = "new_file.txt" 
$webclient.DownloadFile($url,$file) 

