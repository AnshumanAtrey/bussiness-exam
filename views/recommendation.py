"""Final recommendation for the SecureNet cybersecurity investment."""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from components.chart_builders import apply_theme, show
from config.constants import COMPANY_NAME, COMPANY_LOCATION
from config.theme import COLORS, CHART_COLORS


# ── Header ───────────────────────────────────────────────────────────────────
st.header("Recommendation")

# ── Verdict Box ──────────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div style="background:{COLORS['success_light']}; border:1.5px solid {COLORS['success']};
                border-radius:8px; padding:24px 28px; margin-bottom:24px;">
        <div style="font-size:1.35rem; font-weight:700; color:{COLORS['heading']}; margin-bottom:6px;">
            Invest in the Cloud Cybersecurity Monitoring Service
        </div>
        <div style="font-size:0.95rem; color:{COLORS['muted']};">
            The investment is financially sound, strategically necessary, and operationally transformative.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Supporting Arguments ─────────────────────────────────────────────────────
st.subheader("Financial Viability")

st.markdown(
    "The system reaches breakeven in approximately 15.7 months, well within "
    "the first half of a three-year planning window. Cumulative net benefit "
    "by the end of Year 3 is projected at around 78 lakhs. Monte Carlo "
    "simulation across 10,000 scenarios shows a positive return on investment "
    "in 92.1% of cases, even after accounting for variation in cost reduction "
    "efficiency and rising attack frequency. The numbers leave a comfortable "
    "margin of safety."
)

st.subheader("Operational Necessity")

st.markdown(
    "An 8% annual incident rate across 50 client companies, with no automated "
    "monitoring in place, represents an unacceptable exposure. Mean response "
    "time currently sits at 247 minutes per incident. The proposed system "
    "brings that down to 12 minutes, a 95.1% improvement. Moving from reactive "
    "firefighting to proactive detection changes the nature of the service "
    "itself, not just its speed."
)

st.subheader("Strategic Value")

st.markdown(
    "Clients increasingly expect their managed-security provider to offer "
    "real-time visibility, not periodic reports. A cloud-based monitoring "
    "dashboard becomes a differentiator during sales conversations and "
    "renewal negotiations. It also positions SecureNet ahead of upcoming "
    "compliance mandates under the Digital Personal Data Protection Act, "
    "reducing the scramble when regulations tighten."
)

st.divider()

# ── Risk Factors ─────────────────────────────────────────────────────────────
with st.expander("Risk Factors"):
    st.markdown(
        "Implementation delays are the most likely near-term risk. Integrating "
        "with 50 client environments of varying complexity could stretch the "
        "deployment beyond the planned three-month window. Some clients may "
        "resist granting the access permissions required for deep log analysis, "
        "slowing onboarding."
    )
    st.markdown(
        "Ongoing maintenance costs, estimated at 10 to 15% of the initial "
        "investment annually (6 to 9 lakhs), must be budgeted separately. "
        "These cover cloud infrastructure, rule-set updates, and staffing "
        "for a small security operations centre. Failure to account for "
        "recurring costs is a common reason cybersecurity projects underdeliver "
        "after Year 1."
    )

st.divider()

# ── Implementation Timeline ──────────────────────────────────────────────────
st.subheader("Implementation Timeline")

phases = pd.DataFrame([
    {"Phase": "Setup and Integration", "Start": 1, "End": 3},
    {"Phase": "Client Onboarding", "Start": 3, "End": 6},
    {"Phase": "Full Operation and Optimization", "Start": 6, "End": 12},
])

fig = go.Figure()

for i, row in phases.iterrows():
    fig.add_trace(go.Bar(
        y=[row["Phase"]],
        x=[row["End"] - row["Start"]],
        base=[row["Start"]],
        orientation="h",
        marker_color=CHART_COLORS[i],
        text=f"Months {row['Start']}-{row['End']}",
        textposition="inside",
        textfont=dict(color="white", size=12),
        name=row["Phase"],
        showlegend=False,
    ))

apply_theme(fig,
    xaxis_title="Month",
    yaxis=dict(autorange="reversed", gridcolor=COLORS["divider"]),
    xaxis=dict(dtick=1, range=[0, 13], gridcolor=COLORS["divider"]),
    height=220,
    margin=dict(l=40, r=20, t=20, b=40),
)
show(fig)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("")
st.caption(
    f"Analysis prepared for the Business Studies examination, "
    f"{COMPANY_NAME}, {COMPANY_LOCATION}."
)
