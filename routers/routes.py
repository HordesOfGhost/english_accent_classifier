from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from services import download_video, extract_audio, classify_accent, transcribe_and_summarize
from config import TEMPLATES_DIR, MEDIA_DIR

app = FastAPI()
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Ensure media directory exists
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/analyze", response_class=HTMLResponse)
def analyze_accent(request: Request, video_url: str = Form(...)):
    video_filename = "video.mp4"
    audio_filename = "audio.wav"

    video_path = MEDIA_DIR / video_filename
    audio_path = MEDIA_DIR / audio_filename

    result = None
    error = None
    audio_web_path = None
    transcription = None
    summary = None

    try:
        for path in [video_path, audio_path]:
            if path.exists():
                path.unlink()

        download_video(video_url, str(video_path))
        extract_audio(str(video_path), str(audio_path))

        # Classify accent
        accent, confidence, all_confidences = classify_accent(str(audio_path))

        # Convert confidence scores to percentages
        confidence_pct = round(confidence * 100, 2)
        all_confidences_pct = {k: round(v * 100, 2) for k, v in all_confidences.items()}

        # Transcribe and summarize
        transcription_summary = transcribe_and_summarize(str(audio_path))
        transcription = transcription_summary.get("transcription", "")
        summary = transcription_summary.get("summary", "")

        result = {
            "accent": accent,
            "confidence_score": confidence_pct,
            "all_confidence": all_confidences_pct
        }

        audio_web_path = f"/static/media/{audio_filename}"

    except Exception as e:
        error = str(e)

    finally:
        if video_path.exists():
            video_path.unlink()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "error": error,
        "audio_path": audio_web_path,
        "transcription": transcription,
        "summary": summary,
    })
