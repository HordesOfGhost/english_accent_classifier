from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config import STATIC_DIR
from routers import routes

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(routes.router)