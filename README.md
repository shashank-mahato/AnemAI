# 🩸AnemAI - AI-Powered Non-Invasive Anemia Detection System

## 🌟 Overview
The **AI-Powered Non-Invasive Anemia Detection System** is an innovative healthcare solution designed to analyze **👁️ eye conjunctiva, 👄 lip, and 🖐️ skin images**, along with **📊 PPG-based hemoglobin estimation**, to detect anemia in a **fast, non-invasive, and efficient** manner. The system leverages **🤖 deep learning models and a Random Forest classifier** to classify anemia risk levels and recommend nearby 👨‍⚕️ doctors based on the user's 📍 location.

---

## 🔬 How It Works

### 🏥 Step 1: **User Input**
- Users **📷 upload or capture** images of their **eye conjunctiva, lips, and skin**.
- They also **🎥 record a PPG video** by placing their finger on the camera for optical hemoglobin estimation.

### ⚙️ Step 2: **Preprocessing & Feature Extraction**
- The uploaded images are resized and normalized for **🧠 deep learning model inference**.
- The PPG video is processed to **extract 🔴 red channel intensity variations**, which serve as key features for hemoglobin estimation.

### 🧑‍🔬 Step 3: **Model Inference & Decision Making**
- **🖥️ Deep Learning Models (TF Lite)**:
  - **👁️ Eye Conjunctiva Model (CNN)**: Detects pallor in the conjunctiva.
  - **👄 Lip Coloration Model (MobileNetV2)**: Analyzes lip paleness.
  - **🖐️ Skin Coloration Model (MobileNetV2)**: Identifies skin pallor.
- **📊 PPG-based Hemoglobin Estimation**
  - The extracted PPG signal is fed into a **🌲 Random Forest model** trained on **📄 CSV-based hemoglobin level data**.

### ⚖️ Step 4: **Weighted Confidence Scoring & Final Classification**
- The outputs from all four models are combined using **⚖️ weighted confidence scores**:
  - **Higher weight for PPG & Eye Models** (more reliable indicators)
  - **Lower weight for Lip & Skin Models**
- The final decision is made:
  - **❗ "Anemic"** if the aggregated score surpasses a set threshold.
  - **✅ "Not Anemic"** otherwise.

### 📋 Step 5: **Result Display & Doctor Recommendation**
- The result is presented along with a **📝 simple report** detailing individual analysis.
- Users can consult a **💬 LangChain-powered AI medical chatbot** for real-time health advice.
- The app fetches **📍 nearby doctors** using **🌍 Google Maps API**, based on the user's location.

---

## 🛠 Tech Stack & Components

### 🤖 **Machine Learning & Deep Learning**
- **🧠 TensorFlow Lite (TF Lite)** – Optimized models for real-time execution
- **📱 MobileNetV2 & CNN-based classifiers** – Image-based anemia detection
- **🌲 Random Forest Classifier** – PPG-based hemoglobin estimation

### 🌐 **Web App Development**
- **🎨 Streamlit** – Interactive UI for seamless user experience
- **📸 OpenCV & PIL** – Image processing and feature extraction
- **📊 NumPy & Pandas** – Data handling and analysis

### 📍 **Geolocation & Doctor Recommendation**
- **🗺️ Google Maps API** – Fetches nearby doctors
- **🌍 Geopy** – Location detection

### 🤖 **AI Chatbot for Medical Advice**
- **💬 LangChain with Llama 3.3-70B** – Provides AI-driven medical insights

---

## 🚀 Key Features
✅ **🩸 Non-Invasive & Fast** – No blood tests required, results in seconds.  
✅ **🤖 Multi-Modal AI Processing** – Image & PPG-based anemia detection.  
✅ **⚡ Real-Time Execution** – Optimized for web and mobile platforms.  
✅ **📍 Doctor Recommendations** – Live location-based specialist suggestions.  
✅ **💬 AI-Powered Chatbot** – Instant health advice from LangChain LLM.  

---

This project revolutionizes anemia detection by making it **accessible, efficient, and AI-powered** for real-world healthcare applications! 💡
