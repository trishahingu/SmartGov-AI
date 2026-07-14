import streamlit as st

government_services = [
    ("🪪", "Aadhaar", "Update Aadhaar Details"),
    ("💳", "PAN Card", "PAN Services"),
    ("🛂", "Passport", "Passport Renewal"),
    ("🚗", "Driving License", "Driving Services"),
    ("🗳️", "Voter ID", "Election Services"),
    ("📜", "Birth Certificate", "Certificates"),
]

def service_cards():

    st.markdown("## 🚀 Popular Government Services")

    cols = st.columns(3)

    for index, service in enumerate(government_services):

        icon, title, subtitle = service

        with cols[index % 3]:

            with st.container(border=True):

                st.markdown(f"## {icon}")
                st.markdown(f"### {title}")
                st.caption(subtitle)

                if st.button(
                    "Open Service",
                    key=f"service_btn_{index}"   # <-- unique key
                ):
                    st.success(f"Opening {title}")