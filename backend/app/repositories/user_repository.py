from sqlalchemy.orm import Session

from app.model.user_model import User


def create_user(db: Session, user_data):

    user = User(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

def get_users(db: Session):

    return db.query(User).all()

def delete_user(db: Session, user_id: int):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None

    db.delete(user)

    db.commit()

    return user

def update_user(
    db: Session,
    user_id: int,
    user_data
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None

    user.username = user_data.username
    user.email = user_data.email
    user.password = user_data.password

    db.commit()

    db.refresh(user)

    return user