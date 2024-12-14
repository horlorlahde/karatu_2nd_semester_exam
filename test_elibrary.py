import pytest
from fastapi.testclient import TestClient
from main import app
from models import User, Book

client = TestClient(app)

# Mock Data for Tests
mock_user = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "is_active": True
}

mock_book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "is_available": True
}

def test_create_user():
    response = client.post("/users/", json=mock_user)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == mock_user["name"]
    assert data["email"] == mock_user["email"]
    assert data["is_active"] is True
    global user_id
    user_id = data["id"]

    
def test_create_book():
    response = client.post("/books/", json=mock_book)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == mock_book["title"]
    assert data["author"] == mock_book["author"]
    assert data["is_available"] is True
    global book_id
    book_id = data["id"]

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert any(user["email"] == mock_user["email"] for user in data)

def test_list_books():
    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert any(book["title"] == mock_book["title"] for book in data)

def test_deactivate_user():
    response = client.put(f"/users/{user_id}/deactivate")
    assert response.status_code == 200
    data = response.json()
    assert data["is_active"] is False



# def test_borrow_book():
#     response = client.post("/borrow/borrow", json={"user_id": user_id, "book_id": book_id})
#     assert response.status_code == 200
#     data = response.json()
#     assert data["user_id"] == user_id
#     assert data["book_id"] == book_id

# def test_borrow_unavailable_book():
#     response = client.post("/borrow/borrow", json={"user_id": user_id, "book_id": book_id})
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Book is not available"

# def test_return_book():
#     response = client.post("/borrow/return", json={"user_id": user_id, "book_id": book_id})
#     assert response.status_code == 200
#     data = response.json()
#     assert data["return_date"] is not None

# def test_return_non_borrowed_book():
#     response = client.post("/borrow/return", json={"user_id": user_id, "book_id": book_id})
#     assert response.status_code == 400
#     assert response.json()["detail"] == "No active borrow record found"


# def test_borrow_with_inactive_user():
#     response = client.post("/borrow/borrow", json={"user_id": user_id, "book_id": book_id})
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Invalid or inactive user"
