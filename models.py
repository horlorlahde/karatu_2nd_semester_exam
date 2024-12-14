# models.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class User(BaseModel):
    id: UUID = uuid4()
    name: str
    email: EmailStr
    is_active: bool = True

class Book(BaseModel):
    id: UUID = uuid4()
    title: str
    author: str
    is_available: bool = True

class BorrowRecord(BaseModel):
    id: UUID = uuid4()
    user_id: UUID
    book_id: UUID
    borrow_date: datetime = datetime.now()
    return_date: Optional[datetime] = None
