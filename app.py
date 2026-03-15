"""SecureNet Technologies - Cloud Cybersecurity Monitoring Dashboard."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st

st.set_page_config(
    page_title="SecureNet - Cybersecurity Monitoring",
    page_icon="\U0001f6e1",
    layout="wide",
    initial_sidebar_state="expanded",
)

from components.css_loader import load_css
from components.sidebar import render_sidebar
from config.logging_config import log

load_css()
render_sidebar()
log.info("Dashboard loaded")

pages = [
    st.Page("views/executive_summary.py", title="Executive Summary", icon=":material/dashboard:"),
    st.Page("views/cost_benefit.py", title="Cost-Benefit Analysis", icon=":material/calculate:"),
    st.Page("views/live_simulator.py", title="Live Threat Monitor", icon=":material/monitor_heart:"),
    st.Page("views/threat_dashboard.py", title="Threat Dashboard", icon=":material/security:"),
    st.Page("views/monte_carlo.py", title="Risk Simulation", icon=":material/casino:"),
    st.Page("views/market_analysis.py", title="Market Analysis", icon=":material/trending_up:"),
    st.Page("views/recommendation.py", title="Recommendation", icon=":material/task_alt:"),
]

pg = st.navigation(pages)
pg.run()
