# Deployment Checklist

Use this when actually deploying.

## Before Deployment

- [ ] Create `Procfile` with gunicorn command
- [ ] Create `requirements.txt` with all dependencies
- [ ] Update CORS to include production frontend URL
- [ ] Generate strong `SECRET_KEY`

## Backend Deployment

- [ ] Push code to GitHub
- [ ] Create account on Railway/Render
- [ ] Connect GitHub repository
- [ ] Add environment variables
- [ ] Verify auto-deployment works
- [ ] Test backend API endpoints
- [ ] Note backend URL

## Frontend Deployment

- [ ] Create account on Vercel/Netlify
- [ ] Connect GitHub repository
- [ ] Set root directory to `frontend`
- [ ] Add `VITE_API_URL` environment variable
- [ ] Build and deploy
- [ ] Test all pages
- [ ] Verify API connection

## Post-Deployment

- [ ] Test complete user flow
- [ ] Test all questionnaires
- [ ] Verify data persistence
- [ ] Check CORS errors in browser console
- [ ] Monitor logs for errors
- [ ] Set up custom domain (optional)

