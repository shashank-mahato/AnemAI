import streamlit as st
import os
from langchain_groq import ChatGroq

LANGSMITH_TRACING = "true"  # Keep this as a string
LANGSMITH_ENDPOINT = "https://api.smith.langchain.com"
LANGSMITH_API_KEY = st.secrets["LANGSMITH_API_KEY"]
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)

def get_medical_advice(user_query):
    """Fetch AI-generated medical advice based on user input."""
    prompt = f"""
    A patient has undergone non-invasive anemia tests with these results:
    - Eye Conjunctiva: {results['eye']}
    - Lip Coloration: {results['lip']}
    - Skin Coloration: {results['skin']}
    - PPG Hemoglobin Estimate: {results['ppg']} g/dL
    
    The patient asks: {user_query}
    Provide a concise, medically relevant response.
    """
    response = llm.invoke(prompt)
    return response.content  

st.set_page_config(page_title="Anemia Test Results", layout="wide")
st.title("📋 Test Results & AI-Powered Medical Chatbot")
st.markdown("---")

if "anemia_diagnosis" not in st.session_state:
    st.error("⚠️ No test results found! Please go back and process your data.")
    st.stop()

results = {
    "eye": "Pale Conjunctiva - Possible Anemia" if st.session_state.eye_result < 0.5 else "Normal Conjunctiva",
    "lip": "Pale Lips - Possible Anemia" if st.session_state.lip_result < 0.5 else "Normal Lip Coloration",
    "skin": "Pale Skin - Possible Anemia" if st.session_state.skin_result < 0.5 else "Normal Skin Tone",
    "ppg": round(st.session_state.ppg_result, 2) if "ppg_result" in st.session_state else "Unavailable"
}

st.subheader("🩺 Test Results Interpretation")
st.write(f"**Eye Conjunctiva:** {results['eye']}")
st.write(f"**Lip Coloration:** {results['lip']}")
st.write(f"**Skin Coloration:** {results['skin']}")
st.write(f"**PPG Hemoglobin Estimate:** {results['ppg']} g/dL")
st.markdown("---")

st.subheader("💬 Ask AI About Your Results")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything about your anemia test results...")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    ai_response = get_medical_advice(user_input)

    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

    with st.chat_message("assistant"):
        st.markdown(ai_response)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Reprocess Data"):
        st.switch_page("pages/processing.py")

with col2:
    if st.button("📍 Find Nearby Doctors"):
        st.switch_page("pages/doctors.py")
