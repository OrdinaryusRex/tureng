function tureng {
    $param=$args[0]
    $param2=$args[1]
    $loc = Get-Location
    Set-Location C:\Users\EMINA\desktop\tureng
    .\env\Scripts\Activate.ps1
    if (!$param2) { $kelime=$param }
    if ($param2) { $kelime=$param + '%20' + $param2 }
    python .\tureng.py $kelime
    Set-Location $loc
    deactivate
}