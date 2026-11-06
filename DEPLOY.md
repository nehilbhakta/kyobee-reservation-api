# Deploying the Kyobee Reservation API

Repo: **nehilbhakta/kyobee-reservation-api**, branch `main`. One Render web
service, no accounts created yet — the deploy below is a one-form step once
signed in to Render.

No endpoints or features were changed for this deploy. The only code change
is CORS in `app/main.py` (from the `CORS_ORIGINS` env var, default `*`, so
Swagger docs work from a browser). `requirements.txt` was already pinned
(fastapi==0.110.0, uvicorn[standard]==0.27.1, SQLAlchemy==2.0.27,
pydantic==2.6.1) and was left untouched.

## Render — manual web service

**Option A — Blueprint (recommended):** Render Dashboard → New →
Blueprint → pick repo `nehilbhakta/kyobee-reservation-api`. Render reads
`render.yaml` at the repo root.

**Option B — manual:**

| Setting | Value |
|---|---|
| Service type | Web Service |
| Runtime / Environment | Python |
| Repository | `nehilbhakta/kyobee-reservation-api`, branch `main` |
| Root Directory | (blank — repo root) |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| Instance | Free |
| Env var `CORS_ORIGINS` | `*` (docs use; restrict to a comma-separated origin list if a frontend is added) |
| Env var `PYTHON_VERSION` | `3.12.3` |

The start module is `app.main:app` (verified — the app lives in
`app/main.py`, with `app/database.py`, `app/models.py`, `app/schemas.py`,
`app/crud.py` alongside it). Run from the repo root, not from `app/`.

## Verify after deploy

- `GET /health` → `{"status": "ok"}`
- Swagger docs: `<render-url>/docs` — try `POST /reservations`,
  `GET /reservations`, `PATCH /reservations/{id}/status`,
  `DELETE /reservations/{id}` from the docs page.

## Caveat — SQLite is ephemeral on Render

The app uses SQLite (`sqlite:///./kyobee.db`, created next to the repo
root on first run). On Render's free tier the filesystem is ephemeral:
reservations are wiped on every redeploy/restart. That is fine for a
demo, but for persistent data the follow-up is a Render PostgreSQL
instance plus a small `app/database.py` change to read `DATABASE_URL` —
deliberately **not** done here (out of scope: deploy config only).
