"""Final recommendation for the SecureNet cybersecurity investment."""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from components.chart_builders import apply_theme, show
from components.visual import callout, section_tag, stat_row
from config.constants import COMPANY_NAME, COMPANY_LOCATION
from config.theme import COLORS, CHART_COLORS


st.header("Recommendation")

# ── Verdict Box ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="sn-animate" style="
    background:linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
    border:1.5px solid {COLORS['success']};
    border-radius:10px;padding:28px 32px;margin-bottom:20px;">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <i class="ph-duotone ph-seal-check" style="font-size:28px;color:{COLORS['success']};"></i>
        <span style="font-family:Space Grotesk,sans-serif;font-size:1.3rem;font-weight:700;
            color:{COLORS['heading']};">Invest in the Cloud Cybersecurity Monitoring Service</span>
    </div>
    <div style="font-family:Plus Jakarta Sans,sans-serif;font-size:14px;
        color:{COLORS['muted']};max-width:700px;">
        The investment is financially sound, strategically necessary, and operationally
        transformative for SecureNet and its 50 client companies.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Key numbers at a glance ──────────────────────────────────────────────────
stat_row([
    {"value": "15.7", "unit": "mo", "label": "Breakeven period", "color": COLORS["brand"]},
    {"value": "₹78", "unit": "L", "label": "3-year net benefit", "color": COLORS["success"]},
    {"value": "92.1", "unit": "%", "label": "Positive ROI probability", "color": COLORS["brand"]},
    {"value": "95.1", "unit": "%", "label": "Response time improvement", "color": COLORS["success"]},
])

st.markdown("")

# ── Supporting Arguments ─────────────────────────────────────────────────────
section_tag("01", "Financial Viability")

st.markdown(
    "The system reaches breakeven in approximately 15.7 months, well within "
    "the first half of a three-year planning window. Cumulative net benefit "
    "by the end of Year 3 is projected at around 78 lakhs. Monte Carlo "
    "simulation across 10,000 scenarios shows a positive return on investment "
    "in 92.1% of cases, even after accounting for variation in cost reduction "
    "efficiency and rising attack frequency."
)

section_tag("02", "Operational Necessity")

col_left, col_right = st.columns([3, 2])
with col_left:
    st.markdown(
        "An 8% annual incident rate across 50 client companies, with no automated "
        "monitoring in place, represents an unacceptable exposure. Mean response "
        "time currently sits at 247 minutes per incident. The proposed system "
        "brings that down to 12 minutes, a 95.1% improvement."
    )
with col_right:
    callout(
        "Moving from reactive firefighting to proactive detection changes "
        "the nature of the service itself, not just its speed.",
        icon="shield-check", variant="brand",
    )

section_tag("03", "Strategic Value")

st.markdown(
    "Clients increasingly expect their managed-security provider to offer "
    "real-time visibility, not periodic reports. A cloud-based monitoring "
    "dashboard becomes a differentiator during sales conversations and "
    "renewal negotiations. It also positions SecureNet ahead of upcoming "
    "compliance mandates under the Digital Personal Data Protection Act."
)

st.markdown("")

# ── Risk Factors ─────────────────────────────────────────────────────────────
with st.expander("Risk Factors to Consider"):
    r1, r2 = st.columns(2)
    with r1:
        callout(
            "Implementation delays from integrating with 50 client environments "
            "of varying complexity could stretch beyond the 3-month window.",
            icon="warning-diamond", variant="warning",
        )
    with r2:
        callout(
            "Ongoing maintenance costs of 10-15% of investment annually (6-9 lakhs) "
            "must be budgeted separately for infrastructure, updates, and staffing.",
            icon="currency-inr", variant="warning",
        )

st.markdown("")

# ── Implementation Timeline ──────────────────────────────────────────────────
section_tag("04", "Implementation Timeline")

phases = pd.DataFrame([
    {"Phase": "Setup and Integration", "Start": 1, "End": 3},
    {"Phase": "Client Onboarding", "Start": 3, "End": 6},
    {"Phase": "Full Operation", "Start": 6, "End": 12},
])

fig = go.Figure()
for i, row in phases.iterrows():
    fig.add_trace(go.Bar(
        y=[row["Phase"]], x=[row["End"] - row["Start"]], base=[row["Start"]],
        orientation="h", marker_color=CHART_COLORS[i],
        text=f"Months {row['Start']}-{row['End']}", textposition="inside",
        textfont=dict(color="white", size=12), name=row["Phase"], showlegend=False,
    ))

apply_theme(fig,
    xaxis_title="Month",
    yaxis=dict(autorange="reversed", gridcolor=COLORS["divider"]),
    xaxis=dict(dtick=1, range=[0, 13], gridcolor=COLORS["divider"]),
    height=200, margin=dict(l=40, r=20, t=16, b=36),
)
show(fig)

st.caption(
    f"Analysis prepared for the Business Studies examination, "
    f"{COMPANY_NAME}, {COMPANY_LOCATION}."
)
