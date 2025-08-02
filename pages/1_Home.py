import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import st_folium

# Config
st.set_page_config(page_title="🔥 Fire Insights Dashboard", layout="wide")
st.title("🌍 Fire Data Visualization Dashboard")
st.markdown("---")

# Data loading
df = pd.concat([
    pd.read_csv("data_2021.csv"),
    pd.read_csv("data_2022.csv"),
    pd.read_csv("data_2023.csv")
], ignore_index=True)

# Numericals
numerical_cols = ['brightness', 'scan', 'track', 'acq_time', 'confidence', 'version', 'bright_t31', 'frp']

# Seaborn Plot Wrapper
def sns_plot(plot_func, **kwargs):
    title = kwargs.pop('title', '')
    xlabel = kwargs.pop('xlabel', '')
    ylabel = kwargs.pop('ylabel', '')
    fig, ax = plt.subplots(figsize=kwargs.pop('figsize', (8, 6)))
    plot_func(ax=ax, **kwargs)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# Heatmap separately
def sns_heatmap_plot(data):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

# Sidebar Toggles
with st.sidebar:
    st.markdown("## 🔧 Controls")
    show_map = st.checkbox("Show Fire Location Map", value=True)
    show_heatmap = st.checkbox("Show Correlation Heatmap", value=True)

# Reusable plotting grid layout
def plot_row(title1, desc1, func1, title2, desc2, func2):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### 🔥 {title1}")
        st.markdown(desc1)
        func1()
    with col2:
        st.markdown(f"### 🔥 {title2}")
        st.markdown(desc2)
        func2()
    st.markdown("---")


# Plots Begin
plot_row(
    "Fire Type Distribution",
    "This chart represents the types of fires recorded via satellite imagery. "
    "Understanding the distribution helps assess the nature of fire events—whether they’re vegetation fires, industrial, or others.",
    lambda: sns_plot(sns.countplot, x='type', data=df, title='Fire Types', xlabel='Type', ylabel='Count'),

    "Confidence Score Distribution",
    "This histogram displays the confidence levels assigned by satellite systems when detecting fires. "
    "Higher values imply more reliable detections, while lower scores might be false positives or noisy data.",
    lambda: sns_plot(sns.histplot, x='confidence', data=df, bins=20, kde=True,
                     title='Confidence Levels', xlabel='Confidence', ylabel='Frequency')
)

plot_row(
    "Confidence by Fire Type",
    "A boxplot to observe how detection confidence varies across different fire categories. "
    "It helps identify if certain types consistently receive lower or higher detection certainty.",
    lambda: sns_plot(sns.boxplot, x='type', y='confidence', data=df,
                     title='Confidence by Type', xlabel='Type', ylabel='Confidence'),

    "Satellite Detection Count",
    "Different satellites contribute to fire detection. This countplot shows which satellites were most active or effective during the recorded years.",
    lambda: sns_plot(sns.countplot, x='satellite', data=df,
                     title='Satellites Used', xlabel='Satellite', ylabel='Count')
)

plot_row(
    "Brightness vs FRP",
    "This scatterplot shows the relationship between fire brightness (how intense the infrared light is) and FRP (Fire Radiative Power). "
    "It’s useful for understanding how fire intensity translates into thermal energy.",
    lambda: sns_plot(sns.scatterplot, x='brightness', y='frp', data=df,
                     title='Brightness vs FRP', xlabel='Brightness', ylabel='FRP'),

    "Scan vs Track",
    "The scan and track values relate to the satellite's sensor coverage. "
    "This plot helps examine the geometry or positioning of detection and whether anomalies exist.",
    lambda: sns_plot(sns.scatterplot, x='scan', y='track', data=df,
                     title='Scan vs Track', xlabel='Scan', ylabel='Track')
)

plot_row(
    "FRP Distribution",
    "The Fire Radiative Power (FRP) indicates how much energy is being released by the fire. "
    "This histogram reveals the typical energy profile of recorded fire events and any extreme cases.",
    lambda: sns_plot(sns.histplot, x='frp', data=df, bins=30, kde=True,
                     title='FRP Distribution', xlabel='FRP', ylabel='Frequency'),

    "Bright T31 vs FRP",
    "Brightness at thermal band T31 is closely linked to fire temperature. "
    "This plot correlates that thermal reading with FRP to see if hotter fires release significantly more energy.",
    lambda: sns_plot(sns.scatterplot, x='bright_t31', y='frp', data=df,
                     title='T31 Brightness vs FRP', xlabel='Bright T31', ylabel='FRP')
)

if show_heatmap:
    with st.container():
        st.markdown("### 📊 Correlation Heatmap")
        st.markdown(
            "This heatmap visually represents how numerical variables in the dataset correlate with each other. "
            "Strong positive/negative relationships help in selecting predictive features and understanding variable behavior."
        )
        sns_heatmap_plot(df[numerical_cols])
        st.markdown("---")



# Fire Map
if show_map:
    with st.container():
        st.markdown("### 🌐 Fire Locations Map")
        st.markdown(
            "This interactive map plots the geographical locations of fires reported across India. "
            "Each red marker represents a fire, and its intensity (FRP) is shown on hover. Helps analyze spatial patterns of fire activity."
        )
        sample_df = df.sample(n=min(5000, len(df)), random_state=42)
        fire_map = folium.Map(location=[22.351115, 78.667743], zoom_start=5)

        for _, row in sample_df.iterrows():
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=2,
                color='red',
                fill=True,
                fill_opacity=0.6,
                popup=f"FRP: {row['frp']:.2f}"
            ).add_to(fire_map)

        st_folium(fire_map, width=500)
        
        # 🔧 Pull next section closer
        st.markdown("<div style='margin-bottom: -40px;'></div>", unsafe_allow_html=True)

# 🚀 Footer Section
with st.container():
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 14px;'>
            <p>📊 This dashboard was handcrafted with ☕, 🧠, and a hint of late-night overthinking.</p>
            <p>🛰️ Powered by <strong>Terra</strong> & <strong>Aqua</strong> satellites — Earth's official firefighters in orbit.</p>
            <p>© 2025 | Built by <strong>Nitesh</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )

