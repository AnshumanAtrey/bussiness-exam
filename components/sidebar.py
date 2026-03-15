"""Sidebar branding and supplementary info."""

import os
import base64
import streamlit as st
from config.theme import LOGO_SVG, LOGO_ICON_SVG


def _svg_to_data_uri(svg_str: str) -> str:
    """Convert an SVG string to a data URI for st.logo."""
    encoded = base64.b64encode(svg_str.encode()).decode()
    return f"data:image/svg+xml;base64,{encoded}"


def render_sidebar():
    """Place the SecureNet logo at the top of the sidebar using st.logo."""
    st.logo(
        image=_svg_to_data_uri(LOGO_SVG),
        icon_image=_svg_to_data_uri(LOGO_ICON_SVG),
    )
