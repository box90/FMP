
$players = import-csv -Delimiter ";" ".\CSVDB Magician.csv" # | ConvertTo-Json | Add-Content -Path "FMPDB.json" 

foreach ($item in $players){    # change properties to an integer

    [int32]$item.ID = $item.ID
    [int32]$item.OVA = $item.OVA
    [int32]$item.POT = $item.POT
    [int32]$item.Height = $item.Height
    [int32]$item.Weight = $item.Weight
}

$players | ConvertTo-Json | Add-Content -Path "FMPDB.json" -Force