from sqlalchemy.orm import Session
from . import models, schemas

def create_reservation(db: Session, payload: schemas.ReservationCreate) -> models.Reservation:
    reservation = models.Reservation(
        customer_name=payload.customer_name,
        phone=payload.phone,
        party_size=payload.party_size,
        reservation_time=payload.reservation_time,
        status="BOOKED",
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation

def get_reservation(db: Session, reservation_id: int):
    return db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()

def list_reservations(db: Session, skip: int = 0, limit: int = 50):
    return (
        db.query(models.Reservation)
        .order_by(models.Reservation.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def update_status(db: Session, reservation: models.Reservation, status: str) -> models.Reservation:
    reservation.status = status
    db.commit()
    db.refresh(reservation)
    return reservation

def delete_reservation(db: Session, reservation: models.Reservation) -> None:
    db.delete(reservation)
    db.commit()
