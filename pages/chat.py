"""
AI Chat Page - Private counseling and support
"""
import streamlit as st
import sys
sys.path.append('..')
import anthropic
import os

def show_chat():
    st.markdown("""
    <div class="main-header">
        <h1>💬 AI Support Chat</h1>
        <p>Private, confidential support and guidance</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.warning("�� **Private**: This conversation is confidential and NOT shared with DCP")
    
    # Initialize chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f"""
            <div style="background:#E3F2FD;padding:1rem;border-radius:10px;margin:0.5rem 0;">
                <strong>You:</strong><br>{message['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background:#F1F8E9;padding:1rem;border-radius:10px;margin:0.5rem 0;">
                <strong>AI Support:</strong><br>{message['content']}
            </div>
            """, unsafe_allow_html=True)
    
    # Chat input
    user_message = st.text_area(
        "Message",
        placeholder="Ask me anything - I'm here to support you...",
        key="chat_input"
    )
    
    if st.button("Send ��", use_container_width=True):
        if user_message.strip():
            # Add user message to history
            st.session_state.chat_history.append({
                'role': 'user',
                'content': user_message
            })
            
            # Get AI response
            api_key = os.environ.get('ANTHROPIC_API_KEY', st.secrets.get('ANTHROPIC_API_KEY', ''))
            
            if api_key:
                try:
                    client = anthropic.Anthropic(api_key=api_key)
                    
                    # Build messages for API
                    messages = [{'role': msg['role'], 'content': msg['content']} 
                               for msg in st.session_state.chat_history]
                    
                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1000,
                        system="""You are a supportive, empathetic AI counselor helping parents navigate child protection cases. Provide:
- Emotional support and encouragement
- Practical guidance
- Understanding and empathy
- Motivation to keep going
- Reminder of their child's needs
Be warm, professional, and genuinely caring.""",
                        messages=messages
                    )
                    
                    ai_response = response.content[0].text
                    
                    # Add AI response to history
                    st.session_state.chat_history.append({
                        'role': 'assistant',
                        'content': ai_response
                    })
                    
                except Exception as e:
                    ai_response = f"I'm having trouble connecting right now: {str(e)}"
                    st.session_state.chat_history.append({
                        'role': 'assistant',
                        'content': ai_response
                    })
            else:
                st.error("AI chat unavailable - API key not configured")
            
            st.rerun()
    
    # Quick topics
    st.markdown("### 💡 Quick Topics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("😰 I'm feeling overwhelmed", use_container_width=True):
            st.session_state.chat_history.append({
                'role': 'user',
                'content': "I'm feeling really overwhelmed right now. Can you help?"
            })
            st.rerun()
    
    with col2:
        if st.button("💪 I need motivation", use_container_width=True):
            st.session_state.chat_history.append({
                'role': 'user',
                'content': "I need some motivation to keep going. This is so hard."
            })
            st.rerun()
    
    with col3:
        if st.button("❓ What should I do next?", use_container_width=True):
            st.session_state.chat_history.append({
                'role': 'user',
                'content': "What's the most important thing I should focus on right now?"
            })
            st.rerun()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()
