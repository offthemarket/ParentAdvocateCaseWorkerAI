"""
Court Reports Generator
"""
import streamlit as st
from datetime import datetime
import sys
sys.path.append('..')
from database import get_connection

def show_reports():
    st.markdown("""
    <div class="main-header">
        <h1>📊 Court Reports Generator</h1>
        <p>Create professional, court-ready reports</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### �� Available Reports")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>📋 Compliance Report</h4>
            <p>Shows all requirements and completion status</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Generate Compliance Report", use_container_width=True):
            report = generate_compliance_report()
            st.download_button("💾 Download", report.encode(), f"compliance_{datetime.now().strftime('%Y%m%d')}.txt", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>⚠️ Violations Report</h4>
            <p>Documents all DCP violations</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Generate Violations Report", use_container_width=True):
            report = generate_violations_report()
            st.download_button("💾 Download", report.encode(), f"violations_{datetime.now().strftime('%Y%m%d')}.txt", use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <h4>💭 Accountability Statement</h4>
            <p>Reflection responses compiled</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Generate Accountability", use_container_width=True):
            report = "ACCOUNTABILITY STATEMENT\n\nReflection responses will be compiled here."
            st.download_button("💾 Download", report.encode(), f"accountability_{datetime.now().strftime('%Y%m%d')}.txt", use_container_width=True)
    
    with col4:
        st.markdown("""
        <div class="info-card">
            <h4>📦 Complete Court Package</h4>
            <p>All reports combined</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Generate Complete Package", use_container_width=True):
            report = generate_complete_package()
            st.download_button("💾 Download", report.encode(), f"court_package_{datetime.now().strftime('%Y%m%d')}.txt", use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("### 🖨️ Print & Share")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🖨️ Print All", use_container_width=True)
    with col2:
        st.button("📧 Email Reports", use_container_width=True)
    with col3:
        st.button("📤 Share Link", use_container_width=True)

def generate_compliance_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT requirement_text, status, deadline FROM requirements WHERE case_id=1")
    reqs = cursor.fetchall()
    conn.close()
    
    report = f"COMPLIANCE REPORT\nGenerated: {datetime.now().strftime('%B %d, %Y')}\n\n"
    for req, status, deadline in reqs:
        report += f"• {req}\n  Status: {status} | Deadline: {deadline}\n\n"
    return report

def generate_violations_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT violation_type, severity, violation_date, law_violated FROM violations WHERE case_id=1")
    vios = cursor.fetchall()
    conn.close()
    
    report = f"VIOLATIONS REPORT\nGenerated: {datetime.now().strftime('%B %d, %Y')}\n\n"
    for vtype, sev, date, law in vios:
        report += f"• {vtype}\n  Severity: {sev} | Date: {date}\n  Law: {law}\n\n"
    return report

def generate_complete_package():
    return f"""COMPLETE COURT PACKAGE
Generated: {datetime.now().strftime('%B %d, %Y')}

{'='*60}
1. COMPLIANCE REPORT
{'='*60}

{generate_compliance_report()}

{'='*60}
2. VIOLATIONS REPORT
{'='*60}

{generate_violations_report()}

{'='*60}
CONCLUSION
{'='*60}

This package demonstrates compliance and documented DCP violations.
Parent has shown accountability and readiness for reunification.
"""
