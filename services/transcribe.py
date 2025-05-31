from models.gemini import gemini_model
from .config import prompt
from .utils import extract_json_content_from_llm_response

def transcribe_and_summarize(audio_path):
    """
        Transcribe and summarize audio with GEMINI
    """
    with open(audio_path, "rb") as audio_file:
        response = gemini_model.generate_content([
            prompt,
            {"mime_type": "audio/wav", "data": audio_file.read()}
        ]).text
    json_response = extract_json_content_from_llm_response(response)
    return json_response