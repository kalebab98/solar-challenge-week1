import pandas as pd
import os
import tempfile
import streamlit as st

def load_data(uploaded_files):
    """
    Load data from the given uploaded files.

    Args:
    uploaded_files (list): List of uploaded file-like objects from Streamlit file_uploader.

    Returns:
    pd.DataFrame: A DataFrame containing the merged data from all the files.
    """
    data_frames = []
    
    # Handle each uploaded file
    for uploaded_file in uploaded_files:
        try:
            # Create a temporary file to save the uploaded file content
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.getbuffer())  # Write the content to the temp file
                tmp_file_path = tmp_file.name  # Get the path of the temp file
            
            # Read the file into a DataFrame
            df = pd.read_csv(tmp_file_path)
            data_frames.append(df)
        
        except Exception as e:
            # Catch any errors and display them to the user
            st.error(f"Error processing file {uploaded_file.name}: {e}")
            continue  # Skip to the next file if there was an error

    # Concatenate all the DataFrames
    if data_frames:
        combined_data = pd.concat(data_frames, ignore_index=True)
        return combined_data
    else:
        st.warning("No data was loaded. Please check the uploaded files.")
        return pd.DataFrame()  # Return an empty DataFrame if no files were loaded
