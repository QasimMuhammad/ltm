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