import streamlit as st

def metrics():

    c1,c2,c3,c4=st.columns(4)

    c1.metric("📄 Documents","1245","+45")

    c2.metric("🤖 Trust Score","98.7%","+2%")

    c3.metric("👥 Citizens","532","+21")

    c4.metric("🛡 Fraud Alerts","3","-1")