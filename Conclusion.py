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

    with col1:
        st.metric("Most Common Age Range", "30-40 years")
    with col2:
        st.metric("Most Frequent Job Level", "1 (Entry Level)")
    with col3:    
        st.metric("Salary Range", "$2,000-$10,000")

    st.markdown("""<style> [data-testid="stMetricValue"] {font-size: 20px;} </style>""", unsafe_allow_html=True)

    fig = go.Figure()

    hist = go.Histogram(x=df['Age'], nbinsx=30, name='Age')
    fig.add_trace(hist)

    fig.update_layout(
        title_text='Histogram of Age within HR Analytics dataset',
        showlegend=False, 
        height=400,  
        width=700, 
    )
    st.plotly_chart(fig)

