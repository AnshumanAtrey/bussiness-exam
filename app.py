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
from config.theme import LOGO_SVG, COLORS
from config.logging_config import log

load_css()
log.info("Dashboard loaded")

pages = [
    st.Page("views/executive_summary.py", title="Executive Summary", icon=":material/dashboard:"),
    st.Page("views/cost_benefit.py", title="Cost-Benefit Analysis", icon=":material/calculate:"),
    st.Page("views/investment_breakdown.py", title="Investment Breakdown", icon=":material/account_balance:"),
    st.Page("views/live_simulator.py", title="Live Threat Monitor", icon=":material/monitor_heart:"),
    st.Page("views/threat_dashboard.py", title="Threat Dashboard", icon=":material/security:"),
    st.Page("views/monte_carlo.py", title="Risk Simulation", icon=":material/casino:"),
    st.Page("views/market_analysis.py", title="Market Analysis", icon=":material/trending_up:"),
    st.Page("views/recommendation.py", title="Recommendation", icon=":material/task_alt:"),
]

pg = st.navigation(pages, position="hidden")

# ── Top navigation bar ──────────────────────────────────────────────────────
cols = st.columns([0.9] + [1] * 8)

with cols[0]:
    st.markdown(
        f'<div style="padding:0;">{LOGO_SVG}</div>',
        unsafe_allow_html=True,
    )

labels = ["Summary", "Cost-Benefit", "Investment", "Live Monitor", "Dashboard", "Risk Sim", "Market", "Recommend"]
for i, (page, label) in enumerate(zip(pages, labels)):
    with cols[i + 1]:
        if page.title == pg.title:
            # Active page: render as styled HTML (not st.page_link which has
            # Streamlit's inline gray disabled style that CSS cannot override)
            st.markdown(
                f'<div style="font-family:Plus Jakarta Sans,sans-serif;font-size:12.5px;'
                f'font-weight:600;color:{COLORS["brand_hover"]};background:{COLORS["brand_tint"]};'
                f'padding:5px 10px;border-radius:6px;white-space:nowrap;'
                f'display:inline-block;">{label}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.page_link(page, label=label)

st.markdown(
    '<div style="border-bottom:1px solid #E8EAED;margin:0 0 10px 0;"></div>',
    unsafe_allow_html=True,
)

pg.run()
