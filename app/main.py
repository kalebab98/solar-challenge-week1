import streamlit as st
import pandas as pd
from utils import load_data  # Make sure this is the correct path to your utils.py

# Title of the dashboard
st.title("🔆 Solar Potential Comparison Dashboard")

# Instructions on how to use the app
st.markdown("""
    This dashboard compares the solar potential data for different countries. 
    Please select a country from the options below to view its solar data.
""")

# Load data function - replace these file names with actual paths
file_paths = {
    "Sierraleone": "sierraleone_clean.csv",
    "Benin": "benin_clean.csv",
    "Togo": "togo_clean.csv"
}

# Country selection dropdown
country = st.selectbox("Select a country:", list(file_paths.keys()))

# Load data based on the country selection
if country:
    data = load_data(file_paths[country])

    # Display data for the selected country
    st.subheader(f"Solar Data for {country}")
    st.write(data)

    # You can add more visualizations or data summaries here
    st.bar_chart(data['solar_potential'])  # Assuming 'solar_potential' is one of the columns in your CSV file

