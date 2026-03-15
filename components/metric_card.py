"""Custom metric cards with Phosphor duotone icons."""

import streamlit as st
from config.theme import COLORS


def metric_card(
    icon: str,
    label: str,
    value: str,
    delta: str = None,
    delta_color: str = None,
    icon_bg: str = None,
    icon_color: str = None,
    delay: int = 0,
):
    """Render a styled metric card.

    Args:
        icon: Phosphor icon name (e.g. "shield-check", "currency-inr")
        label: Short label above the value
        value: The main metric value (already formatted)
        delta: Optional change indicator text
        delta_color: Color for the delta text
        icon_bg: Background color for icon badge
        icon_color: Icon color
        delay: Animation delay class (0-4)
    """
    bg = icon_bg or COLORS["brand_tint"]
    ic = icon_color or COLORS["brand"]
    anim = f"sn-animate sn-d{delay}" if delay else "sn-animate"

    delta_html = ""
    if delta:
        dc = delta_color or COLORS["success"]
        delta_html = (
            f'<p style="font-family:Plus Jakarta Sans,sans-serif;font-size:12px;'
            f'font-weight:500;color:{dc};margin:0;line-height:1.4;">{delta}</p>'
        )

    html = f"""
    <div class="{anim}" style="
        background:{COLORS['card_bg']};
        border:1px solid {COLORS['border']};
        border-radius:8px;
        padding:24px;
        box-shadow:0 1px 2px rgba(0,0,0,0.04),0 1px 3px rgba(0,0,0,0.06);
        margin-bottom:4px;
    ">
        <div style="display:flex;align-items:flex-start;gap:16px;">
            <div style="
                display:flex;align-items:center;justify-content:center;
                width:48px;height:48px;border-radius:8px;
                background:{bg};flex-shrink:0;
            ">
                <i class="ph-duotone ph-{icon}" style="font-size:24px;color:{ic};"></i>
            </div>
            <div style="min-width:0;">
                <p style="
                    font-family:Plus Jakarta Sans,sans-serif;font-size:13px;
                    font-weight:500;color:{COLORS['muted']};margin:0 0 4px 0;
                ">{label}</p>
                <p style="
                    font-family:JetBrains Mono,monospace;font-size:28px;
                    font-weight:700;color:{COLORS['heading']};margin:0 0 4px 0;
                    line-height:1.1;
                ">{value}</p>
                {delta_html}
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def metric_row(metrics: list[dict]):
    """Render a row of metric cards.

    Args:
        metrics: List of dicts, each containing keyword args for metric_card.
    """
    cols = st.columns(len(metrics))
    for i, (col, m) in enumerate(zip(cols, metrics)):
        with col:
            m.setdefault("delay", i + 1)
            metric_card(**m)
