# routes/user_routes.py
from fastapi import APIRouter, HTTPException
from models import User
from typing import List
from uuid import UUID

router = APIRouter()
users: List[User] = []

@router.post("/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@router.get("/", response_model=List[User])
def list_users():
    return users

@router.get("/{user_id}", response_model=User)
def get_user(user_id: UUID):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=User)
def update_user(user_id: UUID, updated_user: User):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: UUID):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}/deactivate", response_model=User)
def deactivate_user(user_id: UUID):
    for user in users:
        if user.id == user_id:
            user.is_active = False
            return user
    raise HTTPException(status_code=404, detail="User not found")
