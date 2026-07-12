import streamlit as st

st.set_page_config(
    page_title="AEON MATRIX Command Center",
    layout="wide"
)

st.title("🌍 AEON MATRIX TMS — Enterprise AI Command Center")

st.success("Guardian Intelligence Platform Online")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "System Status",
        "ONLINE"
    )

with col2:
    st.metric(
        "AI Governance",
        "ACTIVE"
    )

with col3:
    st.metric(
        "Test Coverage",
        "100%"
    )
