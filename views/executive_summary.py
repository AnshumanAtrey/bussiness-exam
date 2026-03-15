"""Executive Summary - visual landing page for the SecureNet dashboard."""

import streamlit as st

from components.metric_card import metric_row
from components.visual import stat_row, before_after, callout, section_tag
from config.constants import (
    COMPANY_NAME, COMPANY_LOCATION, TOTAL_CLIENTS, INCIDENT_RATE,
    ANNUAL_OPERATIONAL_COST, PROPOSED_INVESTMENT, ESTIMATED_ANNUAL_LOSSES,
    RESPONSE_TIME_BEFORE, RESPONSE_TIME_AFTER,
)
from config.theme import COLORS
from utils.calculations import (
    calculate_annual_savings, calculate_net_benefit,
    calculate_breakeven_months, calculate_cumulative_savings,
)
from utils.formatters import fmt_lakhs, fmt_pct


st.header("Executive Summary")
st.caption(f"{COMPANY_NAME}, {COMPANY_LOCATION}")

# ── Hero stats row ──────────────────────────────────────────────────────────
stat_row([
    {"value": "50", "label": "Client companies served", "color": COLORS["brand"]},
    {"value": "8.0", "unit": "%", "label": "Annual incident rate", "color": COLORS["danger"]},
    {"value": "₹90", "unit": "L", "label": "Yearly operational cost", "color": COLORS["heading"]},
    {"value": "₹60", "unit": "L", "label": "Proposed investment", "color": COLORS["brand"]},
])

st.markdown("")

# ── Situation (compact) ─────────────────────────────────────────────────────
section_tag("01", "The Situation")

col_text, col_compare = st.columns([3, 2])

with col_text:
    st.markdown(
        f"{COMPANY_NAME} provides managed security to {TOTAL_CLIENTS} small and medium "
        f"enterprises across healthcare, financial services, retail, and manufacturing. "
        f"The company currently relies on manual processes for threat detection and incident "
        f"handling, spending {fmt_lakhs(ANNUAL_OPERATIONAL_COST)} annually with an average "
        f"response time of {RESPONSE_TIME_BEFORE['mean']} minutes per incident."
    )
    callout(
        f"With {fmt_pct(INCIDENT_RATE * 100)} of clients affected by incidents annually and "
        f"estimated breach losses of {fmt_lakhs(ESTIMATED_ANNUAL_LOSSES)}, leadership has "
        f"proposed a {fmt_lakhs(PROPOSED_INVESTMENT)} cloud monitoring platform to shift "
        f"from reactive to proactive security.",
        icon="shield-warning",
        variant="danger",
    )

with col_compare:
    before_after(
        before={"value": f"{RESPONSE_TIME_BEFORE['mean']} min", "items": [
            "Manual threat detection",
            "No 24/7 monitoring",
            "Reactive incident response",
            "Basic antivirus only",
        ]},
        after={"value": f"{RESPONSE_TIME_AFTER['mean']} min", "items": [
            "Real-time threat detection",
            "Continuous log monitoring",
            "Automated alerting",
            "Cloud-based dashboard",
        ]},
    )

st.markdown("")

# ── Financial Snapshot ──────────────────────────────────────────────────────
section_tag("02", "Financial Snapshot")

savings = calculate_annual_savings()
total = savings["total_savings"]
breakeven = calculate_breakeven_months(total)
cumulative = calculate_cumulative_savings(total, years=3)
net_y3 = cumulative[-1]["net_benefit"]
response_improvement = (
    (RESPONSE_TIME_BEFORE["mean"] - RESPONSE_TIME_AFTER["mean"])
    / RESPONSE_TIME_BEFORE["mean"] * 100
)

metric_row([
    {"icon": "chart-line-up", "label": "Annual Savings", "value": fmt_lakhs(total),
     "delta": f"Handling {fmt_lakhs(savings['handling_savings'])} + Loss {fmt_lakhs(savings['loss_savings'])}",
     "delta_color": COLORS["success"], "icon_bg": COLORS["success_light"], "icon_color": COLORS["success"]},
    {"icon": "clock-countdown", "label": "Breakeven Period", "value": f"{breakeven:.1f} mo",
     "delta": "Months to recover investment"},
    {"icon": "trend-up", "label": "3-Year Net Benefit", "value": fmt_lakhs(net_y3),
     "delta": "Cumulative after investment", "delta_color": COLORS["success"],
     "icon_bg": COLORS["success_light"], "icon_color": COLORS["success"]},
    {"icon": "timer", "label": "Response Time", "value": f"{response_improvement:.1f}%",
     "delta": f"{RESPONSE_TIME_BEFORE['mean']}min to {RESPONSE_TIME_AFTER['mean']}min faster"},
])

st.markdown("")
callout(
    "Navigate through the top bar to explore interactive cost-benefit modelling, "
    "live threat simulation, Monte Carlo risk analysis, and the final recommendation.",
    icon="grid-four",
)
