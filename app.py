"""
ParentAdvocateAI - Complete Case Management System
"""
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="ParentAdvocateAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Styling
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
    .success-card {
        background: #E8F8F5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #26DE81;
    }
    .warning-card {
        background: #FFF3E0;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #FF6B6B;
    }
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #26DE81 0%, #2E86DE 100%);
    }
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #2E86DE;
    }
</style>
""", unsafe_allow_html=True)

# Session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = None
if 'case_id' not in st.session_state:
    st.session_state.case_id = 1

def main():
    if not st.session_state.authenticated:
        show_auth_page()
    else:
        show_app()

def show_auth_page():
    st.markdown("""
    <div class="main-header">
        <h1>🛡️ ParentAdvocateAI</h1>
        <p>AI-powered case management for family reunification</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])
    
    with tab1:
        st.markdown("### Welcome Back")
        with st.form("login"):
            email = st.text_input("📧 Email")
            password = st.text_input("🔒 Password", type="password")
            if st.form_submit_button("Login", use_container_width=True):
                if email == "demo@parent.com" and password == "demo123":
                    st.session_state.authenticated = True
                    st.session_state.user_name = "Demo Parent"
                    st.success("✅ Welcome!")
                    st.rerun()
                else:
                    st.error("Try: demo@parent.com / demo123")
    
    with tab2:
        st.markdown("### Create Account")
        with st.form("signup"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("👤 Full Name *")
                email = st.text_input("📧 Email *")
            with col2:
                password = st.text_input("🔒 Password *", type="password")
                phone = st.text_input("📱 Phone")
            
            st.markdown("---")
            st.markdown("#### Child Information")
            child_name = st.text_input("Child's Name *")
            col3, col4 = st.columns(2)
            with col3:
                child_dob = st.date_input("Date of Birth *")
            with col4:
                removal_date = st.date_input("Removal Date *")
            
            agree = st.checkbox("I agree to Terms")
            
            if st.form_submit_button("Create Account", use_container_width=True):
                if agree and child_name:
                    st.success("✅ Account created! Login with demo@parent.com / demo123")
                else:
                    st.error("Please complete all fields")

def show_app():
    with st.sidebar:
        st.markdown("### 🛡️ ParentAdvocateAI")
        st.markdown(f"**{st.session_state.user_name}**")
        st.markdown("---")
        
        page = st.radio("Navigation", [
            "🏠 Dashboard",
            "📄 Documents & Analysis",
            "⚠️ Violations Tracker",
            "✅ Compliance Progress",
            "📅 Appointments",
            "👶 Child Updates",
            "💭 Court Reflections",
            "📊 Court Reports",
            "💬 Private AI Chat",
            "👤 Profile"
        ])
        
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()
    
    if page == "�� Dashboard":
        from pages import dashboard
        dashboard.show_dashboard()
    elif page == "📄 Documents & Analysis":
        from pages import documents
        documents.show_documents()
    elif page == "⚠️ Violations Tracker":
        from pages import violations
        violations.show_violations()
    elif page == "✅ Compliance Progress":
        from pages import compliance
        compliance.show_compliance()
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
