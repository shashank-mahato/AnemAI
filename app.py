import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home | AI Anemia Detection", page_icon="🩸", layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
        }
        .title {
            font-size: 4rem;  /* Increased title size */
            font-weight: bold;
            color: #B22222;
            text-align: left;
            flex-grow: 1;
        }
        .subtitle {
            font-size: 2.2rem;  /* Increased subtitle size */
            color: #444;
            text-align: left;
            margin-top: 10px;
        }
        .logo {
            max-width: 180px; /* Increased logo size */
            margin-left: auto;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ✅ Header with Title, Subtitle, and Right-Aligned Logo
st.markdown('<div class="header-container">', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])  # Title takes more space, logo takes less
with col1:
    st.markdown("<p class='title'>🩸 AI-Powered Anemia Detection</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>A non-invasive AI tool analyzing eye, lip, & skin images to detect anemia in seconds.</p>", unsafe_allow_html=True)

with col2:
    logo_path = "assets/logo.png"  # Ensure this path is correct!
    try:
        st.image(logo_path, width=180)  # Larger logo on the right
    except:
        st.warning("⚠️ Logo not found. Please check the file path.")

st.markdown('</div>', unsafe_allow_html=True)

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
st.markdown("<p style='text-align:center; font-size:1.5rem;'>🔬 <strong>AI-Powered | Fast | Reliable</strong></p>", unsafe_allow_html=True)
