"""
Private AI Support Chat - WORKING VERSION
"""
import streamlit as st
import os

def show_chat():
    st.markdown("""
    <div class="main-header">
        <h1>�� AI Support Chat</h1>
        <p>Private, confidential support and guidance</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.warning("🔒 **Private:** This conversation is confidential and NOT shared with DCP")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat messages
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
                <strong>AI Support:</strong><br>{msg['content']}
            </div>
            """, unsafe_allow_html=True)
    
    # Chat input
    user_msg = st.text_area("Your Message", placeholder="I'm here to support you...", key="chat_input")
    
    if st.button("Send 💬", use_container_width=True):
        if user_msg.strip():
            # Add user message
            st.session_state.chat_history.append({'role': 'user', 'content': user_msg})
            
            # Get API key
            try:
                api_key = st.secrets.get('ANTHROPIC_API_KEY', '')
            except:
                api_key = os.environ.get('ANTHROPIC_API_KEY', '')
            
            if api_key:
                try:
                    import anthropic
                    client = anthropic.Anthropic(api_key=api_key)
                    
                    # Build messages for API
                    messages = []
                    for m in st.session_state.chat_history:
                        messages.append({'role': m['role'], 'content': m['content']})
                    
                    # Call Claude API
                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1000,
                        system="""You are a supportive, empathetic AI counselor helping parents navigate child protection cases in South Australia. 

Your role:
- Provide emotional support and encouragement
- Offer practical guidance on reunification steps
- Help them understand court processes and requirements
- Motivate them to keep going when things are hard
- Remind them why they're doing this (their child)

Be warm, professional, caring, and genuinely empathetic. This is a parent fighting to get their child back - treat them with respect and compassion.""",
                        messages=messages
                    )
                    
                    ai_response = response.content[0].text
                    st.session_state.chat_history.append({'role': 'assistant', 'content': ai_response})
                    
                except Exception as e:
                    error_msg = f"I'm having trouble connecting right now. Error: {str(e)}"
                    st.session_state.chat_history.append({'role': 'assistant', 'content': error_msg})
            else:
                st.session_state.chat_history.append({
                    'role': 'assistant', 
                    'content': "AI chat is unavailable - API key not configured. Please contact support."
                })
            
            st.rerun()
    
    # Quick topic buttons
    st.markdown("---")
    st.markdown("### 💡 Quick Topics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("�� I'm feeling overwhelmed", use_container_width=True):
            st.session_state.chat_history.append({
                'role': 'user',
                'content': "I'm feeling really overwhelmed right now. Can you help me?"
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
        if st.button("❓ What should I focus on?", use_container_width=True):
            st.session_state.chat_history.append({
                'role': 'user',
                'content': "What's the most important thing I should focus on right now to get my child back?"
            })
            st.rerun()
    
    # Clear chat
    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

if __name__ == "__main__":
    show_chat()
