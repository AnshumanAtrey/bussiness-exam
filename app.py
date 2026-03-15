"""SecureNet Technologies - Cloud Cybersecurity Monitoring Dashboard."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st

st.set_page_config(
    page_title="SecureNet - Cybersecurity Monitoring",
    page_icon="\U0001f6e1",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from components.css_loader import load_css
from config.theme import LOGO_SVG
from config.logging_config import log

load_css()
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

pg = st.navigation(pages, position="hidden")

# ── Top navigation bar ──────────────────────────────────────────────────────
# Logo + 7 nav links in one row, no spacer column
cols = st.columns([1] + [1] * 7)

with cols[0]:
    st.markdown(
        f'<div style="padding:0;">{LOGO_SVG}</div>',
        unsafe_allow_html=True,
    )

labels = ["Summary", "Cost-Benefit", "Live Monitor", "Dashboard", "Risk Sim", "Market", "Recommend"]
for i, (page, label) in enumerate(zip(pages, labels)):
    with cols[i + 1]:
        st.page_link(page, label=label)

st.markdown(
    '<div style="border-bottom:1px solid #E8EAED;margin:0 0 12px 0;"></div>',
    unsafe_allow_html=True,
)

pg.run()
