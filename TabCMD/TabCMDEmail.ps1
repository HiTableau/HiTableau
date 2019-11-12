$csvfile = import-csv -path "C:\Temp\regions.csv"

$Folder = "C:\temp\"
$server = "https://online.tableau.com/#/site/hosesadev694660"
$username = "jose.cervantes@usaa.com"
$password = "Tableau1309"
$tabcmd = "Tabcmd"
$URL = "/views/Regional/Obesity.pdf"


foreach ($line in $csvfile)
{
  $Region = $line.Regions
  $FileName = $Folder + $Region + ".pdf"
  $FullURL = $URL + "?:Refresh&Region="+ $Region
$Region
$FileName
$FullURL
  & $tabcmd get -s $server -u $username -p $password  $FullURL  -f $FileName
}
& $tabcmd logout

   $username = "tabvisualization@gmail.com"
   $password = "Tableau1309"
   $smtpServer = "smtp.gmail.com"
   $to_address =  ("jcervantesSA@gmail.com","lcorral9@gmail.com")
   $subject = "Tableau Report-" + $Region
   $port = 587

       $secpasswd = ConvertTo-SecureString $password -AsPlainText -Force
       $mycreds = New-Object System.Management.Automation.PSCredential ($username, $secpasswd)
      
 Send-MailMessage -From $username -To $to_address -SmtpServer $smtpServer -Subject $subject -Credential $mycreds -Port $port -UseSsl $true -attachment "C:\temp\West.pdf"
