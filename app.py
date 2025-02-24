import streamlit as st
from PIL import Image

# ✅ Set Page Configuration
st.set_page_config(
    page_title="Home | AI Anemia Detection",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ Hide Sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# ✅ Header Section (Title, Subtitle, Logo)
st.markdown("""
    <style>
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            margin-bottom: 20px;
        }
        .title-container {
            flex-grow: 1;
        }
        .title {
            font-size: 48px;  /* Increased Title Size */
            font-weight: bold;
            color: #B22222;
            margin-bottom: 5px;
        }
        .subtitle {
            font-size: 24px;  /* Increased Subtitle Size */
            color: #444;
        }
        .logo {
            max-width: 140px; /* Adjusted Logo Size */
            margin-left: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Layout for Header
col1, col2 = st.columns([4, 1])  # Title & Subtitle take more space, Logo takes less
with col1:
    st.markdown("<div class='title-container'><p class='title'>🩸 AI-Powered Anemia Detection</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>A non-invasive AI tool analyzing eye, lip, & skin images to detect anemia in seconds.</p></div>", unsafe_allow_html=True)

with col2:
    logo_path = "assets/logo.png"  # Ensure this path is correct!
    try:
        st.image(logo_path, width=140)  # Logo placed on right
    except:
        st.warning("⚠️ Logo not found. Please check the file path.")

# ✅ Hero Image
hero_img = "hero_image.jpg"
try:
    st.image(hero_img, use_container_width=True)
except:
    pass 

# ✅ Features Section
st.markdown("### 🌟 Why Use This?")
st.markdown("""
    - ✅ **No blood tests** – Just upload images.  
    - ✅ **Fast & AI-powered** – Results in seconds.  
    - ✅ **PPG Analysis** – Optical hemoglobin estimation.
""", unsafe_allow_html=True)

st.markdown("---")

# ✅ Start Button
st.subheader("🚀 Ready to Check for Anemia?")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔍 Start Diagnosis", help="Proceed to upload your images and begin analysis"):
        st.switch_page("pages/input.py")  

st.markdown("---")
st.markdown("<p style='text-align:center; font-size:20px;'>🔬 <strong>AI-Powered | Fast | Reliable</strong></p>", unsafe_allow_html=True)
