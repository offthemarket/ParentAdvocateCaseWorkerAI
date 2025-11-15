"""
Appointments Manager
"""
import streamlit as st
from datetime import datetime

def show_appointments():
    st.markdown("""
    <div class="main-header">
        <h1>📅 Appointments Manager</h1>
        <p>Track and manage all your appointments</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📝 AI can book appointments with DASSA, PsychMed, Sonder, Housing SA")
    
    # Quick booking
    st.markdown("### 🤖 AI Quick Booking")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏥 Book DASSA Appointment", use_container_width=True):
            st.success("Searching available slots at DASSA...")
    with col2:
        if st.button("🧠 Book PsychMed", use_container_width=True):
            st.success("Searching PsychMed availability...")
    with col3:
        if st.button("🏠 Book Housing SA", use_container_width=True):
            st.success("Searching Housing SA slots...")
    
    st.markdown("---")
    
    # Manual add
    st.markdown("### 📋 Your Appointments")
    
    with st.form("add_appt"):
        col1, col2 = st.columns(2)
        with col1:
            appt_type = st.selectbox("Type", ["Drug Test", "Therapy", "Court Hearing", "DCP Meeting", "Parenting Class"])
            provider = st.text_input("Provider/Location")
        with col2:
            appt_date = st.date_input("Date")
            appt_time = st.time_input("Time")
        
        if st.form_submit_button("📅 Add Appointment"):
            st.success(f"✅ {appt_type} scheduled for {appt_date} at {appt_time}")
    
    # Upcoming appointments
    st.markdown("### 📆 Upcoming")
    
    st.markdown("""
    <div class="info-card">
        <strong>💉 Drug Test</strong><br>
        Tomorrow at 9:00 AM<br>
        MedLab, 123 Main St, Adelaide<br>
        <button style="background:#2E86DE;color:white;padding:0.3rem 1rem;border:none;border-radius:5px;">📍 Get Directions</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <strong>⚖️ Court Hearing</strong><br>
        Friday at 9:00 AM<br>
        Adelaide Magistrates Court<br>
        <button style="background:#2E86DE;color:white;padding:0.3rem 1rem;border:none;border-radius:5px;">📄 Prepare Documents</button>
    </div>
    """, unsafe_allow_html=True)
