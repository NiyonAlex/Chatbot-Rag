from sqlalchemy import ARRAY, Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.db.base import Base

public_models = [
    "gpt-3.5-turbo",
    "gpt-4-1106-preview",
    "gpt-4o",
    "Llama-2-70B-Chat",
    "Meta-Llama-3-70b-Instruct",
    "Mixtral-8x7B-Instruct",
    "MPT-7B-Instruct",
    "MPT-30B-Instruct",
    "DBRX-Instruct",
]


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    project_name = Column(String, nullable=False)
    team_name = Column(String, nullable=False)
    account_type = Column(String, default="dev")
    openai_api_key_type = Column(String, default="dev")
    openai_api_key_name = Column(String, nullable=False)
    quota = Column(Integer, default=2000)
    usage = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, **data):
        super().__init__(updated_at=func.now(), **data)
