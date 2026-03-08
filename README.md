# Kyobee Reservation API

A RESTful backend service for managing reservations, waitlists, and customer check-ins.  
Built to demonstrate API design, SQL data modeling, and clean backend architecture.

---

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite (local) / PostgreSQL (extensible)

---

## Features
- Create and manage reservations
- Update reservation status (BOOKED / CHECKED_IN / CANCELLED)
- List reservations with pagination
- Health check endpoint
- Auto-generated API documentation (Swagger)

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
