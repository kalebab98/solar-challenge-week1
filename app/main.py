import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

# Set page config
st.set_page_config(page_title="Solar Country Comparison", layout="centered")

# Title
st.title("🔆 Solar Potential Comparison Dashboard")

# File paths (update these with your real paths if needed)
folder = r"C:\Users\Kaleb\OneDrive\Documents\AC\data\data"
file_paths = {
    "Benin": f"{folder}\\benin_clean.csv",
    "Sierra Leone": f"{folder}\\sierraleone_clean.csv",
    "Togo": f"{folder}\\togo_clean.csv",
}

# Load data
data = load_data(file_paths)

# Optional: show columns for debug
if st.checkbox("Show column names"):
    st.write(data.columns.tolist())

# Filter countries
selected_countries = st.multiselect(
    "Select countries to compare:",
    options=data["Country"].unique(),
    default=list(data["Country"].unique())
)

filtered_data = data[data["Country"].isin(selected_countries)]

# Choose metric to visualize
metric = st.selectbox("Choose a solar metric to plot:", ["GHI", "DNI", "DHI"])

# Boxplot
st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots()
sns.boxplot(x="Country", y=metric, data=filtered_data, palette="Set2", ax=ax)
st.pyplot(fig)

# Summary Table
st.subheader(f"{metric} Summary Table")
summary = filtered_data.groupby("Country")[metric].agg(["mean", "median", "std"]).reset_index()
st.dataframe(summary)

# Optional: Average GHI Bar Chart
if metric == "GHI":
    st.subheader("📊 Average GHI by Country")
    ghi_avg = data.groupby("Country")["GHI"].mean().sort_values(ascending=False)
    st.bar_chart(ghi_avg)
