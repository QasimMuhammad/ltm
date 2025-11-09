$ErrorActionPreference = 'Stop'

Write-Host "🚀 Setting up LTM Platform..."

function Ensure-Winget {
    if (-not (Get-Command 'winget' -ErrorAction SilentlyContinue)) {
        throw "❌ winget is required. Install the Microsoft Store App Installer first: https://learn.microsoft.com/windows/package-manager/winget/#install-winget"
    }
}

function Ensure-Command {
    param (
        [string]$Command,
        [string]$WingetId,
        [string]$Description
    )

    if (Get-Command $Command -ErrorAction SilentlyContinue) {
        return
    }

    if ($WingetId) {
        Ensure-Winget

        Write-Host "⬇️  Installing $Description..."
        winget install --id $WingetId --exact --silent --accept-package-agreements --accept-source-agreements

        if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
            throw "❌ Failed to install $Description automatically. Install it manually and re-run the script."
        }
    } else {
        throw "❌ $Description is required. Install it manually and re-run the script."
    }
}

Ensure-Command -Command 'py' -WingetId 'Python.Python.3.11' -Description 'Python 3.11'
Ensure-Command -Command 'node' -WingetId '' -Description 'Node.js LTS (install manually from https://nodejs.org/en/download/prebuilt-installer if missing)'
Ensure-Command -Command 'npm' -WingetId '' -Description 'npm (bundled with Node.js)'

Write-Host "✅ Prerequisites check passed"

Write-Host "`n📦 Setting up backend..."

if (-not (Get-Command 'uv' -ErrorAction SilentlyContinue)) {
    Write-Host "⬇️  Installing uv with py -m pip..."
    py -m pip install --upgrade pip
    py -m pip install uv
}

if (-not (Get-Command 'uv' -ErrorAction SilentlyContinue)) {
    throw "❌ uv installation failed. Install manually with: py -m pip install uv"
}

uv sync

Write-Host "`n📦 Setting up frontend..."

Push-Location frontend
npm install
Pop-Location

Write-Host ""
Write-Host "✅ Setup complete!"
Write-Host ""
Write-Host "To start the application:"
Write-Host ""
Write-Host "Backend:"
Write-Host "  uv run run.py"
Write-Host ""
Write-Host "Frontend (in a new terminal):"
Write-Host "  Set-Location frontend"
Write-Host "  npm run dev"
Write-Host ""
Write-Host "Open http://localhost:5173 in your browser"

