"""
Dashboard Page
"""
import streamlit as st

def show_dashboard():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 10px; color: white; margin-bottom: 2rem;">
        <h1>🏠 Dashboard</h1>
        <p>Welcome to ParentAdvocateAI</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Cases", "0")
    with col2:
        st.metric("Compliance", "0%")
    with col3:
        st.metric("Violations", "0")
    
    st.success("✅ Dashboard loaded successfully!")
    st.info("📝 Full features will be added soon")

if __name__ == "__main__":
    show_dashboard()
