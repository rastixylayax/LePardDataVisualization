import streamlit as st
from streamlit_option_menu import option_menu
import Members
import Overview
import Data_Exploration
import Data_Analysis
import Conclusion
import pathlib as Path

st.set_page_config(page_title='Le Pard | HR Analytics', page_icon='📊', layout='wide')

# Sidebar menu for navigation
with st.sidebar:
    # --- LOAD CSS ---
    current_dir = Path.Path(__file__).parent if "__file__" in locals() else Path.Path.cwd()
    css_file = current_dir / "styles" / "main.css"

    st.image("assets/Le Pard.svg", width=280)

    st.divider()

    selected = option_menu(
        menu_title=None,
        options=["Members", "Overview", "Data Exploration","Data Analysis", "Conclusion"],
        icons=["bi-people", "bi-card-text", "bi-bar-chart-line","bi-graph-up", "bi-chat-left-quote"],
        default_index=0,
    )

    st.divider()
    st.markdown(
        """
        <p style='text-align: center; font-size: 14px; color: #797776'>
            <span>&copy; 2024 Team Le Pard | CIT-U </span>
            <a href=")
        </p>
        """, unsafe_allow_html=True
    )



    


# Load the appropriate page based on the selection
if selected == "Members":
    Members.app()
elif selected == "Overview":
    Overview.app()
elif selected == "Data Exploration":
    Data_Exploration.app()
elif selected == "Data Analysis":
    Data_Analysis.app()
elif selected == "Conclusion":
    Conclusion.app()
