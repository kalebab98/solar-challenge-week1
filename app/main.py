import streamlit as st
import pandas as pd
from utils import load_data  # Ensure this import path is correct

# Title of the dashboard
st.title("🔆 Solar Potential Comparison Dashboard")

# Instructions on how to use the app
st.markdown("""
    This dashboard compares the solar potential data for different countries. 
    Please select a country from the options below to view its solar data.
""")

# Load data function - replace these file names with actual paths
file_paths = {
    "Sierraleone": "data/sierraleone_clean.csv",  # Update the file paths as per your directory
    "Benin": "data/benin_clean.csv",
    "Togo": "data/togo_clean.csv"
}

# Country selection dropdown
country = st.selectbox("Select a country:", list(file_paths.keys()))

# Load data based on the country selection
if country:
    file_path = file_paths[country]  # Get the file path for the selected country
    try:
        data = load_data(file_path)  # Load the data using the load_data function from utils.py

        # Display data for the selected country
        st.subheader(f"Solar Data for {country}")
        st.write(data)

        # You can add more visualizations or data summaries here
        st.bar_chart(data['solar_potential'])  # Assuming 'solar_potential' is one of the columns in your CSV file
    except Exception as e:
        st.error(f"An error occurred: {e}")
