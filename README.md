# Korapati Sreedhar — Flask Portfolio

A recruiter-focused, responsive portfolio built with **Python + Flask + SQLite + Bootstrap 5**.

## Features
- Modern dark developer UI
- Responsive Bootstrap layout
- Hero section with technical code-card visual
- Skills with animated progress bars
- Project case-study cards
- Internship + education timeline
- Certifications with verification links
- Contact form stored in SQLite
- JSON `/api/profile` endpoint
- `/health` health-check endpoint
- Gunicorn production start command
- Render deployment configuration

## Run locally

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Start:
```bash
python app.py
```

Open:
`http://127.0.0.1:5000`

## Production

```bash
gunicorn app:app
```

## Deploy

### Recommended for the Flask version: Render
1. Push this folder to GitHub.
2. Create a new Web Service on Render.
3. Select the GitHub repository.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Add a strong `SECRET_KEY` environment variable.
7. Deploy.

### Netlify note
Netlify is excellent for static HTML/CSS/JS, but a traditional Flask server should be deployed as a Python web service such as Render. If you specifically need Netlify, use Netlify for a static frontend and host the Flask API separately.

## Important database note
SQLite is perfect for local development. On many cloud hosts, local filesystem storage is not persistent across redeploys/restarts. For production contact-message storage, move `DATABASE_URL` to a managed PostgreSQL database.

## Personalization
Update `PROFILE`, `SKILLS`, `PROJECTS`, `EDUCATION`, and `CERTIFICATIONS` in `app.py`.

Do not add claims, metrics, project URLs, or technologies that are not actually on your resume/experience.
