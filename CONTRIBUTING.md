# Contributing Guide

Thank you for your interest in contributing to the License to Marry project!

## Setup for Development

1. Follow the Quick Start guide in README.md
2. Create your branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Code Style

### Python
- Use type hints for function parameters and return types
- Follow PEP 8 style guide
- Max line length: 100 characters
- Use meaningful variable names
- Format with `black`

### JavaScript/React
- Use functional components and hooks
- Follow ESLint rules
- Use meaningful variable and function names
- Keep components small and focused

## Testing Your Changes

### Backend
```bash
python run.py
curl http://localhost:5000/api/health
```

### Frontend
```bash
cd frontend
npm run dev
# Visit http://localhost:5173
```

## Database Changes

If you modify models in `src/backend/models/models.py`, the database will automatically update on next run (SQLite only).

For production databases, you'll need proper migrations.

## Submitting Pull Requests

1. Write clear commit messages
2. Keep PRs focused and small
3. Test thoroughly
4. Update documentation if needed
5. Reference issues being fixed

## Getting Help

- Open an issue for bug reports or feature requests
- Ask questions in discussions
- Check existing issues before creating new ones

Thank you for contributing! 🎉

