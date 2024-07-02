from models.user import User
from sqlalchemy.orm import Session
from dto.user import User as UserDto


def create_user(db: Session, user: UserDto):
    db_user = User(name=user.name)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, user: UserDto):
    db_user = db.query(User).filter(User.id == user_id).first()

    db_user.name = user.name

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()

    db.delete(db_user)
    db.commit()
    return db_user
