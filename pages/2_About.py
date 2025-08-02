import streamlit as st

st.set_page_config(page_title="📘 About Fire Dashboard", layout="wide")

st.title("📘 About This App")
st.markdown("---")

# Intro section
st.markdown("### 🔥 Welcome to the Fire Data Visualization Dashboard")
st.markdown(
    """
    This dashboard helps you **explore**, **analyze**, and **visualize** wildfire satellite data from **NASA's Terra and Aqua satellites**.
    The goal is to present complex geospatial and sensor data in a way that even your **non-techie chacha** can understand it 😌.
    """
)

# App Workflow
with st.expander("📂 Data Collection & Preprocessing"):
    st.markdown(
        """
        - 🔭 **Satellite Data Sources:** Terra & Aqua MODIS (Moderate Resolution Imaging Spectroradiometer).
        - 🧹 **Data Files:** `.csv` files containing latitude, longitude, brightness, confidence, and other variables.
        - 📅 **Years Covered:** 2021, 2022, 2023.
        - 🧠 Data is combined using `pandas.concat()` to form a single DataFrame.
        """
    )

with st.expander("📊 Visualizations & Insights"):
    st.markdown(
        """
        - ✅ **Seaborn & Matplotlib:** Used for plotting histograms, boxplots, scatter plots, and count plots.
        - 🧩 **Heatmaps:** Used to show correlation between numerical features.
        - 🌍 **Folium Maps:** Interactive maps to visualize the geospatial fire spread across India.
        - 🧪 Each section is built modularly using `plot_section()` and `plot_row()` for readability.
        """
    )

with st.expander("🧠 How It Works (Behind-the-Scenes)"):
    st.markdown(
        """
        1. 📦 **Data Ingestion:** CSV files are read using `pandas.read_csv()`.
        2. 🧱 **Concatenation:** All yearly dataframes are merged to form one big juicy dataframe.
        3. 🎯 **Plotting:** Predefined seaborn/matplotlib plots are created with custom functions for reuse.
        4. 📍 **Map Rendering:** Using `folium` to plot thousands of points efficiently on a map.
        5. 🔧 **Sidebar Toggles:** Users can choose to show/hide the map or heatmap as per convenience.
        6. 🧪 **Streamlit Rendering:** `st.pyplot()` for graphs and `st_folium()` for maps.
        """
    )

# Feature Highlights
st.markdown("### 🌟 Key Features")
st.markdown(
    """
    - 📌 **Clean UI:** Consistent structure using `st.container()`, rows, and interactive elements.
    - 📈 **Dual Plot View:** Two visualizations side by side for comparison.
    - 🌐 **Geospatial Insights:** Real satellite coordinates shown on live interactive maps.
    - 💬 **Detailed Captions:** Every plot has meaningful titles and descriptions.
    """
)


# Reliability Section
st.markdown("### 🛡️ Data Reliability & Accuracy")
st.success(
    "The data used in this dashboard is sourced from **NASA's FIRMS (Fire Information for Resource Management System)**.\n\n"
    "- 🛰️ **Real-time satellite feeds** from MODIS sensors\n"
    "- 📡 Continuously updated and validated by multiple global agencies\n"
    "- 📅 Covers historical fire trends to recent satellite observations"
)

# Interactive Element - Learn More
with st.expander("🔍 Want to dive deeper into Satellite Systems?"):
    st.markdown(
        """
        **🛰️ Terra (EOS AM-1):**  
        - Launched: 1999  
        - Observes: Land, oceans, and atmosphere in the morning (AM pass)  
        - Sensor: MODIS (Moderate Resolution Imaging Spectroradiometer)

        **🛰️ Aqua (EOS PM-1):**  
        - Launched: 2002  
        - Observes: Afternoon (PM pass)  
        - Complementary to Terra for round-the-clock Earth monitoring

        🔁 Together, they help form a near 24x7 surveillance loop over Earth 🔥🌍
        """
    )

# Emo interactive section
st.markdown("### 😎 Why This Project Rocks")
st.info(
    "Because it's **fast**, **modular**, and makes wildfire data look Fabulous 🧯🔥.\n"
)

# Footer-style closure
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray; font-size:13px;'>"
    "Made with ☕ by <b>Nitesh</b> | Powered by Python, Streamlit 🧠🌙"
    "</div>",
    unsafe_allow_html=True
)
