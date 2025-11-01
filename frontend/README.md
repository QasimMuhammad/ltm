# LTM Frontend

React + Vite frontend for the License to Marry platform.

## Quick Start

```bash
npm install
npm run dev
```

## Scripts

- `npm run dev` - Start dev server (localhost:5173)
- `npm run build` - Production build
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Project Structure

```
src/
├── components/       # Reusable components (Navbar, etc.)
├── pages/           # Page components (Home, Questionnaires, etc.)
├── api/             # API client and endpoints
├── hooks/           # Custom React hooks (future)
├── utils/           # Utility functions (future)
├── App.jsx          # Main app component
├── main.jsx         # Entry point
└── index.css        # Global styles
```

## Environment Variables

Create `.env.local`:
```
VITE_API_URL=http://localhost:5000/api
```

## Development

The frontend communicates with the Flask backend via REST API. Make sure the backend is running on port 5000 before starting the frontend.

### Adding New Features

1. Create components in `src/components/`
2. Create pages in `src/pages/`
3. Add API endpoints in `src/api/client.js`
4. Update routes in `src/App.jsx`

## Tech Stack

- React 18
- Vite 5
- React Router 6
- TanStack Query 5
- Axios

## Troubleshooting

**Port already in use?**
```bash
# Kill the process using port 5173
lsof -ti:5173 | xargs kill -9
```

**API connection issues?**
- Ensure backend is running on `http://localhost:5000`
- Check browser console for CORS errors
- Verify API URL in `src/api/client.js`

