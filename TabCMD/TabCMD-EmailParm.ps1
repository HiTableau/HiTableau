$ReportName=$args[0]
$Region=$args[1]

$Folder = "C:\temp\"
$server = "https://online.tableau.com/#/site/hosesadev694660"
$username = "tabvisualization@gmail.com"
$password = "*********"
$tabcmd = "tabcmd.exe"
$URL = "/views/Regional/" + $ReportName + ".pdf"


  $FileName = $Folder + $Region + ".pdf"
  $FullURL = $URL + "?:Refresh&Region="+ $Region
  & $tabcmd get -s $server -u $username -p $password  $FullURL  -f $FileName

& $tabcmd logout

$images = @{ 
    image1 = $FileName 
}  
  
$body = @' 
<html>  
  <body>  
    <img src="cid:image1">
  </body>  
</html>  
'@  
  
$params = @{ 
    Attachments = $FileName
    Body = $body 
    BodyAsHtml = $true 
    Subject = 'Tableau Report-' + $Region
    From = 'tabvisualization@gmail.com' 
    To = ("tablvisualization@gmail.com")
    SmtpServer = 'smtp.gmail.com' 
    Port = 587 
    UseSsl = $true 
} 
 
       $username = 'tabvisualization@gmail.com'
       $password = "************"
       $secpasswd = ConvertTo-SecureString $password -AsPlainText -Force
       $mycreds = New-Object System.Management.Automation.PSCredential ($username, $secpasswd)

Send-MailMessage @params -Credential $mycreds 
