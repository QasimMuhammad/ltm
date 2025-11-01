#!/bin/bash

echo "🚀 Setting up LTM Platform..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    exit 1
fi

echo "✅ Prerequisites check passed"

# Backend setup
echo ""
echo "📦 Setting up backend..."

# Check if uv is installed
if command -v uv &> /dev/null; then
    echo "Using uv for Python dependencies..."
    uv sync
else
    echo "⚠️  uv not found. Installing with pip..."
    pip install flask flask-cors sqlalchemy python-dotenv
fi

# Frontend setup
echo ""
echo "📦 Setting up frontend..."
cd frontend
npm install
cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the application:"
echo ""
echo "Backend:"
echo "  python run.py"
echo ""
echo "Frontend (in a new terminal):"
echo "  cd frontend"
echo "  npm run dev"
echo ""
echo "Open http://localhost:5173 in your browser"

