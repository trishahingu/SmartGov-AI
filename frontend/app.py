import streamlit as st

from components.hero import hero
from components.metric_cards import metrics
from components.search_bar import search_bar
from components.service_cards import service_cards
from components.upload_box import upload_box

st.set_page_config(
    page_title="SmartGov AI",
    page_icon="🏛️",
    layout="wide"
)

hero()

metrics()

st.divider()

search_bar()

st.divider()

service_cards()

st.divider()

upload_box()