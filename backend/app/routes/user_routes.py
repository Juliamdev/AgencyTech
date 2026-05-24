from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas.user_schema import UserCreate
from app.schemas.user_schema import UserResponse

from app.services.user_service import create_user_service, delete_user_service, get_users_service, update_user_service

from app.config.database import SessionLocal

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user_service(db, user)

@router.get("/users", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):

    return get_users_service(db)

@router.delete("/users/{user_id}")
def delete_user_route(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = delete_user_service(
        db,
        user_id
    )

    if not user:
        return {
            "message": "User not found"
        }

    return {
        "message": "User deleted"
    }
    
@router.put(
    "/users/{user_id}",
    response_model=UserResponse
)
def update_user_route(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db)
):

    updated_user = update_user_service(
        db,
        user_id,
        user
    )

    if not updated_user:
        return {
            "message": "User not found"
        }

    return updated_user