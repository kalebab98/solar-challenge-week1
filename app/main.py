import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

# Page setup
st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("🔆 Solar Potential Comparison Dashboard")

st.markdown("""
Compare solar irradiance data from multiple countries.  
Select a country to explore its solar energy potential using visual tools.
""")

# File paths (relative to main.py)
file_paths = {
    "Sierra Leone": "sierraleone_clean.csv",
    "Benin": "benin_clean.csv",
    "Togo": "togo_clean.csv"
}

# Country selection
country = st.selectbox("🌍 Select a Country", options=list(file_paths.keys()))

# Load data
data = load_data(file_paths[country])

if data.empty:
    st.error("Failed to load data. Please check your file paths.")
    st.stop()

# Display raw data
if st.checkbox("📄 Show Raw Data"):
    st.write(data.head())

# Ensure expected column exists
ghi_col = "GHI"
if ghi_col not in data.columns:
    st.error(f"'{ghi_col}' column not found in dataset.")
    st.stop()

# Convert Timestamp column to datetime (if not already)
if "Timestamp" in data.columns:
    data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors="coerce")

# Layout for visuals
col1, col2 = st.columns(2)

# Boxplot of GHI
with col1:
    st.subheader("📦 Boxplot of GHI")
    fig1, ax1 = plt.subplots()
    sns.boxplot(data[ghi_col], ax=ax1)
    ax1.set_xlabel("GHI (W/m²)")
    st.pyplot(fig1)

# Histogram
with col2:
    st.subheader("📊 Histogram of GHI")
    fig2, ax2 = plt.subplots()
    sns.histplot(data[ghi_col], bins=30, kde=True, ax=ax2)
    ax2.set_xlabel("GHI (W/m²)")
    st.pyplot(fig2)

# Time series line chart
if "Timestamp" in data.columns:
    st.subheader("⏱️ Time Series of GHI")
    data_sorted = data.sort_values("Timestamp")
    st.line_chart(data_sorted.set_index("Timestamp")[ghi_col])

# Summary metric
avg_ghi = data[ghi_col].mean()
st.metric("📈 Average GHI", f"{avg_ghi:.2f} W/m²")

# Top 5 timestamps with highest GHI
if "Timestamp" in data.columns:
    st.subheader("🏆 Top 5 GHI Readings")
    top_ghi = data[["Timestamp", ghi_col]].sort_values(by=ghi_col, ascending=False).head(5)
    st.table(top_ghi.reset_index(drop=True))
