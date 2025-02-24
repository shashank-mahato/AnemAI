import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home | AI Anemia Detection", page_icon="🩸", layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #B22222;
        }
        .subtitle {
            text-align: center;
            font-size: 1.3rem;
            color: #444;
        }
        .features {
            font-size: 1.2rem;
            margin-top: 10px;
        }
        .start-btn {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<p class='title'>🩸 AI-Powered Anemia Detection</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A non-invasive AI tool analyzing eye, lip, & skin images to detect anemia in seconds.</p>", unsafe_allow_html=True)

hero_img = "hero_image.jpg" 
try:
    st.image(hero_img, use_container_width=True)
except:
    pass 

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
