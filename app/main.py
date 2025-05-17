import streamlit as st
import pandas as pd
from utils import load_data

# Title and description
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")
st.title("🔆 Solar Potential Comparison Dashboard")
st.markdown("""
This dashboard allows you to explore solar radiation data across countries.
Use the selector to choose a country and explore its solar trends.
""")

# File paths (expected to be in the same directory as main.py)
file_paths = {
    "Benin": "benin_clean.csv",
    "Sierra Leone": "sierraleone_clean.csv",
    "Togo": "togo_clean.csv"
}

# Country selection
country = st.selectbox("🌍 Select a Country", options=list(file_paths.keys()))
data = load_data(file_paths[country])

if not data.empty:
    st.subheader(f"📊 Raw Data Preview - {country}")
    st.dataframe(data.head())

    ghi_col = "GHI"
    region_col = "WD"  # Example: you can choose a better "region" column based on your dataset

    if ghi_col in data.columns:
        st.subheader("🌞 GHI Boxplot")
        st.box_chart(data[ghi_col])
    else:
        st.error(f"'{ghi_col}' column not found in dataset.")

    # Optional: top "regions" (or any categorical grouping if available)
    if region_col in data.columns:
        st.subheader("🏆 Top Wind Directions by Avg GHI (proxy for region)")
        top_regions = (
            data.groupby(region_col)[ghi_col]
            .mean()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )
        st.table(top_regions)
    else:
        st.warning(f"'{region_col}' column not found for region analysis.")
else:
    st.error("Data could not be loaded. Please check your files.")
