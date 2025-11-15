import streamlit as st

st.set_page_config(
    page_title="ParentAdvocateAI",
    page_icon="🛡️",
    layout="wide"
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
    }
</style>
""", unsafe_allow_html=True)

# Session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Demo Parent"

# Main app
if not st.session_state.authenticated:
    # Login page
    st.markdown('<div class="main-header"><h1>🛡️ ParentAdvocateAI</h1><p>AI-powered case management for family reunification</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔐 Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.button("Login", use_container_width=True):
            if email == "demo@parent.com" and password == "demo123":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Try: demo@parent.com / demo123")
    
    with col2:
        st.markdown("### 📝 Sign Up")
        st.text_input("Full Name")
        st.text_input("Your Email")
        st.text_input("Your Password", type="password")
        st.button("Create Account", use_container_width=True)

else:
    # Logged in - show app
    with st.sidebar:
        st.markdown("### 🛡️ ParentAdvocateAI")
        st.markdown(f"**{st.session_state.user_name}**")
        st.markdown("---")
        
        page = st.radio("Menu", [
            "🏠 Dashboard",
            "📄 Documents",
            "⚠️ Violations",
            "✅ Compliance",
            "📅 Appointments",
            "👶 Child Updates",
            "💭 Reflections",
            "📊 Reports",
            "💬 AI Chat",
            "👤 Profile"
        ])
        
        st.markdown("---")
        if st.button("🚪 Logout"):
            st.session_state.authenticated = False
            st.rerun()
    
    # Show selected page
    if "Dashboard" in page:
        st.markdown('<div class="main-header"><h1>🏠 Dashboard</h1><p>Welcome back!</p></div>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Days Separated", "45")
        col2.metric("Days to Court", "12")
        col3.metric("Compliance", "82%")
        col4.metric("Violations", "3")
        
        st.success("✅ Clean drug test received!")
        st.info("📌 Next court date: Friday 9am")
        
    elif "Documents" in page:
        st.markdown('<div class="main-header"><h1>�� Documents</h1></div>', unsafe_allow_html=True)
        uploaded = st.file_uploader("Upload document")
        if uploaded:
            st.success("✅ Document uploaded!")
            
    elif "Violations" in page:
        st.markdown('<div class="main-header"><h1>⚠️ Violations Tracker</h1></div>', unsafe_allow_html=True)
        st.metric("Total Violations", "3")
        st.button("Report New Violation")
        
    elif "Compliance" in page:
        st.markdown('<div class="main-header"><h1>✅ Compliance</h1></div>', unsafe_allow_html=True)
        st.progress(0.82)
        st.metric("Completion", "82%")
        
    elif "Appointments" in page:
        st.markdown('<div class="main-header"><h1>📅 Appointments</h1></div>', unsafe_allow_html=True)
        st.info("📌 Drug test tomorrow at 9am")
        
    elif "Child Updates" in page:
        st.markdown('<div class="main-header"><h1>👶 Child Updates</h1></div>', unsafe_allow_html=True)
        st.success("Emma got 100% on her spelling test!")
        
    elif "Reflections" in page:
        st.markdown('<div class="main-header"><h1>💭 Court Reflections</h1></div>', unsafe_allow_html=True)
        st.text_area("Answer reflection questions")
        
    elif "Reports" in page:
        st.markdown('<div class="main-header"><h1>📊 Reports</h1></div>', unsafe_allow_html=True)
        st.button("📥 Download Compliance Report")
        st.button("📥 Download Violations Report")
        
    elif "Chat" in page:
        st.markdown('<div class="main-header"><h1>💬 AI Chat</h1></div>', unsafe_allow_html=True)
        st.text_area("Message the AI")
        st.button("Send")
        
    elif "Profile" in page:
        st.markdown('<div class="main-header"><h1>👤 Profile</h1></div>', unsafe_allow_html=True)
        st.text_input("Name", value=st.session_state.user_name)
        st.button("Save")
