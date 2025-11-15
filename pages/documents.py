"""
Documents & AI Analysis
"""
import streamlit as st
import anthropic
import os
import sys
sys.path.append('..')
from database import get_connection

def show_documents():
    st.markdown("""
    <div class="main-header">
        <h1>📄 Document Management</h1>
        <p>Upload and analyze case documents with AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Upload section
    with st.expander("📤 Upload New Document", expanded=True):
        uploaded_file = st.file_uploader("Choose file", type=['pdf', 'txt', 'jpg', 'png'])
        doc_type = st.selectbox("Type", ["Court Order", "DCP Letter", "Case Plan", "Drug Test", "Certificate"])
        
        if uploaded_file and st.button("�� Upload & Analyze", use_container_width=True):
            with st.spinner("Analyzing..."):
                # Read file
                if uploaded_file.type == "text/plain":
                    text = uploaded_file.read().decode('utf-8')
                else:
                    text = "Document uploaded"
                
                # AI Analysis
                api_key = os.environ.get('ANTHROPIC_API_KEY', st.secrets.get('ANTHROPIC_API_KEY', ''))
                if api_key:
                    try:
                        client = anthropic.Anthropic(api_key=api_key)
                        response = client.messages.create(
                            model="claude-sonnet-4-20250514",
                            max_tokens=2000,
                            messages=[{"role": "user", "content": f"Analyze this {doc_type}: {text[:3000]}. Extract: 1) Plain English summary, 2) Parent obligations with deadlines, 3) DCP violations of SA law, 4) Urgency level, 5) Next steps"}]
                        )
                        analysis = response.content[0].text
                    except:
                        analysis = "AI analysis unavailable"
                else:
                    analysis = "AI analysis unavailable - configure API key"
                
                # Save
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("""
                INSERT INTO documents (case_id, document_name, document_type, ai_analysis)
                VALUES (?, ?, ?, ?)
                """, (1, uploaded_file.name, doc_type, analysis))
                conn.commit()
                conn.close()
                
                st.success("✅ Uploaded!")
                st.rerun()
    
    st.markdown("---")
    
    # Documents list
    st.markdown("### 📋 Your Documents")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT document_id, document_name, document_type, upload_date, ai_analysis FROM documents WHERE case_id = 1 ORDER BY upload_date DESC")
    docs = cursor.fetchall()
    conn.close()
    
    if docs:
        for doc_id, name, dtype, date, analysis in docs:
            with st.expander(f"📄 {name} ({dtype})"):
                st.markdown(f"**Uploaded:** {date}")
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.button("📥 Download", key=f"dl_{doc_id}")
                with col2:
                    st.button("🖨️ Print", key=f"p_{doc_id}")
                with col3:
                    st.button("📤 Share", key=f"s_{doc_id}")
                with col4:
                    if st.button("🗑️ Delete", key=f"d_{doc_id}"):
                        conn = get_connection()
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM documents WHERE document_id = ?", (doc_id,))
                        conn.commit()
                        conn.close()
                        st.rerun()
                
                if analysis:
                    st.markdown("---")
                    st.markdown("### 🤖 AI Analysis")
                    st.markdown(analysis)
                    st.download_button("💾 Download Analysis", analysis.encode(), f"analysis_{name}.txt", key=f"da_{doc_id}")
    else:
        st.info("No documents yet. Upload above!")
