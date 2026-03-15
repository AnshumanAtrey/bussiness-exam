"""Visual components: stat highlights, callout boxes, before/after comparisons."""

import streamlit as st
from config.theme import COLORS


def stat_row(stats: list[dict]):
    """Render a row of large stat highlights.

    Each stat dict: {"value": "247", "unit": "min", "label": "avg response time"}
    Optional: "color" for the number color (defaults to brand).
    """
    cols = st.columns(len(stats))
    for i, (col, s) in enumerate(zip(cols, stats)):
        color = s.get("color", COLORS["brand"])
        unit = s.get("unit", "")
        anim = f"sn-animate sn-d{i+1}"
        with col:
            st.markdown(f"""
            <div class="{anim}" style="
                text-align:center;padding:20px 12px;
                background:{COLORS['card_bg']};border:1px solid {COLORS['border']};
                border-radius:8px;
            ">
                <div style="margin-bottom:4px;">
                    <span style="font-family:JetBrains Mono,monospace;font-size:32px;
                        font-weight:700;color:{color};letter-spacing:-0.03em;
                        line-height:1;">{s['value']}</span>
                    <span style="font-family:Plus Jakarta Sans,sans-serif;font-size:14px;
                        font-weight:500;color:{COLORS['muted']};margin-left:3px;">{unit}</span>
                </div>
                <div style="font-family:Plus Jakarta Sans,sans-serif;font-size:12px;
                    color:{COLORS['muted']};letter-spacing:0.02em;">
                    {s['label']}
                </div>
            </div>
            """, unsafe_allow_html=True)


def before_after(before: dict, after: dict):
    """Render a before/after comparison card.

    Each dict: {"value": "247 min", "items": ["Manual detection", "Slow response"]}
    """
    def _render_side(data, label, bg, accent):
        items_html = "".join(
            f'<div style="font-size:12.5px;color:{COLORS["primary_text"]};'
            f'padding:3px 0;">{item}</div>'
            for item in data.get("items", [])
        )
        return f"""
        <div style="flex:1;background:{bg};border-radius:8px;padding:20px;">
            <div style="font-family:Plus Jakarta Sans,sans-serif;font-size:11px;
                font-weight:600;color:{accent};text-transform:uppercase;
                letter-spacing:0.06em;margin-bottom:8px;">{label}</div>
            <div style="font-family:JetBrains Mono,monospace;font-size:22px;
                font-weight:700;color:{COLORS['heading']};margin-bottom:10px;
                letter-spacing:-0.03em;">{data['value']}</div>
            {items_html}
        </div>
        """

    left = _render_side(before, "Before", "#FEF2F2", COLORS["danger"])
    right = _render_side(after, "After", "#ECFDF5", COLORS["success"])
    arrow = f"""
    <div style="display:flex;align-items:center;justify-content:center;
        width:36px;flex-shrink:0;">
        <i class="ph-duotone ph-arrow-right" style="font-size:20px;color:{COLORS['brand']};"></i>
    </div>
    """

    st.markdown(f"""
    <div class="sn-animate" style="display:flex;gap:0;align-items:stretch;
        border:1px solid {COLORS['border']};border-radius:8px;overflow:hidden;
        margin:8px 0;">
        {left}{arrow}{right}
    </div>
    """, unsafe_allow_html=True)


def callout(text: str, icon: str = "info", variant: str = "brand"):
    """Styled callout/highlight box."""
    variants = {
        "brand": (COLORS["brand_tint"], COLORS["brand"]),
        "success": (COLORS["success_light"], COLORS["success"]),
        "danger": (COLORS["danger_light"], COLORS["danger"]),
        "warning": (COLORS["warning_light"], COLORS["warning"]),
    }
    bg, accent = variants.get(variant, variants["brand"])

    st.markdown(f"""
    <div class="sn-animate" style="
        display:flex;align-items:flex-start;gap:12px;
        background:{bg};border-radius:8px;padding:16px 20px;margin:8px 0;
    ">
        <i class="ph-duotone ph-{icon}" style="font-size:20px;color:{accent};
            flex-shrink:0;margin-top:1px;"></i>
        <div style="font-family:Plus Jakarta Sans,sans-serif;font-size:13.5px;
            color:{COLORS['heading']};line-height:1.55;">
            {text}
        </div>
    </div>
    """, unsafe_allow_html=True)


def section_tag(number: str, text: str):
    """Numbered section label with accent styling."""
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:10px;margin:24px 0 8px 0;">
        <span style="font-family:JetBrains Mono,monospace;font-size:12px;
            font-weight:700;color:{COLORS['brand']};background:{COLORS['brand_tint']};
            padding:3px 8px;border-radius:4px;">{number}</span>
        <span style="font-family:Space Grotesk,sans-serif;font-size:13px;
            font-weight:600;color:{COLORS['muted']};text-transform:uppercase;
            letter-spacing:0.06em;">{text}</span>
    </div>
    """, unsafe_allow_html=True)
