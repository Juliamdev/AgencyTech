from sqlalchemy.orm import Session

from app.repositories.user_repository import create_user, delete_user, update_user
from app.repositories.user_repository import get_users
from app.utils.security import hash_password

def create_user_service(db: Session, user_data):

    user_data.password = hash_password(
    user_data.password
)

    return create_user(db, user_data)

def get_users_service(db: Session):

    return get_users(db)

def delete_user_service(
    db: Session,
    user_id: int
):

    return delete_user(db, user_id)

def update_user_service(
    db: Session,
    user_id: int,
    user_data
):

    return update_user(
        db,
        user_id,
        user_data
    )