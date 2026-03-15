"""Executive Summary - landing page for the SecureNet cybersecurity dashboard."""

import streamlit as st

from components.metric_card import metric_row
from config.constants import (
    COMPANY_NAME,
    COMPANY_LOCATION,
    TOTAL_CLIENTS,
    INCIDENT_RATE,
    ANNUAL_OPERATIONAL_COST,
    PROPOSED_INVESTMENT,
    ESTIMATED_ANNUAL_LOSSES,
    RESPONSE_TIME_BEFORE,
    RESPONSE_TIME_AFTER,
)
from utils.calculations import (
    calculate_annual_savings,
    calculate_net_benefit,
    calculate_breakeven_months,
    calculate_cumulative_savings,
)
from utils.formatters import fmt_lakhs, fmt_pct


# ── Header ───────────────────────────────────────────────────────────────────
st.header("Executive Summary")
st.caption(
    f"{COMPANY_NAME}, {COMPANY_LOCATION}. Cloud-Based Cybersecurity Monitoring System"
)

# ── Situational Metrics ──────────────────────────────────────────────────────
metric_row([
    {"icon": "buildings", "label": "Client Companies", "value": str(TOTAL_CLIENTS),
     "delta": "Across 10 industries"},
    {"icon": "shield-warning", "label": "Incident Rate", "value": fmt_pct(INCIDENT_RATE * 100),
     "delta": "Clients affected annually"},
    {"icon": "currency-inr", "label": "Annual Operational Cost", "value": fmt_lakhs(ANNUAL_OPERATIONAL_COST),
     "delta": "Manual handling and response"},
    {"icon": "lock", "label": "Proposed Investment", "value": fmt_lakhs(PROPOSED_INVESTMENT),
     "delta": "One-time system deployment"},
])

st.divider()

# ── The Situation ─────────────────────────────────────────────────────────────
st.subheader("The Situation")

st.markdown(
    f"{COMPANY_NAME} is a Mumbai-based cybersecurity firm that provides managed security "
    f"services to {TOTAL_CLIENTS} small and medium enterprises spread across healthcare, "
    f"financial services, retail, manufacturing, and six other sectors. The company currently "
    f"relies on manual processes for threat detection, incident handling, and compliance "
    f"reporting, resulting in annual operational costs of {fmt_lakhs(ANNUAL_OPERATIONAL_COST)} "
    f"and an average incident response time of roughly {RESPONSE_TIME_BEFORE['mean']} minutes."
)

st.markdown(
    f"Approximately {fmt_pct(INCIDENT_RATE * 100)} of its client base experiences a security "
    f"incident each year, and estimated breach-related losses amount to "
    f"{fmt_lakhs(ESTIMATED_ANNUAL_LOSSES)} annually. The firm's leadership has proposed a "
    f"{fmt_lakhs(PROPOSED_INVESTMENT)} investment in a cloud-based monitoring platform that "
    f"would automate log analysis, threat detection, vulnerability scanning, and incident "
    f"response workflows."
)

st.markdown(
    "This dashboard evaluates whether the proposed investment is financially justified by "
    "examining projected cost savings, the breakeven timeline, and the net benefit over a "
    "multi-year horizon. The analysis also models how response times, incident severity, "
    "and operational efficiency would change after deployment."
)

st.divider()

# ── Financial Snapshot ────────────────────────────────────────────────────────
st.subheader("Financial Snapshot")

savings = calculate_annual_savings()
total = savings["total_savings"]
net_y1 = calculate_net_benefit(total)
breakeven = calculate_breakeven_months(total)
cumulative = calculate_cumulative_savings(total, years=3)
net_y3 = cumulative[-1]["net_benefit"]

response_improvement = (
    (RESPONSE_TIME_BEFORE["mean"] - RESPONSE_TIME_AFTER["mean"])
    / RESPONSE_TIME_BEFORE["mean"]
    * 100
)

metric_row([
    {"icon": "chart-line-up", "label": "Annual Savings", "value": fmt_lakhs(total),
     "delta": "Handling + loss reduction", "delta_color": "#1A7F4B"},
    {"icon": "clock-countdown", "label": "Breakeven Period",
     "value": f"{breakeven:.1f} months", "delta": "Time to recover investment"},
    {"icon": "trend-up", "label": "3-Year Net Benefit", "value": fmt_lakhs(net_y3),
     "delta": "Cumulative savings minus investment", "delta_color": "#1A7F4B"},
    {"icon": "timer", "label": "Response Time Improvement",
     "value": fmt_pct(response_improvement),
     "delta": f"{RESPONSE_TIME_BEFORE['mean']} min to {RESPONSE_TIME_AFTER['mean']} min"},
])

# ── Closing ───────────────────────────────────────────────────────────────────
st.markdown("")
st.markdown(
    "Use the sidebar to explore the **Cost-Benefit Analysis** for interactive financial "
    "modelling, or visit the other detail pages for deeper breakdowns of incident data, "
    "response-time distributions, and system architecture."
)
