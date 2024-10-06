# A Conclusion Section summarizing the general insights and takeaways from your exploration.

import streamlit as st
import pandas as pd
import panel as pn
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pathlib as Path

# st.set_page_config(
#     page_title="Le Pard | Conclusion",
#     page_icon="📜",
#     layout="centered")
def app():
    # --- LOAD CSS ---
    current_dir = Path.Path(__file__).parent if "__file__" in locals() else Path.Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
        
    # Load the dataset
    df = pd.read_csv('HR_Analytics.csv')

    # Key metrics
    col1, col2, col3 = st.columns(3)

    # Include Bootstrap Icons CSS
    st.markdown("""
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
    """, unsafe_allow_html=True)

    # Create a container with a Bootstrap icon
    with col1:
        with st.container(border=True):
            coll1, coll2 = st.columns([0.8, 3]) 
            with coll1:
                st.markdown("<div style='text-align: center;'><i class='bi bi-people' style='color: #eb5e28; font-size: 38px;'></i></div>", unsafe_allow_html=True)  # Center the icon
            with coll2:
                st.metric("Most Common Age Range", "30-40 years")
    with col2:
        with st.container(border=True):
            coll1, coll2 = st.columns([0.8, 3]) 
            with coll1:
                st.markdown("<div style='text-align: center;'><i class='bi bi-graph-up' style='color: #eb5e28; font-size: 38px;'></i></div>", unsafe_allow_html=True)  # Center the icon
            with coll2:
                st.metric("Most Frequent Job Level", "1 (Entry Level)")
    with col3:    
        with st.container(border=True):
            coll1, coll2 = st.columns([0.8, 3]) 
            with coll1:
                st.markdown("<div style='text-align: center;'><i class='bi bi-cash-coin' style='color: #eb5e28; font-size: 38px;'></i></div>", unsafe_allow_html=True)  # Center the icon
            with coll2:
                st.metric("Salary Range", "$2,000-$10,000")

    st.markdown("""<style> [data-testid="stMetricValue"] {font-size: 20px;} </style>""", unsafe_allow_html=True)

    # Create a figure for the histogram
    fig = go.Figure()

    # Create the histogram with the specified color
    hist = go.Histogram(
        x=df['Age'], 
        nbinsx=30, 
        name='Age',
        marker_color='#E67644'  # Set the color of the histogram bars
    )
    fig.add_trace(hist)

    # Update the layout of the figure
    fig.update_layout(
        title_text='Histogram of Age within HR Analytics dataset',
        showlegend=False, 
        height=500,  
        width=1000, 
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig)
