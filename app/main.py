import streamlit as st
import pandas as pd
import os
from utils import load_data  # Make sure this is the correct path to your utils.py

# Title of the dashboard
st.title("🔆 Solar Potential Comparison Dashboard")

# Instructions on how to use the app
st.markdown("""
    This dashboard compares the solar potential data for different countries. 
    Please select a country from the options below to view its solar data.
""")

# Define the file paths for each country's data (assuming CSVs are in the same directory as main.py)
file_paths = {
    "Sierraleone": "sierraleone_clean.csv",  # Adjust to your correct file name if needed
    "Benin": "benin_clean.csv",
    "Togo": "togo_clean.csv"
}

# Country selection dropdown
country = st.selectbox("Select a country:", list(file_paths.keys()))

# Function to check if file exists
def check_file_exists(file_path):
    return os.path.exists(file_path)

# Load data based on the country selection
if country:
    # Check if the file exists before trying to load it
    selected_file_path = file_paths[country]
    if check_file_exists(selected_file_path):
        data = load_data(selected_file_path)

        # Display data for the selected country
        st.subheader(f"Solar Data for {country}")
        st.write(data)

        # You can add more visualizations or data summaries here
        st.bar_chart(data['solar_potential'])
    else:
        st.error(f"File not found: {selected_file_path}")
