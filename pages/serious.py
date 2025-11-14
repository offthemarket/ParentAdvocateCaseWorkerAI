"""
SERIOUS Page - Critical Requirements for Reunification
"""
import streamlit as st
import sys
sys.path.append('..')

def show_serious():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF6B6B 0%, #C92A2A 100%); padding: 2rem; border-radius: 10px; color: white; margin-bottom: 2rem;">
        <h1 style="margin:0;">🚨 SERIOUS - What You MUST Do</h1>
        <p style="margin:0.5rem 0 0 0;">Critical requirements for reunification - DO NOT SKIP</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.error("⚠️ **ATTENTION:** These are MANDATORY requirements from your court orders and case plans")
    
    # Critical requirements
    st.markdown("### 🔴 IMMEDIATE ACTION REQUIRED")
    
    st.markdown("""
    <div class="serious-card">
        <h4>1. Complete Drug Testing</h4>
        <strong>What:</strong> Weekly drug testing at approved lab<br>
        <strong>Where:</strong> MedLab, 123 Main St, Adelaide<br>
        <strong>When:</strong> Every Monday by 9am<br>
        <strong>Deadline:</strong> ONGOING - Cannot miss any<br>
        <strong>Why:</strong> Court ordered - missing tests = failure<br>
        <br>
        <button style="background:#C92A2A;color:white;padding:0.5rem 1rem;border:none;border-radius:5px;">📅 Book Next Test</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="serious-card">
        <h4>2. Complete Parenting Program</h4>
        <strong>What:</strong> 10-week parenting course<br>
        <strong>Where:</strong> Online via Alison.com<br>
        <strong>When:</strong> Start immediately<br>
        <strong>Deadline:</strong> Complete by [Court Date]<br>
        <strong>Why:</strong> Required to demonstrate parenting capacity<br>
        <br>
        <button style="background:#C92A2A;color:white;padding:0.5rem 1rem;border:none;border-radius:5px;">🎓 Start Course Now</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="serious-card">
        <h4>3. Secure Stable Housing</h4>
        <strong>What:</strong> Permanent, safe housing approved by DCP<br>
        <strong>Where:</strong> Contact Housing SA<br>
        <strong>When:</strong> ASAP<br>
        <strong>Deadline:</strong> Before child can be returned<br>
        <strong>Why:</strong> Cannot reunify without approved housing<br>
        <br>
        <button style="background:#C92A2A;color:white;padding:0.5rem 1rem;border:none;border-radius:5px;">🏠 Apply for Housing</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Progress tracker
    st.markdown("### 📊 Your Critical Compliance")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Drug Tests", "12/12", "✅ 100%")
    with col2:
        st.metric("Parenting Course", "40%", "⚠️ In Progress")
    with col3:
        st.metric("Housing", "Pending", "🔴 Not Secured")
    
    st.markdown("---")
    
    st.info("💡 **TIP:** Complete these 3 things first - everything else is secondary. These are what the judge cares about MOST.")
    
    # Download action plan
    if st.button("📥 Download Complete Action Plan"):
        action_plan = """CRITICAL ACTION PLAN FOR REUNIFICATION

🚨 PRIORITY 1 - MUST DO IMMEDIATELY:

1. DRUG TESTING
   - What: Weekly testing at approved lab
   - Where: [Lab address]
   - When: Every Monday 9am
   - Status: [ ] Set up
   
2. PARENTING PROGRAM
   - What: Complete 10-week course
   - Where: Alison.com
   - When: Start today
   - Status: [ ] Enrolled
   
3. HOUSING
   - What: Secure stable housing
   - Where: Housing SA application
   - When: ASAP
   - Status: [ ] Applied

DO THESE THREE THINGS FIRST. Everything else can wait.
"""
        st.download_button(
            "💾 Download Action Plan",
            data=action_plan.encode(),
            file_name="critical_action_plan.txt",
            mime="text/plain"
        )
