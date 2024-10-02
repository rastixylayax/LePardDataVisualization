import streamlit as st

# An Introduction Section describing the dataset, its source, and the purpose of your exploration.

st.set_page_config(
    page_title="Page 2",
    page_icon=":woman_and_man_holding_hands:",
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

# Expander
with st.expander("Dataset Snapshots on Excel (Raw Data)"):
    st.image('assets/dataset_excel_pic.png', width=950)
    st.divider()
    st.image('assets/dataset_excel_pic2.png', width=950)