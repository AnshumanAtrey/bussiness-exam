"""Threat Dashboard - pre-generated data analysis across attacks, clients, and capabilities."""

import streamlit as st
import pandas as pd
import plotly.express as px

from components.metric_card import metric_row
from components.chart_builders import (
    create_bar_chart, create_pie_chart, create_line_chart, apply_theme, show,
)
from config.constants import SYSTEM_FEATURES, RESPONSE_TIME_BEFORE, RESPONSE_TIME_AFTER
from config.theme import COLORS, CHART_COLORS
from data.generators.attack_simulator import generate_client_profiles, generate_attack_history
from utils.formatters import fmt_pct


@st.cache_data
def _load_data():
    return generate_client_profiles(), generate_attack_history()


clients, attacks = _load_data()

st.header("Threat Dashboard")

tab_attack, tab_client, tab_system = st.tabs(
    ["Attack Analysis", "Client Risk", "System Capabilities"]
)

# ── Tab 1: Attack Analysis ───────────────────────────────────────────────────
with tab_attack:
    total_events = attacks.shape[0]
    breach_count = (attacks["outcome"] == "Breach").sum()
    breach_rate = breach_count / total_events * 100
    avg_response = attacks["response_time_min"].mean()

    metric_row([
        {"icon": "siren", "label": "Total Events", "value": str(total_events)},
        {"icon": "shield-warning", "label": "Breach Rate", "value": fmt_pct(breach_rate),
         "delta": f"{breach_count} confirmed breaches", "delta_color": COLORS["danger"]},
        {"icon": "timer", "label": "Avg Response Time", "value": f"{avg_response:.0f} min"},
    ])

    st.markdown("")
    col_left, col_right = st.columns(2)

    with col_left:
        type_counts = attacks["attack_type"].value_counts().reset_index()
        type_counts.columns = ["attack_type", "count"]
        create_pie_chart(type_counts, names="attack_type", values="count",
                         title="Attack Type Distribution")

    with col_right:
        sev_counts = attacks["severity"].value_counts().reindex(
            ["Low", "Medium", "High", "Critical"]
        ).reset_index()
        sev_counts.columns = ["severity", "count"]
        create_bar_chart(sev_counts, x="severity", y="count", title="Severity Distribution")

    st.markdown("")
    attacks["month"] = pd.to_datetime(attacks["date"]).dt.to_period("M").astype(str)
    monthly = attacks.groupby("month").size().reset_index(name="events")
    create_line_chart(monthly, x="month", y="events", title="Monthly Attack Trend")

# ── Tab 2: Client Risk ───────────────────────────────────────────────────────
with tab_client:
    st.subheader("Highest-Risk Clients")

    top10 = clients.nlargest(10, "risk_score")[
        ["client_name", "industry", "risk_score", "security_level", "incidents_last_year"]
    ].reset_index(drop=True)
    top10.index = top10.index + 1
    st.dataframe(top10, use_container_width=True, hide_index=False)

    st.markdown("")
    col_l, col_r = st.columns(2)

    with col_l:
        ind_counts = attacks.groupby("industry").size().reset_index(name="events")
        ind_counts = ind_counts.sort_values("events", ascending=True)
        create_bar_chart(ind_counts, x="industry", y="events",
                         title="Attacks by Industry", horizontal=True)

    with col_r:
        fig = px.histogram(clients, x="risk_score", nbins=15,
                           title="Risk Score Distribution",
                           color_discrete_sequence=CHART_COLORS)
        apply_theme(fig)
        show(fig)

# ── Tab 3: System Capabilities ───────────────────────────────────────────────
with tab_system:
    st.subheader("Monitoring Platform Features")

    _icons = [
        "shield-check", "terminal-window", "grid-four", "magnifying-glass",
        "lock", "chart-line-up", "seal-check", "network",
    ]

    cards = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:24px;">'
    for i, feat in enumerate(SYSTEM_FEATURES):
        ico = _icons[i] if i < len(_icons) else "gear-six"
        cards += (
            f'<div style="background:{COLORS["card_bg"]};border:1px solid {COLORS["border"]};'
            f'border-radius:8px;padding:16px 18px;display:flex;align-items:flex-start;gap:12px;">'
            f'<div style="display:flex;align-items:center;justify-content:center;width:36px;'
            f'height:36px;border-radius:6px;background:{COLORS["brand_tint"]};flex-shrink:0;">'
            f'<i class="ph-duotone ph-{ico}" style="font-size:18px;color:{COLORS["brand"]};"></i>'
            f'</div><p style="font-family:Plus Jakarta Sans,sans-serif;font-size:13px;'
            f'color:{COLORS["primary_text"]};margin:0;line-height:1.5;padding-top:7px;">'
            f'{i + 1}. {feat}</p></div>'
        )
    cards += "</div>"
    st.markdown(cards, unsafe_allow_html=True)

    st.divider()
    st.subheader("How Real-Time Monitoring Strengthens Small Business Security")

    st.markdown(
        f"The most immediate benefit of a cloud-based monitoring system is the "
        f"reduction in response time. Before deployment, SecureNet's average "
        f"response time to a detected threat was roughly "
        f"{RESPONSE_TIME_BEFORE['mean']} minutes, which translates to over four "
        f"hours of potential exposure for every incident. After deployment the "
        f"system brings that figure down to approximately "
        f"{RESPONSE_TIME_AFTER['mean']} minutes, a reduction of over 95 percent. "
        f"For a small company with limited IT staff, this shift from reactive to "
        f"proactive detection can mean the difference between a contained alert "
        f"and a full-scale data breach."
    )

    st.markdown(
        "Automated log collection and anomaly detection remove the dependency on "
        "manual review, which is both slow and inconsistent. When a monitoring "
        "platform ingests logs from firewalls, endpoints, and cloud workloads "
        "simultaneously, it can correlate patterns that a human analyst reviewing "
        "one source at a time would miss. This is particularly relevant for "
        "phishing and insider-threat scenarios, where early signals are subtle "
        "and time-sensitive."
    )

    st.markdown(
        "Cost reduction follows naturally. By automating routine detection and "
        "triage, the firm estimates a 40 percent reduction in incident handling "
        "costs and a 50 percent reduction in breach-related losses. The proposed "
        "investment of 60 lakhs reaches breakeven within roughly 17 months, after "
        "which the savings compound. For small enterprises that cannot absorb the "
        "financial impact of even a single ransomware event, this kind of "
        "predictable cost structure is important."
    )

    st.markdown(
        "Finally, compliance readiness becomes a continuous process rather than "
        "an annual scramble. The platform generates audit trails and reports "
        "aligned with ISO 27001 and GDPR requirements, which helps clients in "
        "regulated industries like healthcare and financial services maintain "
        "their certifications without dedicated compliance teams."
    )
