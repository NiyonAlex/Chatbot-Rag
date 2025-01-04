from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.hash import Hasher


def get_user(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()


def create_new_user(user: User, db: Session):

    user = User(
        email=user.email,
        password=Hasher.get_hashed(user.password),
        is_active=True,
        is_admin=user.is_admin,
        project_name=user.project_name,
        team_name=user.team_name,
        account_type=user.account_type,
        openai_api_key_type=user.openai_api_key_type,
        openai_api_key_name=user.openai_api_key_name,
        usage=0,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
