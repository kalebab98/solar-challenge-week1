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
# Load data based on the country selection
if country:
    data = load_data(file_paths[country])

    # Display data for the selected country
    st.subheader(f"Solar Data for {country}")
    st.write(data)

    # Check the columns to identify the one to use for solar potential
    st.write("Columns in the data:", data.columns)

    # Assuming 'GHI' is the column you want to visualize
    if 'GHI' in data.columns:
        st.bar_chart(data['GHI'])  # Display chart based on the 'GHI' column
    else:
        st.warning(f"The 'GHI' column does not exist in the {country} dataset.")
