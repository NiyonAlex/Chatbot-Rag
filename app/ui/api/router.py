from fastapi import APIRouter

from app.ui.api import route_auth, route_chat

ui_router = APIRouter()

ui_router.include_router(route_chat.router, prefix="", tags=["chatbot"])
ui_router.include_router(route_auth.router, prefix="", tags=["auth"])
