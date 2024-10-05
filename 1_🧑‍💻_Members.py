import streamlit as st

st.set_page_config(
    page_title="Le Pard",
    page_icon="📚",
    layout="wide")

st.markdown("<h1 style='text-align: center;'>Team Le Pard</h1>", unsafe_allow_html=True)

# Hero Section
col1, col2, col3, col4, col5 = st.columns(5, gap="small")

with col1:
    st.image("assets/shin_pic.png", width=190)
    st.markdown("<p style='text-align: center;'>Shania Canoy</p>", unsafe_allow_html=True)

with col2:
    st.image("assets/arj_pic.png", width=190)
    st.markdown("<p style='text-align: center;'>Rustico John Ylaya</p>", unsafe_allow_html=True)

with col3:
    st.image("assets/rynze_pic.png", width=190)
    st.markdown("<p style='text-align: center;'>Keath Ian Lavador</p>", unsafe_allow_html=True)

with col4:
    st.image("assets/ket_pic.png", width=190)
    st.markdown("<p style='text-align: center;'>Joshua Briones</p>", unsafe_allow_html=True)

with col5:
    st.image("assets/josh_pic.png", width=190)
    st.markdown("<p style='text-align: center;'>Rynze RJ Lozano</p>", unsafe_allow_html=True)

st.divider()

code = '''def hello():
    print("Hello, everyone!")
    print("We are Team Le Pard!")
    print("Let's explore our team's data exploration project!")'''
st.code(code, language="python")

# streamlit run 1_🧑‍💻_Members.py
# 2_🌟_Introduction
# 3_📈_Data Visualization
# 4_📜_Conclusion
