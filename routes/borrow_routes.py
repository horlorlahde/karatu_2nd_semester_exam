
# routes/borrow_routes.py
from fastapi import APIRouter, HTTPException
from models import BorrowRecord, User, Book
from typing import List
from uuid import UUID
from datetime import datetime
from routes.user_routes import users
from routes.book_routes import books

router = APIRouter()
borrow_records: List[BorrowRecord] = []

@router.post("/borrow", response_model=BorrowRecord)
def borrow_book(user_id: UUID, book_id: UUID):
    # Check user and book availability
    user = next((u for u in users if u.id == user_id and u.is_active), None)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or inactive user")

    book = next((b for b in books if b.id == book_id and b.is_available), None)
    if not book:
        raise HTTPException(status_code=400, detail="Book is not available")

    # Check if user already borrowed the book
    if any(record.user_id == user_id and record.book_id == book_id and not record.return_date for record in borrow_records):
        raise HTTPException(status_code=400, detail="User has already borrowed this book")

    # Create borrow record
    book.is_available = False
    record = BorrowRecord(user_id=user_id, book_id=book_id)
    borrow_records.append(record)
    return record

@router.post("/return", response_model=BorrowRecord)
def return_book(user_id: UUID, book_id: UUID):
    for record in borrow_records:
        if record.user_id == user_id and record.book_id == book_id and not record.return_date:
            record.return_date = datetime.now()
            for book in books:
                if book.id == book_id:
                    book.is_available = True
                    return record
    raise HTTPException(status_code=400, detail="No active borrow record found")

@router.get("/records", response_model=List[BorrowRecord])
def list_borrow_records():
    return borrow_records

@router.get("/records/{user_id}", response_model=List[BorrowRecord])
def user_borrow_records(user_id: UUID):
    return [record for record in borrow_records if record.user_id == user_id]
