import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home | AI Anemia Detection", page_icon="🩸", layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
        .header-container {
            display: flex;
            align-items: center;
            justify-content: flex-start; /* Align logo to the left */
        }
        .logo {
            width: 80px; /* Adjust logo size */
            margin-right: 15px;
        }
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #B22222;
            margin: 0;
        }
        .subtitle {
            text-align: center;
            font-size: 1.3rem;
            color: #444;
            margin-top: 5px;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ✅ Logo & Title in the Same Line (Logo aligned to the left)
logo_path = "assets/logo.png"  # Ensure this exists!
st.markdown(
    f"""
    <div class="header-container">
        <img src="{logo_path}" class="logo">
        <p class="title">🩸 AI-Powered Anemia Detection</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ✅ Subtitle (Centered)
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
