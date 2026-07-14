import streamlit as st

def services():

    st.subheader("🚀 Popular Government Services")

    c1,c2,c3=st.columns(3)

    with c1:
        st.info("🪪 Aadhaar Services")

    with c2:
        st.info("💳 PAN Card")

    with c3:
        st.info("🛂 Passport")

    c4,c5,c6=st.columns(3)

    with c4:
        st.info("🚗 Driving License")

    with c5:
        st.info("🗳 Voter ID")

    with c6:
        st.info("📄 Income Certificate")