"""Sidebar branding and supplementary info."""

import streamlit as st
from config.theme import LOGO_SVG, COLORS


def render_sidebar():
    """Inject the SecureNet logo into the sidebar."""
    st.sidebar.markdown(
        f'<div style="padding:4px 0 12px 0;">{LOGO_SVG}</div>',
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        f'<div style="border-bottom:1px solid {COLORS["border"]};margin-bottom:8px;"></div>',
        unsafe_allow_html=True,
    )
