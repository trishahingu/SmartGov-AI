import streamlit as st

def search_bar():

    st.markdown("## 🔍 AI Government Copilot")

    query = st.text_input(
    "Ask SmartGov AI",
    placeholder="How do I update my Aadhaar address?",
    label_visibility="collapsed"
)

    col1, col2 = st.columns([5,1])

    with col2:
        st.button("🎤 Voice")

    if query:
        st.success(f"You asked: {query}")

    return query