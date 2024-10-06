from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu


def app():
    # --- LOAD CSS ---
    
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Meet <span style='color: #eb5e28'>The Team</span></h1>", unsafe_allow_html=True)

    st.divider()

    # Hero Section
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

    with col1:
        st.image("assets/shin_pic.png", width=190)
        st.markdown("<p style='text-align: center; width: 190px;'>Shania Canoy</p>", unsafe_allow_html=True)

    with col2:
        st.image("assets/arj_pic.png", width=190)
        st.markdown("<p style='text-align: center;width: 190px;'>Rustico John Ylaya</p>", unsafe_allow_html=True)

    with col3:
        st.image("assets/rynze_pic.png", width=190)
        st.markdown("<p style='text-align: center;width: 190px;'>Keath Ian Lavador</p>", unsafe_allow_html=True)

    with col4:
        st.image("assets/ket_pic.png", width=190)
        st.markdown("<p style='text-align: center;width: 190px;'>Joshua Briones</p>", unsafe_allow_html=True)

    with col5:
        st.image("assets/josh_pic.png", width=190)
        st.markdown("<p style='text-align: center;width: 190px;'>Rynze RJ Lozano</p>", unsafe_allow_html=True)

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
# Run the app
if __name__ == "__main__":
    app()