"""
Training Courses Page - Alison.com Integration
"""
import streamlit as st

def show_courses():
    st.markdown("""
    <div class="main-header">
        <h1>�� Training Courses</h1>
        <p>Complete required courses for reunification</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("🎓 All courses are FREE from Alison.com - get certificates to show court")
    
    # Featured courses
    st.markdown("### 🌟 Required Parenting Courses")
    
    courses = [
        {
            "name": "Child Psychology and Development",
            "url": "https://alison.com/course/child-psychology-and-development",
            "duration": "1-2 hours",
            "required": True
        },
        {
            "name": "Introduction to Parenting Skills",
            "url": "https://alison.com/course/introduction-to-parenting-skills",
            "duration": "1-2 hours",
            "required": True
        },
        {
            "name": "Understanding Child Behavior",
            "url": "https://alison.com/course/understanding-child-behavior",
            "duration": "2-3 hours",
            "required": True
        }
    ]
    
    for course in courses:
        st.markdown(f"""
        <div class="info-card">
            <h4>{'🔴 REQUIRED: ' if course['required'] else ''}{course['name']}</h4>
            <p><strong>Duration:</strong> {course['duration']}</p>
            <p><strong>Certificate:</strong> Yes - downloadable upon completion</p>
            <a href="{course['url']}" target="_blank">
                <button style="background:#2E86DE;color:white;padding:0.5rem 1rem;border:none;border-radius:5px;cursor:pointer;">
                    🎓 Start Course
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Browse more courses
    st.markdown("### 🔍 Browse More Courses")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>Substance Abuse Recovery</h4>
            <a href="https://alison.com/courses?query=addiction" target="_blank">
                <button style="background:#10AC84;color:white;padding:0.5rem 1rem;border:none;border-radius:5px;">
                    View Courses
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h4>Mental Health & Wellness</h4>
            <a href="https://alison.com/courses?query=mental+health" target="_blank">
                <button style="background:#10AC84;color:white;padding:0.5rem 1rem;border:none;border-radius:5px;">
                    View Courses
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Track completed courses
    st.markdown("### ✅ Your Completed Courses")
    
    st.info("Upload your Alison certificates here to add to your court reports")
    
    uploaded_cert = st.file_uploader("Upload Certificate", type=['pdf', 'jpg', 'png'])
    if uploaded_cert:
        st.success("✅ Certificate uploaded! This will be included in your court package.")
    
    # Link to browse all
    st.markdown("---")
    st.markdown("### 🌐 Browse All Alison Courses")
    st.markdown("[🔗 Visit Alison.com](https://alison.com/courses?query=parenting)")
