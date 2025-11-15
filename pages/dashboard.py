"""
Dashboard with Metrics
"""
import streamlit as st
from datetime import datetime, timedelta
import sys
sys.path.append('..')
from database import get_connection

def show_dashboard():
    st.markdown("""
    <div class="main-header">
        <h1>Welcome back, """ + st.session_state.user_name + """</h1>
        <p>Here's your case overview and progress</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📅 Days Separated", "45", delta=None)
    with col2:
        st.metric("⚖️ Days to Court", "12", delta=None)
    with col3:
        st.metric("✅ Compliance", "82%", delta="+5%")
    with col4:
        st.metric("⚠️ DCP Violations", "3", delta=None)
    
    st.markdown("---")
    
    # Children Info
    st.markdown("### 👶 Your Children")
    st.markdown("""
    <div class="info-card">
        <h4>Emma Smith</h4>
        <p><strong>Age:</strong> 3 years old<br>
        <strong>Current Placement:</strong> Foster care</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Urgent Tasks
    st.markdown("### 🚨 Urgent Tasks (Next 7 Days)")
    
    st.markdown("""
    <div class="warning-card">
        <strong>📌 Drug test due tomorrow</strong><br>
        Due: Tomorrow 9am | Status: Scheduled
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-card">
        <strong>📌 Court hearing Friday 9am</strong><br>
        Prepare documents and talking points
    </div>
    """, unsafe_allow_html=True)
    
    # Recent Wins
    st.markdown("### 🎉 This Week's Wins")
    st.markdown("✅ **Attended all therapy sessions** (4/4)")
    st.markdown("✅ **Clean drug test received**")
    st.markdown("✅ **Positive visit feedback**")
    
    # Quick Actions
    st.markdown("### ⚡ Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("📄 Upload Document", use_container_width=True)
    with col2:
        st.button("💬 Chat with AI", use_container_width=True)
    with col3:
        st.button("📊 View Reports", use_container_width=True)
    with col4:
        st.button("⚠️ Check Violations", use_container_width=True)
