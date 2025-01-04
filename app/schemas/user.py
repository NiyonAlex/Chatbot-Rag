from fastapi import HTTPException, status
from fastapi import Form
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional

from app.db.models.user import public_models
from app.api.models.request_model import AvailableModels


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)
    project_name: str = Field(...)
    team_name: str = Field(...)
    account_type: str = Field(...)
    openai_api_key_type: str = Field(...)
    openai_api_key_name: str = Field(...)
    openai_quota: int = Field(default=2000)
    is_admin: bool = Field(default=False)


def create_user_from_form(
    email: str = Form(...),
    password: str = Form(..., min_length=4),
    project_name: str = Form(...),
    team_name: str = Form(...),
    account_type: str = Form(...),
    openai_api_key_type: str = Form(...),
    openai_api_key_name: str = Form(...),
    openai_quota: int = Form(default=2000),
) -> UserCreate:
    return UserCreate(
        email=email,
        password=password,
        project_name=project_name,
        team_name=team_name,
        account_type=account_type,
        openai_api_key_type=openai_api_key_type,
        openai_api_key_name=openai_api_key_name,
        openai_quota=openai_quota,
    )


class UserUpdate(BaseModel):
    password: Optional[str] = Field(None, min_length=4)
    is_active: Optional[bool] = Field(None)
    project_name: Optional[str] = Field(None)
    team_name: Optional[str] = Field(None)
    account_type: Optional[str] = Field(None)
    openai_api_key_type: Optional[str] = Field(None)
    openai_api_key_name: Optional[str] = Field(None)
    quota: Optional[int] = Field(None)
    is_admin: Optional[bool] = Field(None)

    class Config:
        schema_extra = {
            "example": {
                "password": "string",
                "is_active": True,
                "project_name": "string",
                "team_name": "string",
                "account_type": "string",
                "openai_api_key_type": "string",
                "openai_api_key_name": "string",
                "quota": 0,
                "is_admin": True,
                "available_models": [model.value for model in AvailableModels],
            }
        }


class ShowUser(BaseModel):
    id: int
    email: EmailStr
    project_name: str
    team_name: str
    team_name: str
    account_type: str
    openai_api_key_type: str
    openai_api_key_name: str
    quota: int
    usage: int
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: datetime

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
