# Deployment Guide

Minimal steps to deploy LTM platform to production.

## 🎯 Quick Deployment (Free)

### Backend: Railway / Render
- Push to GitHub
- Deploy from GitHub
- Add env vars: `SECRET_KEY`, `DATABASE_URL`, `FLASK_ENV=production`

### Frontend: Vercel
- Import from GitHub
- Root: `frontend`
- Build: `npm run build`
- Env: `VITE_API_URL=https://your-backend-url/api`

## 📋 Pre-Deployment Checklist

**Files to create:**
- `Procfile` (for Railway/Heroku)
- `requirements.txt` (backup for pip-based platforms)

**Changes needed:**
- Update CORS origins in `src/backend/app.py` to production domain
- Set environment variables in hosting platform
- Rebuild frontend with production API URL

## 🔐 Required Environment Variables

**Backend:**
- `SECRET_KEY` - Generate random string
- `DATABASE_URL` - PostgreSQL (auto-provided) or sqlite
- `FLASK_ENV=production`

**Frontend:**
- `VITE_API_URL` - Your backend API URL

## 💰 Cost

**Free tier covers:**
- Railway: 500 hours/month free
- Vercel: Free for most sites
- Database: Free PostgreSQL on Railway

