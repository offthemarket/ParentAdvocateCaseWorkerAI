import streamlit as st

def show_violations():
    st.markdown('<div class="main-header"><h1>⚠️ Violations Tracker</h1></div>', unsafe_allow_html=True)
    st.info("📋 Document DCP violations of SA legislation")
