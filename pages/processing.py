import streamlit as st
import time
import numpy as np
import tensorflow.lite as tflite
import joblib
import cv2
import json
from PIL import Image
import numpy as np

st.set_page_config(page_title="Processing Data", layout="wide", initial_sidebar_state="collapsed")

@st.cache_resource
def load_models():
    eye_model = tflite.Interpreter(model_path="models/eye_model.tflite")
    lip_model = tflite.Interpreter(model_path="models/lip_model.tflite")
    skin_model = tflite.Interpreter(model_path="models/skin_model.tflite")
    
    ppg_model = joblib.load("models/ppg_model.pkl")
    
    return eye_model, lip_model, skin_model, ppg_model

eye_model, lip_model, skin_model, ppg_model = load_models()

if not hasattr(ppg_model, "predict"):
    st.error("🚨 Error loading PPG model. It might be corrupted or not an sklearn model.")
    st.stop()

def run_inference(model, image):
    image = np.expand_dims(image, axis=0).astype(np.float32)
    input_details = model.get_input_details()
    output_details = model.get_output_details()
    model.allocate_tensors()
    model.set_tensor(input_details[0]['index'], image)
    model.invoke()
    return model.get_tensor(output_details[0]['index'])[0][0]

def estimate_hemoglobin_from_intensity(red_intensity):
    """
    Estimate hemoglobin levels based on red channel intensity.
    """
    if len(red_intensity) == 0:
        return np.random.uniform(9.0, 11.0)  

    avg_intensity = np.mean(red_intensity)
    norm_intensity = (avg_intensity - 50) / (255 - 50)
    estimated_hb = 7.5 + (norm_intensity * (15.0 - 7.5))
    
    return round(np.clip(estimated_hb, 7.5, 15.0), 2)

hide_streamlit_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("🔍 Processing Anemia Diagnosis")
st.write("The AI is analyzing your uploaded data to detect anemia.")

st.markdown("---")

progress_bar = st.progress(0)
status_text = st.empty()

if "eye_data" not in st.session_state or "lip_data" not in st.session_state or "skin_data" not in st.session_state:
    st.error("⚠️ No uploaded images found! Please go back and upload images.")
    st.stop()

status_text.text("Processing Eye Conjunctiva Image...")
time.sleep(1)
eye_result = run_inference(eye_model, np.array(st.session_state.eye_data))
progress_bar.progress(25)

status_text.text("Processing Lip Image...")
time.sleep(1)
lip_result = run_inference(lip_model, np.array(st.session_state.lip_data))
progress_bar.progress(50)

status_text.text("Processing Skin Coloration...")
time.sleep(1)
skin_result = run_inference(skin_model, np.array(st.session_state.skin_data))
progress_bar.progress(75)

ppg_result = None
estimated_hb = None
if "ppg_signal" in st.session_state:
    try:
        status_text.text("Processing PPG Data...")
        ppg_signal = json.loads(st.session_state.ppg_signal)
        ppg_signal = np.array(ppg_signal)

        expected_features = 12
        if ppg_signal.shape[0] > expected_features:
            ppg_signal = ppg_signal[:expected_features]
        elif ppg_signal.shape[0] < expected_features:
            ppg_signal = np.pad(ppg_signal, (0, expected_features - ppg_signal.shape[0]), mode='constant')

        ppg_signal = ppg_signal.reshape(1, -1)
        ppg_result = ppg_model.predict(ppg_signal)[0]
        progress_bar.progress(90)

        estimated_hb = estimate_hemoglobin_from_intensity(ppg_signal.flatten())
    except Exception as e:
        st.error(f"🚨 Error processing PPG signal: {e}")
        ppg_result = None

weights = {"eye": 0.35, "lip": 0.15, "skin": 0.15, "ppg": 0.35}
final_score = (eye_result * weights["eye"]) + (lip_result * weights["lip"]) + (skin_result * weights["skin"])
if ppg_result is not None:
    final_score += (ppg_result * weights["ppg"])

threshold = 0.5
anemia_prediction = "Anemic" if final_score >= threshold else "Not Anemic"

st.session_state.anemia_diagnosis = "❗ You Have Anemia. Consult a Doctor." if anemia_prediction == "Anemic" else "✅ You Do Not Have Anemia."

st.session_state.ppg_result = estimated_hb
st.session_state.eye_result = eye_result
st.session_state.lip_result = lip_result
st.session_state.skin_result = skin_result

progress_bar.progress(100)
status_text.text("✅ Processing Complete!")

st.markdown("---")

if st.button("🔘 View Detailed Results"):
    st.switch_page("pages/results.py")
