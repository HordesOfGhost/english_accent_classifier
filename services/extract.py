from moviepy import VideoFileClip

def extract_audio(video_path, audio_path):
    """
        Extract audio given video path and save to audio path.
    """
    clip = VideoFileClip(video_path)
    try:
        clip.audio.write_audiofile(audio_path, codec='pcm_s16le')  # WAV format
    finally:
        clip.audio.close()
        clip.close()
    return audio_path