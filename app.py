"""
ParentAdvocateAI - Complete Case Management System
"""
import streamlit as st
import os
from datetime import datetime
import sys

st.set_page_config(
    page_title="ParentAdvocateAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #2E86DE;
    }
    .serious-card {
        background: #FFEBEE;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #FF6B6B;
        margin: 1rem 0;
    }
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'user_name' not in st.session_state:
    st.session_state.user_name = None
if 'case_id' not in st.session_state:
    st.session_state.case_id = None

def main():
    if not st.session_state.authenticated:
        show_login_page()
    else:
        show_main_app()

def show_login_page():
    st.markdown("""
    <div class="main-header">
        <h1 style="margin:0;">🛡️ ParentAdvocateAI</h1>
        <p style="margin:0.5rem 0 0 0; opacity:0.9;">
            Your AI-powered case management system for family reunification
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])
    
    with tab1:
        st.markdown("### Welcome Back")
        
        with st.form("login_form"):
            email = st.text_input("📧 Email")
            password = st.text_input("🔒 Password", type="password")
            
            if st.form_submit_button("Login", use_container_width=True):
                if email == "demo@parent.com" and password == "demo123":
                    st.session_state.authenticated = True
                    st.session_state.user_id = 1
                    st.session_state.user_name = "Demo Parent"
                    st.session_state.case_id = 1
                    st.success("✅ Welcome back!")
                    st.rerun()
                else:
                    st.error("❌ Try: demo@parent.com / demo123")
    
    with tab2:
        st.markdown("### Create Your Account")
        
        with st.form("signup_form"):
            st.markdown("#### Your Information")
            col1, col2 = st.columns(2)
            with col1:
                full_name = st.text_input("👤 Full Name *")
                email = st.text_input("📧 Email *")
            with col2:
                password = st.text_input("🔒 Password *", type="password")
                phone = st.text_input("📱 Phone")
            
            st.markdown("---")
            st.markdown("#### Child Information")
            st.info("⚠️ Add your child's details now - this is required!")
            
            child_name = st.text_input("Child's Name *", placeholder="Emma Smith")
            col3, col4 = st.columns(2)
            with col3:
                child_dob = st.date_input("Child's Date of Birth *")
            with col4:
                removal_date = st.date_input("Date of Removal *")
            
            agree = st.checkbox("I agree to Terms of Service")
            
            if st.form_submit_button("Create Account", use_container_width=True):
                if not agree:
                    st.error("❌ You must agree to Terms")
                elif not child_name:
                    st.error("❌ Child's name is required")
                else:
                    st.success("✅ Account created! Log in with: demo@parent.com / demo123")

def show_main_app():
    with st.sidebar:
        st.markdown("### 🛡️ ParentAdvocateAI")
        st.markdown(f"**{st.session_state.user_name}**")
        st.markdown("---")
        
        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "📄 Documents & Analysis",
                "🚨 SERIOUS - What You MUST Do",
                "📚 Training Courses",
                "✅ Compliance Tracker",
                "⚠️ DCP Violations",
                "📅 Appointments",
                "👶 Child Updates",
                "💭 Court Reflections",
                "📊 Court Reports",
                "💬 Private AI Chat",
                "👤 Profile"
            ]
        )
        
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()
    
    # Route to pages
    if page == "🏠 Dashboard":
        from pages import dashboard
        dashboard.show_dashboard()
    elif page == "📄 Documents & Analysis":
        from pages import documents
        documents.show_documents()
    elif page == "🚨 SERIOUS - What You MUST Do":
        from pages import serious
        serious.show_serious()
    elif page == "📚 Training Courses":
        from pages import courses
        courses.show_courses()
    elif page == "✅ Compliance Tracker":
        from pages import compliance
        compliance.show_compliance()
    elif page == "⚠️ DCP Violations":
        from pages import violations
        violations.show_violations()
    elif page == "📅 Appointments":
        from pages import appointments
        appointments.show_appointments()
    elif page == "👶 Child Updates":
        from pages import child_updates
        child_updates.show_child_updates()
    elif page == "💭 Court Reflections":
        from pages import reflection
        reflection.show_reflection()
    elif page == "📊 Court Reports":
        from pages import reports
        reports.show_reports()
    elif page == "💬 Private AI Chat":
        from pages import chat
        chat.show_chat()
    elif page == "👤 Profile":
        from pages import profile
        profile.show_profile()

if __name__ == "__main__":
    main()
