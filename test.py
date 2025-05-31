import os
import tempfile
from services import *
import time

def analyze_accent_from_url(url):

    video_path = "video.mp4"
    audio_path = "test.wav"

    if os.path.exists(audio_path):
        os.remove(audio_path)
    if os.path.exists(video_path):
        os.remove(video_path)

    print("📥 Downloading video...")
    download_video(url, video_path)

    print("🔊 Extracting audio...")
    extract_audio(video_path, audio_path)

    # print("🧠 Transcribing audio using Gemini...")
    # transcript = transcribe_audio_with_gemini(audio_path)
    # print("📝 Transcript snippet:", transcript)

    print("🗣️ Detecting accent...")
    accent, confidence, all_confidences = classify_accent(audio_path)


    os.remove(audio_path)
    os.remove(video_path)
    return {
        "accent": accent,
        "confidence_score": confidence,
        "all_confidence": all_confidences,
        # "transcript_snippet": transcript
    }

video_url = input("Enter public video URL (MP4 or Loom): ")
result = analyze_accent_from_url(video_url)


print("\n=== Result ===")
for key, val in result.items():
    print(f"{key}: {val}")