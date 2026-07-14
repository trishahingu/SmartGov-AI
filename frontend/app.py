import streamlit as st
from components.sidebar import show_sidebar

st.set_page_config(
    page_title="SmartGov AI",
    page_icon="🏛️",
    layout="wide"
)

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

selected = show_sidebar()

if selected == "Home":

    st.markdown(
        "<div class='main-title'>🏛️ SmartGov AI</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='sub-title'>AI-Powered Government Service Platform</div>",
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📄 Documents Verified", "1,245", "+32")

    with col2:
        st.metric("🤖 AI Trust Score", "98.7%", "+2%")

    with col3:
        st.metric("🛡️ Fraud Alerts", "12", "-4")

    with col4:
        st.metric("👨‍💼 Applications", "532", "+15")

    st.divider()

    left, right = st.columns([2,1])

    with left:
        st.subheader("🚀 Welcome")

        st.info(
            """
SmartGov AI is an AI-powered platform that helps citizens complete
government services using OCR, Face Verification,
Voice AI and Intelligent Document Validation.
            """
        )

    with right:
        st.success("System Status : Online ✅")

    st.divider()

    st.subheader("⚡ Quick Actions")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button("📄 Verify Document")

    with c2:
        st.button("🤖 Start AI Assistant")

    with c3:
        st.button("🎤 Voice Command")