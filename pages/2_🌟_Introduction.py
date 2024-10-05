import streamlit as st
import pandas as pd
import panel as pn
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

# An Introduction Section describing the dataset, its source, and the purpose of your exploration.

st.set_page_config(
    page_title="Le Pard | Introduction",
    page_icon="🌟",
    layout="wide")

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image('assets/dataset_pic.png', width=450)
    st.markdown("<p style='text-align: center; text- color: #EFEFEF;'><i>Source: Saad Haroon (Kaggle)</i></p>", unsafe_allow_html=True)

with col2:
    st.title("HR Analytics Dataset")
    st.markdown("""
<p style='text-align: left; color: #EFEFEF;'>
    This dataset captures various aspects 
    of human resources, such as job roles, monthly income, and tenure within an organization. Its primary focus is to 
    provide insights into factors that influence key HR metrics, such as <i><b>employee performance, job satisfaction, and 
    salary distribution.</i></b> The purpose of this dataset is to predict 
    employee attrition, assess productivity, and identify elements that may affect <i><b>job satisfaction and performance.</i></b>
</p>
""", unsafe_allow_html=True)
    
st.divider()

# Load the dataset (CSV file)
df = pd.read_csv('HR_Analytics.csv')
# XLSX file
excel_file = 'HR_Analytics.xlsx'

sheet_name = '(clean w Outlier)HR_Analytics'  # Replace with the name of the sheet you want to display
df_sheet = pd.read_excel(excel_file, sheet_name=sheet_name)

# Expander
with st.expander("Dataset Snapshots on Excel (Raw Data)"):
    st.subheader("Raw Data")
    st.dataframe(df)
    st.divider()
    st.subheader("Cleaned Data with Outliers")
    st.dataframe(df_sheet)