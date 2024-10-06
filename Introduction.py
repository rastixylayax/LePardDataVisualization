import streamlit as st
import pandas as pd
import panel as pn
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pathlib as Path

# An Introduction Section describing the dataset, its source, and the purpose of your exploration.

def app():
    # --- LOAD CSS ---
    current_dir = Path.Path(__file__).parent if "__file__" in locals() else Path.Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    # Hero Section
    col1, col2 = st.columns([1,1.4], gap="large")
    with col1:
        st.image('assets/HR.png', width=400)
        

    with col2:
        st.markdown("""<h1><span style='color: #fff;'>HR Analytics</span> Dataset</h1>""", unsafe_allow_html=True)
        st.markdown("""
        <p style='text-align: left; font-size: 16px; '>
            This dataset captures various aspects 
            of human resources, such as job roles, monthly income, and tenure within an organization. Its primary focus is to 
            provide insights into factors that influence key HR metrics, such as <span ><b>employee performance, job satisfaction, and 
            salary distribution.</b></span> The purpose of this dataset is to predict 
            employee attrition, assess productivity, and identify elements that may affect <span > <b>job satisfaction and performance.</b> </span>
        </p>
        """, unsafe_allow_html=True)

        with st.container():
            # Markdown link with hover class
            st.markdown('<a href="https://www.kaggle.com/datasets/saadharoon27/hr-analytics-dataset" class="hover-link" ><i style="color: #eb5e28">🔗 Source: Saad Haroon (Kaggle)</i></a>', unsafe_allow_html=True)
        
    st.divider() 

    

    # Load the dataset (CSV file)
    df = pd.read_csv('HR_Analytics.csv')
    # XLSX file
    excel_file = 'HR_Analytics.xlsx'

    sheet_name = '(clean w Outlier)HR_Analytics'  # Replace with the name of the sheet you want to display
    df_sheet = pd.read_excel(excel_file, sheet_name=sheet_name)

    st.markdown(
        """
        <h2 style='color: #fff; padding-top:0px; margin-top: 0px;'><i class='bi bi-clipboard-data' style='color: #eb5e28; font-size: 30px;'></i> Dataset Overview</h2>"""
        , unsafe_allow_html=True
        )
    
    # Create a container for the Dataset Overview
    with st.container():
        # Dropdown menu for Dataset Overview
        data_option = st.selectbox(
            "Select Data View:",
            options=["Raw Data", "Cleaned Data with Outliers"]
        )

        if data_option == "Raw Data":
            st.subheader("Raw Data")
            st.dataframe(df)
        elif data_option == "Cleaned Data with Outliers":
            st.subheader("Cleaned Data with Outliers")
            st.dataframe(df_sheet)