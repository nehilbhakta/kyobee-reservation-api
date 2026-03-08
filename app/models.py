from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)
    phone = Column(String(30), nullable=True)
    party_size = Column(Integer, nullable=False)
    reservation_time = Column(DateTime(timezone=True), nullable=False)
    status = Column(String(20), nullable=False, default="BOOKED")  # BOOKED/CHECKED_IN/CANCELLED

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
