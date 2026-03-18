from pydantic import BaseModel, Field
from typing import Optional

class BookingDates(BaseModel):
    checkin: str
    checkout: str

class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None

class BookingResponse(BaseModel):
    bookingid: int
    booking: BookingModel

class AuthResponse(BaseModel):
    token: str
