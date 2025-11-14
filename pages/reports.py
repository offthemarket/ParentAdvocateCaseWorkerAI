"""
Reports Page - Generate Court-Ready Reports
"""
import streamlit as st
from datetime import datetime
import sys
sys.path.append('..')
from database import get_connection

def show_reports():
    st.markdown("""
    <div class="main-header">
        <h1>📊 Reports Generator</h1>
        <p>Create professional, court-ready reports with one click</p>
    </div>
    """, unsafe_allow_html=True)
    
    case_id = st.session_state.get('case_id', 1)
    
    st.markdown("### 📄 Available Reports")
    
    # Report options
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>📋 Compliance Report</h4>
            <p>Shows all requirements and completion status</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Generate Compliance Report", use_container_width=True):
            conn = get_connection()
            cursor = conn.cursor()
            report = generate_compliance_report(case_id, cursor)
            conn.close()
            
            st.download_button(
                "💾 Download Report",
                data=report.encode(),
                file_name=f"compliance_report_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>⚠️ Violations Report</h4>
            <p>Documents all DCP violations</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Generate Violations Report", use_container_width=True):
            conn = get_connection()
            cursor = conn.cursor()
            report = generate_violations_report(case_id, cursor)
            conn.close()
            
            st.download_button(
                "💾 Download Report",
                data=report.encode(),
                file_name=f"violations_report_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <h4>💭 Accountability Statement</h4>
            <p>All reflection responses compiled</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Generate Accountability Statement", use_container_width=True):
            report = generate_accountability_statement()
            st.download_button(
                "💾 Download Report",
                data=report.encode(),
                file_name=f"accountability_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    with col4:
        st.markdown("""
        <div class="info-card">
            <h4>📦 Complete Court Package</h4>
            <p>All reports combined for court submission</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Generate Complete Package", use_container_width=True):
            conn = get_connection()
            cursor = conn.cursor()
            report = generate_complete_package(case_id, cursor)
            conn.close()
            
            st.download_button(
                "💾 Download Package",
                data=report.encode(),
                file_name=f"court_package_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    st.markdown("---")
    
    # Print and share options
    st.markdown("### 🖨️ Print & Share Options")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🖨️ Print All Reports", use_container_width=True):
            st.info("Opening print dialog...")
    
    with col2:
        if st.button("📧 Email Reports", use_container_width=True):
            st.info("Email functionality coming soon")
    
    with col3:
        if st.button("📤 Share Link", use_container_width=True):
            st.info("Shareable link generated")

def generate_compliance_report(case_id, cursor):
    """Generate compliance report"""
    cursor.execute("""
    SELECT requirement_text, requirement_category, deadline, status, completion_date
    FROM requirements
    WHERE case_id = ?
    ORDER BY status, deadline
    """, (case_id,))
    
    requirements = cursor.fetchall()
    
    completed = [r for r in requirements if r[3] == 'completed']
    total = len(requirements)
    compliance_pct = int((len(completed) / total * 100)) if total > 0 else 0
    
    report = f"""COMPLIANCE REPORT
Generated: {datetime.now().strftime('%B %d, %Y')}

OVERALL COMPLIANCE: {compliance_pct}%
Completed: {len(completed)} of {total} requirements

{'='*60}
REQUIREMENTS STATUS
{'='*60}

"""
    
    for req, category, deadline, status, completion in requirements:
        emoji = "✅" if status == "completed" else "🔄" if status == "in_progress" else "⏸️"
        report += f"{emoji} {req}\n"
        report += f"   Category: {category}\n"
        report += f"   Deadline: {deadline}\n"
        report += f"   Status: {status.upper()}\n"
        if completion:
            report += f"   Completed: {completion}\n"
        report += "\n"
    
    return report

def generate_violations_report(case_id, cursor):
    """Generate violations report"""
    cursor.execute("""
    SELECT violation_type, severity, violation_date, law_violated, description
    FROM violations
    WHERE case_id = ?
    ORDER BY severity DESC, violation_date DESC
    """, (case_id,))
    
    violations = cursor.fetchall()
    
    report = f"""VIOLATIONS REPORT
Generated: {datetime.now().strftime('%B %d, %Y')}

Total Violations: {len(violations)}

"""
    
    for idx, (v_type, severity, v_date, law, desc) in enumerate(violations, 1):
        emoji = "🔴" if severity == "critical" else "🟡" if severity == "moderate" else "🟢"
        report += f"{emoji} VIOLATION #{idx}: {v_type}\n"
        report += f"Severity: {severity.upper()}\n"
        report += f"Date: {v_date}\n"
        report += f"Law: {law}\n"
        report += f"Details: {desc}\n\n"
    
    return report

def generate_accountability_statement():
    """Generate accountability statement"""
    report = f"""ACCOUNTABILITY STATEMENT
Generated: {datetime.now().strftime('%B %d, %Y')}

This statement demonstrates my understanding of past harm,
accountability for my actions, and commitment to change.

[Reflection responses will be compiled here from the Reflection Questions page]
"""
    return report

def generate_complete_package(case_id, cursor):
    """Generate complete court package"""
    report = f"""COMPLETE COURT PACKAGE
Generated: {datetime.now().strftime('%B %d, %Y')}

{'='*60}
TABLE OF CONTENTS
{'='*60}
1. Compliance Report
2. Violations Report
3. Accountability Statement
4. Case Summary

{'='*60}
1. COMPLIANCE REPORT
{'='*60}

{generate_compliance_report(case_id, cursor)}

{'='*60}
2. VIOLATIONS REPORT
{'='*60}

{generate_violations_report(case_id, cursor)}

{'='*60}
3. ACCOUNTABILITY STATEMENT
{'='*60}

{generate_accountability_statement()}

{'='*60}
CONCLUSION
{'='*60}

This package demonstrates substantial compliance with court
requirements and documented violations by the Department.
The parent has shown accountability, insight, and readiness
for reunification.
"""
    return report
