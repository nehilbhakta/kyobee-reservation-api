from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Literal

ReservationStatus = Literal["BOOKED", "CHECKED_IN", "CANCELLED"]

class ReservationCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=100)
    phone: Optional[str] = Field(default=None, max_length=30)
    party_size: int = Field(ge=1, le=50)
    reservation_time: datetime

class ReservationUpdateStatus(BaseModel):
    status: ReservationStatus

class ReservationOut(BaseModel):
    id: int
    customer_name: str
    phone: Optional[str]
    party_size: int
    reservation_time: datetime
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
