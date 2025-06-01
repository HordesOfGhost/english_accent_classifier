import streamlit as st
from services import analyze_video
import os

st.set_page_config(page_title="Accent Analyzer", page_icon="🧠")

st.title("🎧 English Accent Analyzer")

# Input form
with st.form("video_form"):
    video_url = st.text_input("🔗 Enter Video URL", placeholder="https://...")
    submitted = st.form_submit_button("Analyze")

# On form submission
if submitted:
    if not video_url:
        st.error("Please provide a video URL.")
    else:
        with st.spinner("Analyzing video..."):
            response = analyze_video(None, video_url)

        # Handle error
        if response["error"]:
            st.error(f"❌ Error: {response['error']}")
        else:
            result = response["result"]
            transcription = response["transcription"]
            summary = response["summary"]
            audio_path = response["audio_path"]

            st.success("✅ Analysis complete!")

            # Video preview
            if "youtube.com" in video_url or "youtu.be" in video_url:
                st.video(video_url)

            # Main Accent Prediction
            st.header("📊 Predicted Accent")
            col1, col2 = st.columns(2)
            col1.metric("Accent", result["accent"])
            col2.metric("Confidence", f"{result['confidence_score']} %")

            # All confidence scores
            st.subheader("🔍 Accent Confidence Breakdown")
            st.bar_chart(result["all_confidence"])
            print(audio_path)
            if audio_path:
                st.text(f"🔎 Path received: {audio_path}")
                if os.path.exists(audio_path):
                    st.subheader("🔊 Extracted Audio")
                    st.audio(audio_path)
                else:
                    st.error("❌ File path doesn't exist.")
            else:
                st.warning("⚠️ No audio path was returned.")
            # Audio playback (if path is valid and accessible from static)
            # if audio_path:
            #     print(audio_path)
            #     st.subheader("🔊 Extracted Audio")
            #     st.audio(audio_path)

            # Transcription & Summary
            st.subheader("📝 Transcription")
            st.write(transcription)

            st.subheader("🧾 Summary")
            st.write(summary)
