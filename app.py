import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="🔥 Fire App",
    layout="wide",
    page_icon="🔥"
)


# App Title
st.markdown(
    "<h1 style='text-align: center; color: orange;'>🔥 Welcome to the Wildfire Detection App 🔥</h1>",
    unsafe_allow_html=True
)

# Subheading 
st.markdown(
    """
    <div style='text-align: center; font-size:18px;'>
        Analyze satellite fire data, predict fire types, visualize hotspots,<br>
        and explore India's wildfire trends — all in one sleek dashboard.
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("###")

# Quick Guide
with st.expander("📌 How to use this app?"):
    st.markdown("""
    - **🏠 Home** → Explore fire data with graphs, heatmaps, and maps.
    - **📖 About** → Understand how the app works behind the scenes.
    - **🧠 Predict** → Enter values to predict the fire type using ML.
    """)

# Add a horizontal separator
st.markdown("---")

# Encourage Sidebar Navigation
st.markdown(
    "<p style='text-align:center; font-size:16px;'>👉 Use the sidebar to navigate between sections.</p>",
    unsafe_allow_html=True
)

# Footer
st.markdown(
    "<p style='text-align:center; color: gray;'>Made by Nitesh</p>",
    unsafe_allow_html=True
)
