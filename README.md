# License to Marry (LTM) Platform

A full-stack marriage preparation platform combining **React + Vite** frontend with **Flask REST API** backend.

## 🏗️ Architecture

```
Frontend (React)  ←──────→  Backend (Flask)  ←──────→  Database
Port: 5173          REST API   Port: 5000         SQLAlchemy ORM
```

## 🚀 Quick Start

### Prerequisites
- **Node.js** 18+ and npm
- **Python** 3.8+
- uv (Python package manager) - Install from https://github.com/astral-sh/uv

### Setup (5 minutes)

**Option 1: Automated Setup**
```bash
git clone git@github.com:QasimMuhammad/ltm.git
cd ltm
./setup.sh
```

**Option 2: Manual Setup**

1. **Clone the repository**
   ```bash
   git clone git@github.com:QasimMuhammad/ltm.git
   cd ltm
   ```

2. **Backend Setup**
   ```bash
   # Install Python dependencies using uv
   uv sync
   
   # Or if you prefer pip:
   pip install flask flask-cors sqlalchemy python-dotenv
   
   # Start Flask server
   python run.py
   ```
   
   Backend runs on: `http://localhost:5000`

3. **Frontend Setup** (in a new terminal)
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   
   Frontend runs on: `http://localhost:5173`

4. **Open your browser**
   ```
   http://localhost:5173
   ```

## 📁 Project Structure

```
ltm-platform/
├── backend/                    # Python Flask API
│   ├── src/
│   │   └── backend/
│   │       ├── app.py          # Flask app config
│   │       ├── api/
│   │       │   └── routes.py   # REST endpoints
│   │       └── models/
│   │           ├── database.py
│   │           └── models.py   # SQLAlchemy models
│   ├── pyproject.toml         # uv dependencies
│   └── run.py
│
├── frontend/                   # React + Vite
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   ├── api/
│   │   │   └── client.js       # API client
│   │   ├── App.jsx             # Main app
│   │   └── main.jsx            # Entry point
│   ├── package.json            # Node dependencies
│   ├── vite.config.js
│   └── README.md
│
├── static/                     # Legacy static files
├── templates/                  # Legacy templates
├── README.md                   # This file
└── .gitignore
```

## 🔌 API Endpoints

### Questions
- `GET /api/questions?type=couple` - Get all couple questions
- `GET /api/questions?type=parent` - Get all parent questions
- `GET /api/questions/:id` - Get specific question

### Responses
- `POST /api/responses/couple` - Submit couple responses
- `POST /api/responses/parent` - Submit parent responses

### Health
- `GET /api/health` - Health check

### Example API Usage

```bash
# Get couple questions
curl http://localhost:5000/api/questions?type=couple

# Submit responses
curl -X POST http://localhost:5000/api/responses/couple \
  -H "Content-Type: application/json" \
  -d '{"responses": [{"question_id": 1, "response": "My answer"}]}'
```

## 🛠️ Development

### Backend Development
```bash
# Using uv
uv run python run.py

# Or using pip
python run.py  # Auto-reload on changes
```

### Frontend Development
```bash
cd frontend
npm run dev  # Hot reload on changes
```

### Code Quality

**Backend:**
```bash
# Format with black
black src/

# Lint with flake8
flake8 src/
```

**Frontend:**
```bash
cd frontend
npm run lint
npm run build
```

## 🗄️ Database

SQLite is used by default. The database file `ltm.db` is created automatically on first run.

To reset the database:
```bash
rm ltm.db
python run.py  # Recreates the DB with seed questions
```

## 📦 Technology Stack

**Frontend:**
- React 18
- Vite (fast dev server)
- React Router (navigation)
- TanStack Query (data fetching)
- Axios (HTTP client)

**Backend:**
- Flask 3.0 (web framework)
- SQLAlchemy (ORM)
- python-dotenv (config)
- Flask-CORS (API access)
- uv (Python package manager)

**Database:**
- SQLite (dev)
- PostgreSQL (production-ready)

## 🚢 Deployment

### Deploy Backend (Heroku/Railway/Render)
```bash
# Use uv or pip to install dependencies
uv sync
# Then use gunicorn for production
pip install gunicorn
gunicorn src.backend.app:app
```

### Deploy Frontend (Vercel/Netlify)
```bash
cd frontend
npm run build
# Deploy dist/ folder
```

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📝 License

MIT

## 💬 Support

Open an issue on GitHub

