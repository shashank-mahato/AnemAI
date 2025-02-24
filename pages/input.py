import streamlit as st
import time
import cv2
import numpy as np
from PIL import Image
from geopy.geocoders import Nominatim
import requests
import tempfile
import json

MAX_IMAGE_SIZE = (224, 224)

def extract_ppg_signal(video_path):
    """Extracts red channel intensity from PPG video more efficiently."""
    cap = cv2.VideoCapture(video_path)
    red_intensity = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % 5 == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            red_intensity.append(np.mean(frame[:, :, 0])) 
        
        frame_count += 1
    
    cap.release()
    return red_intensity

st.set_page_config(page_title="Anemia Detection", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

st.title("🩸 AI-Powered Anemia Detection")
st.write("Non-Invasive Diagnosis using Eye Conjunctiva, Lip & Skin Analysis")

col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("📷 Upload Images for Analysis")
    eye_image = st.file_uploader("Upload Eye Conjunctiva Image", type=["jpg", "png", "jpeg"], key="eye")
    lip_image = st.file_uploader("Upload Lip Image", type=["jpg", "png", "jpeg"], key="lip")
    skin_image = st.file_uploader("Upload Skin Image", type=["jpg", "png", "jpeg"], key="skin")

with col2:
    st.subheader("📹 Upload PPG Video for Processing")
    ppg_video = st.file_uploader("Upload PPG Video", type=["mp4", "avi"], key="ppg")
    

if eye_image:
    img = Image.open(eye_image).convert("RGB").resize(MAX_IMAGE_SIZE)
    st.session_state["eye_data"] = np.array(img)

if lip_image:
    img = Image.open(lip_image).convert("RGB").resize(MAX_IMAGE_SIZE)
    st.session_state["lip_data"] = np.array(img)

if skin_image:
    img = Image.open(skin_image).convert("RGB").resize(MAX_IMAGE_SIZE)
    st.session_state["skin_data"] = np.array(img)

if ppg_video:
    st.success("✅ Video uploaded successfully!")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(ppg_video.read())
        temp_video_path = temp_file.name
    
    with st.spinner("Extracting PPG data..."):
        ppg_signal = extract_ppg_signal(temp_video_path)
    
    st.session_state["ppg_signal"] = json.dumps(ppg_signal) 
    st.success("📊 PPG Signal Extracted! Data ready for processing.")

st.markdown("---")
if st.button("🔍 Start Diagnosis"):
    if "eye_data" in st.session_state and "lip_data" in st.session_state and "skin_data" in st.session_state:
        st.session_state["navigate_to_processing"] = True
        st.rerun()
    else:
        st.error("⚠️ Please upload all three images before proceeding.")

if "navigate_to_processing" in st.session_state and st.session_state["navigate_to_processing"]:
    st.session_state["navigate_to_processing"] = False 
    st.switch_page("pages/processing.py") 
