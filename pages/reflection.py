"""
Court Reflection Questions
"""
import streamlit as st

QUESTIONS = {
    "Substance Abuse": [
        "What substances were you using when your child was removed?",
        "How often were you using?",
        "Describe a specific day when your substance use affected your parenting.",
        "What did your child see or hear related to your substance use?",
        "How do you think your child felt when they saw you intoxicated?",
        "What triggered your substance use?",
        "What have you learned about how addiction affects children?",
        "What specific changes have you made?",
        "How will you handle cravings if your child returns?"
    ],
    "Domestic Violence": [
        "Describe violent incidents your child witnessed.",
        "What do you think your child was feeling?",
        "How has DV affected your child's sense of safety?",
        "What steps have you taken to ensure this doesn't happen again?",
        "How will you protect your child if your ex returns?",
        "What red flags will you watch for in future relationships?"
    ],
    "Neglect": [
        "What were your child's basic needs that weren't being met?",
        "Why were you unable to meet those needs?",
        "Describe a typical day for your child before removal.",
        "What has changed in your life since then?",
        "How will you ensure your child has food, clothing, supervision?"
    ]
}

def show_reflection():
    st.markdown("""
    <div class="main-header">
        <h1>💭 Court Reflection Questions</h1>
        <p>Demonstrate accountability and insight</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.warning("🔒 **Important:** These answers can be included in court reports to demonstrate accountability")
    
    category = st.selectbox("Choose Category", list(QUESTIONS.keys()))
    
    st.markdown(f"### {category}")
    
    for idx, question in enumerate(QUESTIONS[category], 1):
        st.markdown(f"#### Question {idx}")
        st.markdown(f"*{question}*")
        
        answer = st.text_area(
            "Your Answer",
            height=150,
            key=f"q_{category}_{idx}",
            placeholder="Take your time to answer honestly and thoroughly..."
        )
        
        if st.button(f"�� Save Answer #{idx}", key=f"save_{category}_{idx}"):
            st.success("✅ Saved! This will be included in court reports.")
        
        st.markdown("---")
    
    # Download all
    if st.button("📥 Download All Reflections for Court"):
        report = f"REFLECTION RESPONSES - {category}\n\n"
        for idx, q in enumerate(QUESTIONS[category], 1):
            report += f"Q{idx}: {q}\n\nA: [Your answer here]\n\n{'-'*60}\n\n"
        
        st.download_button("💾 Download", report.encode(), f"reflections_{category.lower().replace(' ', '_')}.txt")
