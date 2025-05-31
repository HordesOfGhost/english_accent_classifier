# Accent Detector App

This app detects the accent from a video URL (YouTube or Loom), extracts the audio, classifies the accent, transcribes the audio to English, and generates a summary of the transcription.

## Features

- Accepts a public video URL.
- Downloads the video and extracts the audio.
- Classifies the accent using a pretrained accent classification model.
- Transcribes the extracted audio to English.
- Generates a brief summary of the transcription.

## Models Used

- **Transcription & Summary Generation:** `gemini-2.0-flash`
- **Accent Classification:** [`Jzuluaga/accent-id-commonaccent_ecapa`](https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa)

## Getting Started

### Installation

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
````

### Run the App

Start the FastAPI server with auto-reload enabled:

```bash
uvicorn app:app --reload
```

### Usage

Open your browser and navigate to `http://localhost:8000`.
Enter a public video URL and click "Analyze" to get the accent classification, transcription, and summary.

---

