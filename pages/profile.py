"""
Profile Management
"""
import streamlit as st

def show_profile():
    st.markdown("""
    <div class="main-header">
        <h1>👤 Your Profile</h1>
        <p>Manage your account information</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📋 Personal Information")
    
    with st.form("profile"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", value=st.session_state.user_name)
            email = st.text_input("Email", value="demo@parent.com", disabled=True)
            phone = st.text_input("Phone")
        with col2:
            new_pw = st.text_input("New Password (optional)", type="password")
            confirm_pw = st.text_input("Confirm Password", type="password")
        
        if st.form_submit_button("💾 Save Changes", use_container_width=True):
            if new_pw and new_pw != confirm_pw:
                st.error("Passwords don't match")
            else:
                st.success("✅ Profile updated!")
    
    st.markdown("---")
    
    st.markdown("### 🏥 Additional Information")
    st.info("Store Medicare, Centrelink info for faster appointment booking")
    
    with st.form("additional"):
        medicare = st.text_input("Medicare Number")
        crn = st.text_input("Centrelink CRN")
        gp = st.text_input("Regular GP")
        emergency = st.text_input("Emergency Contact")
        
        if st.form_submit_button("💾 Save", use_container_width=True):
            st.success("✅ Information saved!")
