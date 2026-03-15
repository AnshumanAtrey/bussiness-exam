"""Visual components: stat highlights, callout boxes, before/after comparisons.

CRITICAL: All HTML must be written WITHOUT indentation (no 4+ leading spaces)
because Streamlit's markdown parser treats indented lines as code blocks
BEFORE applying unsafe_allow_html. Every HTML string must start at column 0
or be a single-line concatenation.
"""

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
            html = (
                f'<div class="{anim}" style="text-align:center;padding:20px 12px;'
                f'background:{COLORS["card_bg"]};border:1px solid {COLORS["border"]};'
                f'border-radius:8px;">'
                f'<div style="margin-bottom:4px;">'
                f'<span style="font-family:JetBrains Mono,monospace;font-size:32px;'
                f'font-weight:700;color:{color};letter-spacing:-0.03em;'
                f'line-height:1;">{s["value"]}</span>'
                f'<span style="font-family:Plus Jakarta Sans,sans-serif;font-size:14px;'
                f'font-weight:500;color:{COLORS["muted"]};margin-left:3px;">{unit}</span>'
                f'</div>'
                f'<div style="font-family:Plus Jakarta Sans,sans-serif;font-size:12px;'
                f'color:{COLORS["muted"]};letter-spacing:0.02em;">'
                f'{s["label"]}</div></div>'
            )
            st.markdown(html, unsafe_allow_html=True)


def before_after(before: dict, after: dict):
    """Render a before/after comparison card.

    Each dict: {"value": "247 min", "items": ["Manual detection", "Slow response"]}
    """
    def _items(data):
        return "".join(
            f'<div style="font-size:12.5px;color:#1A1D23;padding:3px 0;">{item}</div>'
            for item in data.get("items", [])
        )

    def _side(data, label, bg, accent):
        return (
            f'<div style="flex:1;background:{bg};padding:20px;">'
            f'<div style="font-family:Plus Jakarta Sans,sans-serif;font-size:11px;'
            f'font-weight:600;color:{accent};text-transform:uppercase;'
            f'letter-spacing:0.06em;margin-bottom:8px;">{label}</div>'
            f'<div style="font-family:JetBrains Mono,monospace;font-size:22px;'
            f'font-weight:700;color:#0F1114;margin-bottom:10px;'
            f'letter-spacing:-0.03em;">{data["value"]}</div>'
            f'{_items(data)}</div>'
        )

    left = _side(before, "Before", "#FEF2F2", COLORS["danger"])
    right = _side(after, "After", "#ECFDF5", COLORS["success"])
    arrow = (
        f'<div style="display:flex;align-items:center;justify-content:center;'
        f'width:36px;flex-shrink:0;background:#F9FAFB;">'
        f'<i class="ph-duotone ph-arrow-right" style="font-size:20px;'
        f'color:{COLORS["brand"]};"></i></div>'
    )

    html = (
        f'<div style="display:flex;gap:0;align-items:stretch;'
        f'border:1px solid {COLORS["border"]};border-radius:8px;'
        f'overflow:hidden;margin:8px 0;">'
        f'{left}{arrow}{right}</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def callout(text: str, icon: str = "info", variant: str = "brand"):
    """Styled callout/highlight box."""
    variants = {
        "brand": (COLORS["brand_tint"], COLORS["brand"]),
        "success": (COLORS["success_light"], COLORS["success"]),
        "danger": (COLORS["danger_light"], COLORS["danger"]),
        "warning": (COLORS["warning_light"], COLORS["warning"]),
    }
    bg, accent = variants.get(variant, variants["brand"])

    html = (
        f'<div style="display:flex;align-items:flex-start;gap:12px;'
        f'background:{bg};border-radius:8px;padding:16px 20px;margin:8px 0;">'
        f'<i class="ph-duotone ph-{icon}" style="font-size:20px;color:{accent};'
        f'flex-shrink:0;margin-top:1px;"></i>'
        f'<div style="font-family:Plus Jakarta Sans,sans-serif;font-size:13.5px;'
        f'color:{COLORS["heading"]};line-height:1.55;">{text}</div></div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def section_tag(number: str, text: str):
    """Numbered section label with accent styling."""
    html = (
        f'<div style="display:flex;align-items:center;gap:10px;margin:24px 0 8px 0;">'
        f'<span style="font-family:JetBrains Mono,monospace;font-size:12px;'
        f'font-weight:700;color:{COLORS["brand"]};background:{COLORS["brand_tint"]};'
        f'padding:3px 8px;border-radius:4px;">{number}</span>'
        f'<span style="font-family:Space Grotesk,sans-serif;font-size:13px;'
        f'font-weight:600;color:{COLORS["muted"]};text-transform:uppercase;'
        f'letter-spacing:0.06em;">{text}</span></div>'
    )
    st.markdown(html, unsafe_allow_html=True)
