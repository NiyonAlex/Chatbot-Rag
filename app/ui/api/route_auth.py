import os
from dotenv import load_dotenv

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.ui import templates
from app.schemas.user import UserCreate, create_user_from_form
from app.db.utils.user import create_new_user


router = APIRouter()
load_dotenv()


@router.get("/login", response_class=HTMLResponse)
def login(request: Request):
    access_token = request.cookies.get("access_token")
    if access_token:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/new_user", response_class=HTMLResponse)
def register(
    user: UserCreate = Depends(create_user_from_form), db: Session = Depends(get_db)
):
    user.is_admin = user.email == os.getenv("SUPERUSER")
    user = create_new_user(user, db)

    if user:
        print(f"{user.email} registered successfully")
        return RedirectResponse(url="/", status_code=303)
