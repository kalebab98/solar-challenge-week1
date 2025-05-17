import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data(file_paths):
    all_data = []
    for country, path in file_paths.items():
        df = pd.read_csv(path)
        df["Country"] = country
        all_data.append(df)
    return pd.concat(all_data, ignore_index=True)

def plot_boxplot(data, metric):
    fig, ax = plt.subplots()
    sns.boxplot(x="Country", y=metric, data=data, palette="Set2", ax=ax)
    ax.set_title(f"{metric} by Country")
    st.pyplot(fig)
