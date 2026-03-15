"""Custom metric cards with Phosphor duotone icons."""

import streamlit as st
from config.theme import COLORS


def metric_card(
    icon: str,
    label: str,
    value: str,
    delta: str = None,
    delta_color: str = None,
    icon_color: str = None,
    delay: int = 0,
    # Legacy params kept for compatibility but ignored
    icon_bg: str = None,
):
    """Render a styled metric card with a duotone icon (no background badge)."""
    ic = icon_color or COLORS["brand"]
    anim = f"sn-animate sn-d{delay}" if delay else "sn-animate"

    delta_html = ""
    if delta:
        dc = delta_color or COLORS["muted"]
        delta_html = (
            f'<p style="font-family:Plus Jakarta Sans,sans-serif;font-size:11.5px;'
            f'font-weight:500;color:{dc};margin:0;line-height:1.4;">{delta}</p>'
        )

    html = (
        f'<div class="sn-card {anim}" style="'
        f'background:{COLORS["card_bg"]};border:1px solid {COLORS["border"]};'
        f'border-radius:8px;padding:20px;'
        f'box-shadow:0 1px 2px rgba(0,0,0,0.04),0 1px 3px rgba(0,0,0,0.06);'
        f'margin-bottom:4px;min-height:110px;">'
        f'<div style="display:flex;align-items:flex-start;gap:14px;">'
        f'<i class="ph-duotone ph-{icon}" style="font-size:30px;color:{ic};'
        f'flex-shrink:0;margin-top:2px;"></i>'
        f'<div style="min-width:0;">'
        f'<p style="font-family:Plus Jakarta Sans,sans-serif;font-size:12px;'
        f'font-weight:500;color:{COLORS["muted"]};margin:0 0 3px 0;'
        f'letter-spacing:0.01em;">{label}</p>'
        f'<p style="font-family:JetBrains Mono,monospace;font-size:24px;'
        f'font-weight:700;color:{COLORS["heading"]};margin:0 0 3px 0;'
        f'line-height:1.15;letter-spacing:-0.03em;">{value}</p>'
        f'{delta_html}</div></div></div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def metric_row(metrics: list[dict]):
    """Render a row of metric cards."""
    cols = st.columns(len(metrics))
    for i, (col, m) in enumerate(zip(cols, metrics)):
        with col:
            m.setdefault("delay", i + 1)
            metric_card(**m)
