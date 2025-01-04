import os
import socket

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.db.base import Base
from app.db.session import engine
from app.ui.api.router import ui_router

load_dotenv()


def start_app():
    app = FastAPI(title=os.getenv("PROJECT_NAME"))
    app.mount(
        "/styles", StaticFiles(directory="app/ui/templates/styles"), name="styles"
    )
    app.mount(
        "/scripts", StaticFiles(directory="app/ui/templates/scripts"), name="scripts"
    )

    # Create tables

    print("--- Engine ---")
    print(engine)
    print("--- Engine End ---")
    Base.metadata.create_all(bind=engine)

    # inlcude UI router
    app.include_router(ui_router)

    # include app router

    return app


app = start_app()

if os.getenv("RUN_LOCALLY"):

    @app.middleware("http")
    async def add_middleware(request: Request, call_next):
        response = await call_next(request)
        print(f"Container ID: {socket.gethostname()}")

        return response
