import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home | AI Anemia Detection", page_icon="🩸", layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            margin-top: 30px; /* Increased margin for more space */
        }
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #B22222;
            margin-top: 15px;
        }
        .subtitle {
            font-size: 1.3rem;
            color: #444;
            margin-top: 5px;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ✅ Logo, Title & Subtitle (All Centered)
st.markdown("<div class='container'>", unsafe_allow_html=True)

# **Try loading the logo**
logo_path = "assets/logo.png"  # Ensure the file exists in this path!
try:
    st.image(logo_path, width=150)  # Increased width for better visibility
except:
    st.warning("⚠️ Logo not found. Please check the file path.")

st.markdown(
    """
    <p class="title">🩸 AI-Powered Anemia Detection</p>
    <p class="subtitle">A non-invasive AI tool analyzing eye, lip, & skin images to detect anemia in seconds.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

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
