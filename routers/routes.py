from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config import TEMPLATES_DIR
from services import analyze_video

app = FastAPI()
templates = Jinja2Templates(directory=TEMPLATES_DIR)

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/analyze", response_class=HTMLResponse)
def analyze_audio_accent(request: Request, video_url: str = Form(...)):
    json_response = analyze_video(request, video_url)
    
    return templates.TemplateResponse("index.html", json_response)