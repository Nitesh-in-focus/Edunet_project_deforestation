# 3_Predict.py
import streamlit as st
import numpy as np
import joblib
import os
import gdown

# Load model and scaler
MODEL_PATH = ("../best_fire_detection_model.pkl")
GDRIVE_URL = "https://drive.google.com/file/d/1T7ea4xBu6pvx4fQpvuzY_Q50HYgBDEEY"
# Download only if not exists
if not os.path.exists(MODEL_PATH):
    gdown.download(GDRIVE_URL, MODEL_PATH, quiet=False)
model = joblib.load(MODEL_PATH)
scaler = joblib.load("scaler.pkl")

# --- Page Title ---
st.markdown("<h2 style='color:#FF6B6B;'>🔥 Fire Type Prediction Tool</h2>", unsafe_allow_html=True)
st.markdown("Use satellite-captured MODIS data to predict the type of fire detected. Ideal for environmental monitoring and early action systems.")
st.markdown("---")

# --- Sidebar Info ---
with st.sidebar:
    st.markdown("### 🔧 Model Details")
    st.info("""
    - Trained using historical MODIS satellite data.
    - Classifies fire types:
        - Vegetation Fire 🌿
        - Offshore Fire 🌊
        - Other Static Land Source 🏜️
    - Scaled input using MinMaxScaler for accuracy.
    """)
    st.markdown("**Confidence Levels:**")
    st.code("low → 0 | nominal → 1 | high → 2", language='python')

# --- Input Section ---
st.markdown("### 🧾 Enter Fire Detection Parameters")
col1, col2 = st.columns(2)

with col1:
    brightness = st.number_input("🌟 Brightness", min_value=200.0, max_value=500.0, value=300.0, step=1.0)
    bright_t31 = st.number_input("🌡️ Brightness T31", min_value=200.0, max_value=500.0, value=290.0, step=1.0)
    frp = st.number_input("🔥 Fire Radiative Power (FRP)", min_value=0.0, max_value=100.0, value=15.0, step=0.5)

with col2:
    scan = st.number_input("📡 Scan", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    track = st.number_input("🚀 Track", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    confidence = st.selectbox("✅ Confidence Level", ["low", "nominal", "high"], index=1)

# --- Prediction Section ---
if st.button("🔍 Predict Fire Type"):
    confidence_map = {"low": 0, "nominal": 1, "high": 2}
    confidence_val = confidence_map[confidence]

    input_data = np.array([[brightness, bright_t31, frp, scan, track, confidence_val]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]

    fire_types = {
        0: "🌿 Vegetation Fire",
        2: "🏜️ Other Static Land Source",
        3: "🌊 Offshore Fire"
    }

    result = fire_types.get(prediction, "❓ Unknown Fire Type")

    # Result Box
    st.success(f"**Predicted Fire Type:** {result}")
    st.markdown("✅ Prediction complete. Use this insight for planning mitigation or alert response.")

    # Visual Feedback
    st.balloons()

# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>"
    "<i>Prediction made using trained ML model. Ensure ground-truth verification before acting on results.</i>"
    "</div>",
    unsafe_allow_html=True
)








