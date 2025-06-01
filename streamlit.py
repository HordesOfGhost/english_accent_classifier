# streamlit_app.py
import streamlit as st
from services import analyze_video

# Title
st.title("Video Accent Analyzer")

# Input form
with st.form("video_form"):
    video_url = st.text_input("Enter Video URL", placeholder="https://...")
    submitted = st.form_submit_button("Analyze")

# When the form is submitted
if submitted:
    if not video_url:
        st.error("Please provide a video URL.")
    else:
        with st.spinner("Analyzing video..."):
            result = analyze_video(None, video_url)  # 'request' is not used in Streamlit
            if isinstance(result, dict):
                st.success("Analysis complete!")
                st.json(result)
            else:
                st.error("Unexpected response. Please check the service.")
