import streamlit as st
import os

def upload_box():

    st.markdown("## 📄 Smart Document Verification")
    st.caption("Upload your government document for AI-powered verification.")

    uploaded_file = st.file_uploader(
        "Choose a Government Document",
        type=["png", "jpg", "jpeg", "pdf"],
        help="Supported: Aadhaar, PAN, Passport, Driving License"
    )

    if uploaded_file:

        st.success("✅ Document uploaded successfully!")

        extension = os.path.splitext(uploaded_file.name)[1].lower()

        # Preview image files
        if extension in [".png", ".jpg", ".jpeg"]:
            st.image(uploaded_file, width=350)

        # Handle PDF files
        elif extension == ".pdf":
            st.info("📄 PDF uploaded successfully.")
            st.write(f"**File Name:** {uploaded_file.name}")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.info("🤖 OCR Status")
            st.progress(0)
            st.caption("Waiting to start OCR...")

            st.info("🛡️ Forgery Detection")
            st.progress(0)
            st.caption("Waiting...")

        with col2:
            st.info("😊 Face Verification")
            st.progress(0)
            st.caption("Waiting...")

            st.metric("📊 AI Trust Score", "--")

        st.divider()

        if st.button(
            "🚀 Start AI Verification",
            use_container_width=True
        ):
            st.success("AI Verification will be implemented in the next sprint.")

    else:
        st.warning("📂 Please upload a document to begin verification.")