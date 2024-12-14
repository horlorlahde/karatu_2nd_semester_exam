
# routes/book_routes.py
from fastapi import APIRouter, HTTPException
from models import Book
from typing import List
from uuid import UUID

router = APIRouter()
books: List[Book] = []

@router.post("/", response_model=Book)
def create_book(book: Book):
    books.append(book)
    return book

@router.get("/", response_model=List[Book])
def list_books():
    return books

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: UUID, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}", response_model=Book)
def delete_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/{book_id}/unavailable", response_model=Book)
def mark_book_unavailable(book_id: UUID):
    for book in books:
        if book.id == book_id:
            book.is_available = False
            return book
    raise HTTPException(status_code=404, detail="Book not found")
