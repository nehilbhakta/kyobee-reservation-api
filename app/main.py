from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import schemas, crud

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kyobee Reservation API",
    version="1.0.0",
    description="A demo REST API for reservations built with FastAPI + SQLAlchemy.",
)

# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/reservations", response_model=schemas.ReservationOut, status_code=201)
def create_reservation(payload: schemas.ReservationCreate, db: Session = Depends(get_db)):
    return crud.create_reservation(db, payload)

@app.get("/reservations/{reservation_id}", response_model=schemas.ReservationOut)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    r = crud.get_reservation(db, reservation_id)
    if not r:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return r

@app.get("/reservations", response_model=list[schemas.ReservationOut])
def list_reservations(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.list_reservations(db, skip=skip, limit=limit)

@app.patch("/reservations/{reservation_id}/status", response_model=schemas.ReservationOut)
def update_reservation_status(
    reservation_id: int,
    payload: schemas.ReservationUpdateStatus,
    db: Session = Depends(get_db),
):
    r = crud.get_reservation(db, reservation_id)
    if not r:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return crud.update_status(db, r, payload.status)

@app.delete("/reservations/{reservation_id}", status_code=204)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    r = crud.get_reservation(db, reservation_id)
    if not r:
        raise HTTPException(status_code=404, detail="Reservation not found")
    crud.delete_reservation(db, r)
    return None
