import streamlit as st

from components.hero import hero
from components.metric_cards import metrics
from components.service_cards import services

st.set_page_config(
    page_title="SmartGov AI",
    page_icon="🏛️",
    layout="wide"
)

hero()

metrics()

st.divider()

st.text_input(
    "🔍 Ask SmartGov AI",
    placeholder="Example: How do I update my Aadhaar address?"
)

st.button("🎤 Start Voice Assistant")

st.divider()

services()