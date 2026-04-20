import streamlit as st 

st.title("Input Audio and Video ",anchor=False)


st.divider()

st.audio("./audio/audio.mp3",loop=True)  


audio_file = st.file_uploader("Upload your audio file", type=["mp3", "wav"], accept_multiple_files=False)


if audio_file:
    st.audio(audio_file, loop=True)
    
    
st.divider()

st.video("./video/video.mp4")

video_file = st.file_uploader("Upload your video file", type=["mp4", "avi"], accept_multiple_files=False)   

if video_file:
    st.video(video_file)
    
    
button_pressed = st.button("Play Audio and Video")

if button_pressed:
    st.audio("./audio/audio.mp3",loop=True)  
    st.video("./video/video.mp4")   