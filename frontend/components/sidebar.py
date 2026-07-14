from streamlit_option_menu import option_menu
import streamlit as st


def show_sidebar():

    with st.sidebar:

        selected = option_menu(
            "SmartGov AI",
            [
                "Home",
                "AI Command Center",
                "Smart Verification",
                "AI Assistant",
                "Analytics",
                "Officer Portal",
                "Settings"
            ],
            icons=[
                "house",
                "cpu",
                "file-earmark-text",
                "robot",
                "bar-chart",
                "person-badge",
                "gear"
            ],
            default_index=0,
        )

    return selected