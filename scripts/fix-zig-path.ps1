# Zig PATH fix for LLUX family
# Ajoute C:\DevTools\bin\zig au PATH utilisateur
$zigPath = "C:\DevTools\bin\zig"
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($currentPath -notlike "*$zigPath*") {
    [Environment]::SetEnvironmentVariable("Path", "$zigPath;$currentPath", "User")
    Write-Output "Zig PATH added: $zigPath"
} else {
    Write-Output "Zig PATH already present: $zigPath"
}
