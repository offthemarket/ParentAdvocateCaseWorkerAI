"""
Child Updates Feed
"""
import streamlit as st
from datetime import datetime, timedelta

def show_child_updates():
    st.markdown("""
    <div class="main-header">
        <h1>👶 Child Updates</h1>
        <p>Stay connected with your child's progress</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("🔒 Updates posted by DCP caseworkers and foster parents")
    
    st.markdown("### 📬 Recent Updates")
    
    # Sample updates
    updates = [
        {
            "emoji": "📚",
            "title": "School Achievement",
            "text": "Emma got 100% on her spelling test! She's been working really hard.",
            "date": "2 days ago",
            "author": "Foster Parent"
        },
        {
            "emoji": "🏥",
            "title": "Health Checkup",
            "text": "Well-child checkup completed. Emma is healthy and growing well!",
            "date": "1 week ago",
            "author": "DCP Caseworker"
        },
        {
            "emoji": "🎨",
            "title": "Art Project",
            "text": "Emma drew a beautiful picture of flowers. She said it's for you!",
            "date": "1 week ago",
            "author": "Foster Parent"
        },
        {
            "emoji": "��",
            "title": "Milestone",
            "text": "Emma rode her bike without training wheels for the first time!",
            "date": "2 weeks ago",
            "author": "Foster Parent"
        }
    ]
    
    for update in updates:
        st.markdown(f"""
        <div class="info-card">
            <h4>{update['emoji']} {update['title']}</h4>
            <p>{update['text']}</p>
            <small><em>Posted by {update['author']} • {update['date']}</em></small>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.success("✅ DCP caseworkers can post updates to keep you connected with your child's life")
    
    # Request update
    st.markdown("### 💬 Request an Update")
    with st.form("request_update"):
        question = st.text_area("What would you like to know?", placeholder="How is Emma doing in school?")
        if st.form_submit_button("📤 Send Request to Caseworker"):
            st.success("✅ Request sent! You'll receive an update within 48 hours.")
