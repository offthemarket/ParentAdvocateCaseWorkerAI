import streamlit as st

def show_appointments():
    st.markdown('<div class="main-header"><h1>📅 Appointments</h1></div>', unsafe_allow_html=True)
    st.info("📝 Appointment management system")
    st.success("✅ AI can book appointments with DASSA, PsychMed, Sonder, Housing SA")
