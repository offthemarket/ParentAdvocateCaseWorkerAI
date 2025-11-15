"""
Violations Tracker - SA Legislation
"""
import streamlit as st
from datetime import datetime
import sys
sys.path.append('..')
from database import get_connection

SA_LAWS = {
    "Section 27": "Investigation before removal required",
    "Section 29": "Kinship placement must be explored first",
    "Section 35": "Case plan must be provided in timeframe",
    "Section 52(3)": "Must facilitate parent-child contact as ordered"
}

def show_violations():
    st.markdown("""
    <div class="main-header">
        <h1>⚠️ DCP Violations Tracker</h1>
        <p>Document violations of SA legislation</p>
    </div>
    """, unsafe_allow_html=True)
    
    conn = get_connection()
    cursor = conn.cursor()
    
    # Stats
    cursor.execute("SELECT COUNT(*), SUM(CASE WHEN severity='critical' THEN 1 ELSE 0 END), SUM(CASE WHEN severity='moderate' THEN 1 ELSE 0 END) FROM violations WHERE case_id=1")
    total, critical, moderate = cursor.fetchone()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Violations", total or 0)
    with col2:
        st.metric("🔴 Critical", critical or 0)
    with col3:
        st.metric("�� Moderate", moderate or 0)
    
    st.markdown("---")
    
    # Generate report
    if st.button("📄 Generate Violations Report", use_container_width=True):
        cursor.execute("SELECT violation_type, severity, violation_date, law_violated, description FROM violations WHERE case_id=1")
        vlist = cursor.fetchall()
        report = f"VIOLATIONS REPORT\nGenerated: {datetime.now().strftime('%B %d, %Y')}\n\nTotal: {len(vlist)}\n\n"
        for idx, (vtype, sev, date, law, desc) in enumerate(vlist, 1):
            report += f"{idx}. {vtype}\nSeverity: {sev}\nDate: {date}\nLaw: {law}\nDetails: {desc}\n\n"
        
        st.download_button("💾 Download Report", report.encode(), f"violations_{datetime.now().strftime('%Y%m%d')}.txt")
    
    st.markdown("---")
    
    # Add violation
    with st.expander("➕ Report New Violation"):
        with st.form("new_v"):
            vtype = st.text_input("Violation Type", placeholder="e.g., Reduced visitation without court order")
            severity = st.selectbox("Severity", ["critical", "moderate", "minor"])
            vdate = st.date_input("Date")
            law = st.selectbox("SA Law Violated", list(SA_LAWS.keys()))
            st.info(SA_LAWS[law])
            desc = st.text_area("Description")
            
            if st.form_submit_button("🚨 Report"):
                cursor.execute("""
                INSERT INTO violations (case_id, violation_type, severity, violation_date, law_violated, description)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (1, vtype, severity, vdate, f"{law} - {SA_LAWS[law]}", desc))
                conn.commit()
                st.success("✅ Reported!")
                st.rerun()
    
    # List violations
    st.markdown("### 📋 Documented Violations")
    cursor.execute("SELECT violation_id, violation_type, severity, violation_date, law_violated FROM violations WHERE case_id=1 ORDER BY violation_date DESC")
    violations = cursor.fetchall()
    
    for vid, vtype, sev, vdate, law in violations:
        emoji = "🔴" if sev == "critical" else "🟡" if sev == "moderate" else "🟢"
        with st.expander(f"{emoji} {vtype} ({vdate})"):
            st.markdown(f"**Law:** {law}")
            if st.button("🗑️ Delete", key=f"dv_{vid}"):
                cursor.execute("DELETE FROM violations WHERE violation_id=?", (vid,))
                conn.commit()
                st.rerun()
    
    conn.close()
