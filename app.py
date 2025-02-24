import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home | AI Anemia Detection", page_icon="🩸", layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ✅ Load and Display the Transparent Logo
logo_path = "assets/logo.jpg"  # Ensure this exists!
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image(logo_path, width=120)  # Adjust width as needed

# ✅ Title and Subtitle
st.markdown("<p class='title'>🩸 AI-Powered Anemia Detection</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A non-invasive AI tool analyzing eye, lip, & skin images to detect anemia in seconds.</p>", unsafe_allow_html=True)

# ✅ Hero Image
hero_img = "hero_image.jpg"
try:
    st.image(hero_img, use_container_width=True)
except:
    pass 

# ✅ Features Section
st.markdown("### 🌟 Why Use This?")
st.markdown(
    """
    ✅ **No blood tests** – Just upload images.  
    ✅ **Fast & AI-powered** – Results in seconds.  
    ✅ **PPG Analysis** – Optical hemoglobin estimation.
    """,
    unsafe_allow_html=True,
)

st.markdown("---")
st.subheader("🚀 Ready to Check for Anemia?")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔍 Start Diagnosis", help="Proceed to upload your images and begin analysis"):
        st.switch_page("pages/input.py")  

st.markdown("---")
st.markdown("<p style='text-align:center;'>🔬 <strong>AI-Powered | Fast | Reliable</strong></p>", unsafe_allow_html=True)
