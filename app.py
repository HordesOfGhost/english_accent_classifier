import os
import uuid
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from services import download_video, extract_audio, classify_accent

app = FastAPI()
BASE_DIR = Path(__file__).parent.absolute()
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
MEDIA_DIR = STATIC_DIR / "media"

templates = Jinja2Templates(directory=TEMPLATES_DIR)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Ensure media directory exists
MEDIA_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze", response_class=HTMLResponse)
def analyze_accent(request: Request, video_url: str = Form(...)):
    video_filename = f"video.mp4"
    audio_filename = f"audio.wav"

    video_path = MEDIA_DIR / video_filename
    audio_path = MEDIA_DIR / audio_filename

    result = None
    error = None
    audio_web_path = None

    try:
        # Cleanup any leftover files with same name
        for path in [video_path, audio_path]:
            if path.exists():
                path.unlink()

        # Download & process
        download_video(video_url, str(video_path))
        extract_audio(str(video_path), str(audio_path))
        accent, confidence, all_confidences = classify_accent(str(audio_path))

        result = {
            "accent": accent,
            "confidence_score": confidence,
            "all_confidence": all_confidences
        }
        # Audio path relative to /static for use in HTML
        audio_web_path = f"/static/media/{audio_filename}"

    except Exception as e:
        error = str(e)

    finally:
        if video_path.exists():
            video_path.unlink()
        if audio_path.exists():
            audio_path.unlink()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "error": error,
        "audio_path": audio_web_path
    })
