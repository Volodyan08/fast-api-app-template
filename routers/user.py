from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from services.user import create_user, get_user, update_user, delete_user
from dto.user import User as UserDto

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, tags=["user"])
async def create(user: UserDto, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/{user_id}", tags=["user"])
async def get(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.put("/{user_id}", tags=["user"])
async def update(user_id: int, user: UserDto, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user


@router.delete("/{user_id}", tags=["user"])
async def delete(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user