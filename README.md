# License to Marry (LTM) Platform

Marriage preparation platform with React frontend and Flask REST API backend.

## 🚀 Quick Start

```bash
git clone git@github.com:QasimMuhammad/ltm.git
cd ltm
./setup.sh
```

**Run the app:**

**Terminal 1 (Backend):**
```bash
uv run run.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm install  # First time only
npm run dev
```

Open: `http://localhost:5173`

## 🪟 Windows Quick Start

Use PowerShell (run as Administrator when prompted):

```powershell
winget install --id Git.Git -e --source winget  # Install Git if you don't have it yet
```

```powershell
git clone git@github.com:QasimMuhammad/ltm.git
Set-Location ltm
.\setup.ps1
```

**Run the app:**

**Terminal 1 (Backend):**
```powershell
uv run run.py
```

**Terminal 2 (Frontend):**
```powershell
Set-Location frontend
npm install  # First time only
npm run dev
```

> `setup.ps1` installs Git, Python, Node.js, npm, and `uv` automatically with `winget`. If `winget` is missing, the script tells you how to install it first.

Open: `http://localhost:5173`

## 📦 Tech Stack

- **Frontend:** React 18 + Vite
- **Backend:** Flask + SQLAlchemy
- **Database:** SQLite

## 🔌 API

See [API.md](./API.md) for full API documentation.

**Quick reference:**
- `GET /api/questions?type=couple` - Get questions
- `POST /api/responses/couple` - Submit responses
- `GET /api/health` - Health check

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📝 License

MIT

## 💬 Support

Open an issue on GitHub