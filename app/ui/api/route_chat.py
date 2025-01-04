from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from app.db.session import get_db
from app.db.models.user import public_models
from app.core.user import get_current_user
from app.ui import templates


from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def chat(request: Request, user_db: Session = Depends(get_db)):
    access_token = request.cookies.get("access_token")

    if access_token:
        try:
            current_user = get_current_user(access_token, user_db)
            return templates.TemplateResponse(
                "app.html",
                {
                    "request": request,
                    "models": current_user.available_models,
                    "username": current_user.email,
                },
            )
        except HTTPException:
            return templates.TemplateResponse(
                "app.html",
                {
                    "request": request,
                    "models": public_models,
                    "landing_page": True,
                    "logout": True,
                },
            )

    return templates.TemplateResponse(
        "app.html",
        {"request": request, "models": public_models, "landing_page": True},
    )
