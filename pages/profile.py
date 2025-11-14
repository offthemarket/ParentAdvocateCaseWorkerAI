"""
Profile Page - User information
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
    
    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", value=st.session_state.get('user_name', 'Demo Parent'))
            email = st.text_input("Email", value="demo@parent.com", disabled=True)
            phone = st.text_input("Phone")
        
        with col2:
            new_password = st.text_input("New Password (leave blank to keep current)", type="password")
            confirm_password = st.text_input("Confirm New Password", type="password")
        
        submit = st.form_submit_button("💾 Save Changes", use_container_width=True)
        
        if submit:
            if new_password and new_password != confirm_password:
                st.error("Passwords don't match")
            else:
                st.success("✅ Profile updated!")
    
    st.markdown("---")
    
    # Additional info for parents
    st.markdown("### 🏥 Additional Information")
    st.info("Store your Medicare, Centrelink, and GP information for faster appointment booking")
    
    with st.form("additional_info"):
        medicare = st.text_input("Medicare Number")
        crn = st.text_input("Centrelink CRN")
        gp = st.text_input("Regular GP")
        emergency = st.text_input("Emergency Contact")
        
        if st.form_submit_button("💾 Save", use_container_width=True):
            st.success("✅ Information saved!")
