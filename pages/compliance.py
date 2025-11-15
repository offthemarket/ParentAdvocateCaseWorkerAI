"""
Compliance Tracker with Progress Bars
"""
import streamlit as st
import sys
sys.path.append('..')
from database import get_connection

def show_compliance():
    st.markdown("""
    <div class="main-header">
        <h1>✅ Compliance Tracker</h1>
        <p>Track progress toward reunification</p>
    </div>
    """, unsafe_allow_html=True)
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*), SUM(CASE WHEN status='completed' THEN 1 ELSE 0 END) FROM requirements WHERE case_id=1")
    total, completed = cursor.fetchone()
    
    compliance = int((completed / total * 100)) if total else 0
    
    st.markdown(f"### Overall Completion: {compliance}%")
    st.progress(compliance / 100)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Requirements", total or 0)
    with col2:
        st.metric("✅ Completed", completed or 0)
    
    st.markdown("---")
    
    # Add requirement
    with st.expander("➕ Add Requirement"):
        with st.form("new_req"):
            req = st.text_input("Requirement")
            cat = st.selectbox("Category", ["Housing", "Employment", "Therapy", "Drug Testing", "Parenting Class"])
            deadline = st.date_input("Deadline")
            
            if st.form_submit_button("Add"):
                cursor.execute("INSERT INTO requirements (case_id, requirement_text, category, deadline) VALUES (?, ?, ?, ?)", (1, req, cat, deadline))
                conn.commit()
                st.success("✅ Added!")
                st.rerun()
    
    # List requirements
    cursor.execute("SELECT requirement_id, requirement_text, category, deadline, status FROM requirements WHERE case_id=1")
    reqs = cursor.fetchall()
    
    for rid, text, cat, deadline, status in reqs:
        with st.expander(f"{text} ({cat})"):
            st.markdown(f"**Deadline:** {deadline}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Mark Complete", key=f"c_{rid}"):
                    cursor.execute("UPDATE requirements SET status='completed', completion_date=date('now') WHERE requirement_id=?", (rid,))
                    conn.commit()
                    st.rerun()
            with col2:
                if st.button("🗑️ Delete", key=f"d_{rid}"):
                    cursor.execute("DELETE FROM requirements WHERE requirement_id=?", (rid,))
                    conn.commit()
                    st.rerun()
    
    conn.close()
