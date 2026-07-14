import streamlit as st

def hero():

    st.markdown("""
    <style>

    .hero{
        background: linear-gradient(135deg,#2563eb,#0f172a);
        padding:50px;
        border-radius:25px;
        color:white;
        margin-bottom:25px;
    }

    .hero h1{
        font-size:52px;
        margin-bottom:10px;
    }

    .hero p{
        font-size:20px;
        opacity:.9;
    }

    </style>
    """,unsafe_allow_html=True)

    st.markdown("""

    <div class="hero">

    <h1>🏛 SmartGov AI</h1>

    <p>
    AI Powered Government Service Platform
    </p>

    <br>

    Helping Citizens with
    OCR • AI Verification • Voice AI • Computer Vision

    </div>

    """,unsafe_allow_html=True)