"""Cost-Benefit Analysis - interactive financial modelling (Case Study Q1 and Q2)."""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from components.metric_card import metric_row
from components.chart_builders import apply_theme, show
from config.constants import PROPOSED_INVESTMENT, ANNUAL_OPERATIONAL_COST, ESTIMATED_ANNUAL_LOSSES
from config.theme import COLORS, CHART_COLORS
from utils.calculations import (
    calculate_annual_savings,
    calculate_net_benefit,
    calculate_breakeven_months,
    calculate_cumulative_savings,
)
from utils.formatters import fmt_lakhs, fmt_inr


# ── Header ───────────────────────────────────────────────────────────────────
st.header("Cost-Benefit Analysis")
st.caption("Adjust the parameters below to model different investment scenarios.")

# ── Sliders ──────────────────────────────────────────────────────────────────
sl1, sl2, sl3 = st.columns(3)

with sl1:
    handling_pct = st.slider(
        "Handling cost reduction (%)", min_value=10, max_value=60,
        value=40, step=5, format="%d%%",
    )
with sl2:
    loss_pct = st.slider(
        "Security loss reduction (%)", min_value=10, max_value=70,
        value=50, step=5, format="%d%%",
    )
with sl3:
    investment = st.slider(
        "Investment amount", min_value=30_00_000, max_value=1_00_00_000,
        value=PROPOSED_INVESTMENT, step=5_00_000, format="₹%d",
    )

# ── Calculations ─────────────────────────────────────────────────────────────
savings = calculate_annual_savings(
    handling_reduction=handling_pct / 100,
    loss_reduction=loss_pct / 100,
)
total = savings["total_savings"]
net_y1 = calculate_net_benefit(total, investment)
breakeven = calculate_breakeven_months(total, investment)
cumulative = calculate_cumulative_savings(total, years=5, investment=investment)

# ── Metric Cards ─────────────────────────────────────────────────────────────
st.markdown("")
metric_row([
    {"icon": "coins", "label": "Annual Savings", "value": fmt_lakhs(total),
     "delta": f"Handling {fmt_lakhs(savings['handling_savings'])} + Loss {fmt_lakhs(savings['loss_savings'])}"},
    {"icon": "chart-line-up", "label": "Net Benefit (Year 1)", "value": fmt_lakhs(net_y1),
     "delta": "Savings minus investment",
     "delta_color": COLORS["success"] if net_y1 >= 0 else COLORS["danger"]},
    {"icon": "clock-countdown", "label": "Breakeven Period",
     "value": f"{breakeven:.1f} months" if breakeven < 100 else "N/A",
     "delta": "Months until investment is recovered"},
])

st.markdown("")

# ── Charts ───────────────────────────────────────────────────────────────────
left, right = st.columns(2)

# Left: Savings breakdown horizontal bar chart
with left:
    st.subheader("Savings Breakdown")
    breakdown_df = pd.DataFrame({
        "Category": ["Handling Cost Savings", "Security Loss Savings"],
        "Amount": [savings["handling_savings"], savings["loss_savings"]],
    })
    fig_bar = go.Figure(go.Bar(
        y=breakdown_df["Category"],
        x=breakdown_df["Amount"],
        orientation="h",
        marker_color=[CHART_COLORS[0], CHART_COLORS[1]],
        text=[fmt_lakhs(v) for v in breakdown_df["Amount"]],
        textposition="auto",
    ))
    apply_theme(fig_bar, title=dict(text="Annual Savings by Category"))
    fig_bar.update_layout(
        xaxis_title="Amount (INR)",
        yaxis_title="",
        height=340,
        showlegend=False,
    )
    show(fig_bar)

# Right: Cumulative savings over 5 years with breakeven line
with right:
    st.subheader("Cumulative Projection")
    cum_df = pd.DataFrame(cumulative)
    cum_df["Year"] = cum_df["year"].apply(lambda y: f"Year {y}")

    fig_line = go.Figure()

    # Cumulative savings area
    fig_line.add_trace(go.Scatter(
        x=cum_df["Year"],
        y=cum_df["cumulative_savings"],
        mode="lines+markers",
        name="Cumulative Savings",
        line=dict(color=CHART_COLORS[0], width=2.5),
        fill="tozeroy",
        fillcolor="rgba(13, 124, 102, 0.12)",
        marker=dict(size=7),
    ))

    # Net benefit line
    fig_line.add_trace(go.Scatter(
        x=cum_df["Year"],
        y=cum_df["net_benefit"],
        mode="lines+markers",
        name="Net Benefit",
        line=dict(color=CHART_COLORS[1], width=2),
        marker=dict(size=6),
    ))

    # Investment threshold dashed line
    fig_line.add_hline(
        y=investment,
        line_dash="dash",
        line_color=COLORS["danger"],
        line_width=1.5,
        annotation_text=f"Investment ({fmt_lakhs(investment)})",
        annotation_position="top left",
        annotation_font_color=COLORS["danger"],
    )

    apply_theme(fig_line, title=dict(text="5-Year Financial Trajectory"))
    fig_line.update_layout(
        xaxis_title="",
        yaxis_title="Amount (INR)",
        height=340,
        legend=dict(x=0.02, y=0.98, bgcolor="rgba(255,255,255,0.8)"),
    )
    show(fig_line)

# ── Bottom Summary ───────────────────────────────────────────────────────────
st.divider()
st.subheader("Answering the Case Study Questions")

st.markdown(
    f"**Q1. What are the projected annual savings from adopting the system?** "
    f"With a {handling_pct}% reduction in handling costs and a {loss_pct}% reduction "
    f"in security losses, the projected annual savings amount to "
    f"**{fmt_inr(total)}** ({fmt_lakhs(total)}). This comprises "
    f"{fmt_lakhs(savings['handling_savings'])} from operational efficiency gains and "
    f"{fmt_lakhs(savings['loss_savings'])} from reduced breach-related damages."
)

st.markdown(
    f"**Q2. What is the net benefit of the investment?** "
    f"Net Benefit = Total Annual Savings - Investment = "
    f"{fmt_inr(total)} - {fmt_inr(investment)} = **{fmt_inr(net_y1)}**. "
    f"The first-year net benefit is {'negative, which is expected since the full ' if net_y1 < 0 else 'positive, meaning the '}"
    f"{'investment cost is absorbed upfront. ' if net_y1 < 0 else 'investment pays for itself within the first year. '}"
    f"The breakeven point arrives at approximately **{breakeven:.1f} months**, after which "
    f"the system generates a continuous positive return."
)
