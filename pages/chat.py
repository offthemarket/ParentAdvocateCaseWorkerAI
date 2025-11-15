"""
Private AI Support Chat
"""
import streamlit as st
import anthropic
import os

def show_chat():
    st.markdown("""
    <div class="main-header">
        <h1>💬 AI Support Chat</h1>
        <p>Private, confidential support and guidance</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.warning("🔒 **Private:** This conversation is confidential and NOT shared with DCP")
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat
    for msg in st.session_state.chat_history:
        if msg['role'] == 'user':
            st.markdown(f"""
            <div style="background:#E3F2FD;padding:1rem;border-radius:10px;margin:0.5rem 0;">
                <strong>You:</strong><br>{msg['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background:#F1F8E9;padding:1rem;border-radius:10px;margin:0.5rem 0;">
                <strong>AI:</strong><br>{msg['content']}
            </div>
            """, unsafe_allow_html=True)
    
    # Input
    user_msg = st.text_area("Message", placeholder="I'm here to support you...")
    
    if st.button("Send 💬", use_container_width=True):
        if user_msg.strip():
            st.session_state.chat_history.append({'role': 'user', 'content': user_msg})
            
            api_key = os.environ.get('ANTHROPIC_API_KEY', st.secrets.get('ANTHROPIC_API_KEY', ''))
            if api_key:
                try:
                    client = anthropic.Anthropic(api_key=api_key)
                    messages = [{'role': m['role'], 'content': m['content']} for m in st.session_state.chat_history]
                    
                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1000,
                        system="You are a supportive AI counselor helping parents navigate child protection cases. Be warm, empathetic, and encouraging.",
                        messages=messages
                    )
                    
                    ai_response = response.content[0].text
                    st.session_state.chat_history.append({'role': 'assistant', 'content': ai_response})
                except Exception as e:
                    st.session_state.chat_history.append({'role': 'assistant', 'content': f"Error: {str(e)}"})
            else:
                st.session_state.chat_history.append({'role': 'assistant', 'content': "AI unavailable - configure API key"})
            
            st.rerun()
    
    # Quick topics
    st.markdown("### 💡 Quick Topics")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("😰 I'm overwhelmed", use_container_width=True):
            st.session_state.chat_history.append({'role': 'user', 'content': "I'm feeling overwhelmed. Can you help?"})
            st.rerun()
    with col2:
        if st.button("💪 Need motivation", use_container_width=True):
            st.session_state.chat_history.append({'role': 'user', 'content': "I need motivation. This is hard."})
            st.rerun()
    with col3:
        if st.button("❓ What's next?", use_container_width=True):
            st.session_state.chat_history.append({'role': 'user', 'content': "What should I focus on right now?"})
            st.rerun()
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()
