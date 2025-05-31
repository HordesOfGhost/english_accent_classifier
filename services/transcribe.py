from models.gemini import gemini_model

def transcribe_audio_with_gemini(audio_path):
    with open(audio_path, "rb") as audio_file:
        response = gemini_model.generate_content([
            "You are an English transcription assistant. Transcribe the following audio file in English.",
            {"mime_type": "audio/wav", "data": audio_file.read()}
        ])
    return response.text.strip()