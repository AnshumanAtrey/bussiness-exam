"""Injects custom CSS, fonts, and Phosphor Icons CDN."""

import os
import streamlit as st
from config.theme import PHOSPHOR_CDN


def load_css():
    """Load all external resources and custom styles. Call once at app start."""
    # Phosphor Icons (duotone)
    st.markdown(
        f'<link rel="stylesheet" href="{PHOSPHOR_CDN}">',
        unsafe_allow_html=True,
    )

    # Custom stylesheet
    css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
