# Ask user for folder path
$path = Read-Host "Enter folder path to open"

# Validate path exists
if (!(Test-Path $path)) {
    Write-Host "Path does not exist!" -ForegroundColor Red
    exit
}

# Change directory
Set-Location $path

# Initialize conda

# Activate env
conda activate mscenv

# Launch Jupyter
jupyter notebook