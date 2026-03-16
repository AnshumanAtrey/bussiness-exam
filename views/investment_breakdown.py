"""Investment Breakdown - detailed before/after cost analysis and 5-year projection."""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from components.metric_card import metric_row
from components.chart_builders import apply_theme, show
from components.visual import stat_row, before_after, callout, section_tag
from config.theme import COLORS, CHART_COLORS
from utils.formatters import fmt_lakhs


st.header("Investment Breakdown")
st.caption("Where the money goes today, what changes after the platform, and what the next 5 years look like.")

tab_current, tab_after, tab_projection = st.tabs([
    "Current Operations (₹90L)", "After Investment (₹60L)", "5-Year Projection"
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1: Current Operations
# ══════════════════════════════════════════════════════════════════════════════
with tab_current:
    section_tag("01", "Where ₹90 Lakhs Goes Every Year")

    st.markdown(
        "SecureNet currently runs a fully manual security operation with 9 staff "
        "members handling everything from daily log reviews to on-site audits. "
        "Staffing alone consumes 64% of the budget."
    )

    # Staffing table
    st.markdown("")
    st.markdown("**Staffing (₹58.0L, 64% of budget)**")
    staff_before = pd.DataFrame([
        {"Role": "SOC Manager / Lead", "Count": 1, "Monthly (₹)": "85,000", "Annual with Overhead (₹)": "13.26L"},
        {"Role": "L2 Security Analysts", "Count": 2, "Monthly (₹)": "50,000 each", "Annual with Overhead (₹)": "15.60L"},
        {"Role": "L1 SOC / VAPT Analysts", "Count": 4, "Monthly (₹)": "30,000 each", "Annual with Overhead (₹)": "18.72L"},
        {"Role": "Network / System Admin", "Count": 1, "Monthly (₹)": "40,000", "Annual with Overhead (₹)": "6.24L"},
        {"Role": "IR Consultant (retainer)", "Count": 1, "Monthly (₹)": "35,000", "Annual with Overhead (₹)": "4.20L"},
    ])
    st.dataframe(staff_before, use_container_width=True, hide_index=True)

    callout(
        "Each L1 analyst manually monitors ~12 clients. Daily log review, basic VAPT, "
        "ticket creation, firewall checks. This is why 4 incidents slipped through last year.",
        icon="warning-diamond", variant="warning",
    )

    # Other costs
    st.markdown("")
    st.markdown("**Other Operating Costs (₹32.0L)**")
    other_before = pd.DataFrame([
        {"Category": "Office rent (800 sqft, Andheri)", "Annual (₹)": "9.60L"},
        {"Category": "Electricity, UPS, power backup", "Annual (₹)": "1.80L"},
        {"Category": "Internet (100 Mbps leased line)", "Annual (₹)": "1.44L"},
        {"Category": "IT hardware depreciation (laptops, server)", "Annual (₹)": "3.00L"},
        {"Category": "Phone and mobile reimbursements", "Annual (₹)": "0.96L"},
        {"Category": "Antivirus + basic SIEM (ManageEngine)", "Annual (₹)": "2.70L"},
        {"Category": "Ticketing, VPN, email security", "Annual (₹)": "1.50L"},
        {"Category": "Travel to client sites (50 visits/yr)", "Annual (₹)": "1.80L"},
        {"Category": "Training and certifications", "Annual (₹)": "2.00L"},
        {"Category": "Cyber insurance + compliance", "Annual (₹)": "1.40L"},
        {"Category": "Incident handling (4 incidents)", "Annual (₹)": "3.00L"},
        {"Category": "Miscellaneous", "Annual (₹)": "2.80L"},
    ])
    st.dataframe(other_before, use_container_width=True, hide_index=True)

    # Pie chart
    fig = go.Figure(go.Pie(
        labels=["Staffing", "Office + Infra", "Software + Tools", "Operations", "Incidents"],
        values=[58.0, 16.8, 4.5, 7.7, 3.0],
        hole=0.45,
        marker=dict(colors=CHART_COLORS[:5]),
        textinfo="label+percent",
        textposition="outside",
        textfont=dict(size=12),
    ))
    apply_theme(fig, height=340, title=dict(text="Annual Cost Distribution (₹90L)"),
                margin=dict(l=20, r=20, t=50, b=20))
    show(fig)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2: After Investment
# ══════════════════════════════════════════════════════════════════════════════
with tab_after:
    section_tag("02", "The ₹60L Investment")

    st.markdown(
        "The budget goes primarily to people, infrastructure, and onboarding. "
        "The tools themselves are open-source (Wazuh, Zabbix, Grafana, TheHive), "
        "so licensing cost is nearly zero."
    )

    col_invest, col_stack = st.columns([3, 2])

    with col_invest:
        st.markdown("**Where ₹60 Lakhs Goes (One-Time)**")
        invest_df = pd.DataFrame([
            {"Item": "SOC analyst hiring (2 new, 6-month ramp)", "Amount (₹)": "18.0L"},
            {"Item": "Wazuh SIEM multi-tenant deployment", "Amount (₹)": "5.0L"},
            {"Item": "Zabbix + Grafana + TheHive setup", "Amount (₹)": "2.0L"},
            {"Item": "Cloud infrastructure setup", "Amount (₹)": "2.0L"},
            {"Item": "SOC hardware (workstations, monitors)", "Amount (₹)": "5.0L"},
            {"Item": "Client onboarding (agents, docs)", "Amount (₹)": "5.0L"},
            {"Item": "Staff training and certifications", "Amount (₹)": "3.0L"},
            {"Item": "Nessus Professional (Year 1)", "Amount (₹)": "5.0L"},
            {"Item": "Legal, compliance, insurance", "Amount (₹)": "3.0L"},
            {"Item": "Marketing and client acquisition", "Amount (₹)": "4.0L"},
            {"Item": "Contingency reserve", "Amount (₹)": "8.0L"},
        ])
        st.dataframe(invest_df, use_container_width=True, hide_index=True)

    with col_stack:
        st.markdown("**Tool Stack (All Open-Source)**")
        stack_html = ""
        tools = [
            ("shield-check", "Wazuh", "SIEM + EDR"),
            ("globe", "Zabbix", "Network Monitor"),
            ("magnifying-glass", "OpenVAS", "Vuln Scanner"),
            ("terminal-window", "TheHive", "Case Management"),
            ("gear-six", "Shuffle", "SOAR Automation"),
            ("chart-line-up", "Grafana", "Dashboards"),
            ("lock", "pfSense", "Firewall"),
            ("network", "DigitalOcean", "Cloud Hosting"),
        ]
        for icon, name, desc in tools:
            stack_html += (
                f'<div style="display:flex;align-items:center;gap:10px;padding:8px 0;'
                f'border-bottom:1px solid {COLORS["divider"]};">'
                f'<i class="ph-duotone ph-{icon}" style="font-size:20px;color:{COLORS["brand"]};"></i>'
                f'<div><span style="font-family:Plus Jakarta Sans,sans-serif;font-size:13px;'
                f'font-weight:600;color:{COLORS["heading"]};">{name}</span>'
                f'<span style="font-family:Plus Jakarta Sans,sans-serif;font-size:12px;'
                f'color:{COLORS["muted"]};margin-left:8px;">{desc}</span></div></div>'
            )
        st.markdown(f'<div style="margin-top:8px;">{stack_html}</div>', unsafe_allow_html=True)

    st.markdown("")
    section_tag("03", "New Annual Operating Cost")

    st.markdown(
        "Automation replaces 5 of 9 staff members. Wazuh handles log review, "
        "Zabbix monitors networks, Shuffle automates alert triage. The remaining "
        "team of 4 focuses on advanced analysis and client relationships."
    )

    # New staffing
    st.markdown("**Reduced Team (₹33.5L, down from ₹58.0L)**")
    staff_after = pd.DataFrame([
        {"Role": "SOC Manager / Lead", "Count": 1, "Monthly (₹)": "90,000", "Annual with Overhead (₹)": "14.04L"},
        {"Role": "L2 Security Analyst", "Count": 1, "Monthly (₹)": "55,000", "Annual with Overhead (₹)": "8.58L"},
        {"Role": "L1 Junior Analyst / VAPT", "Count": 2, "Monthly (₹)": "35,000 each", "Annual with Overhead (₹)": "10.92L"},
    ])
    st.dataframe(staff_after, use_container_width=True, hide_index=True)

    # Before vs After comparison
    st.markdown("")
    before_after(
        before={"value": "₹90.0L / yr", "items": [
            "9 staff members",
            "Manual log review daily",
            "Quarterly vulnerability scans",
            "247 min avg response time",
            "8% client incident rate",
        ]},
        after={"value": "₹59.8L / yr", "items": [
            "4 staff members",
            "Automated 24/7 monitoring",
            "Weekly automated scans",
            "12 min avg response time",
            "~2% projected incident rate",
        ]},
    )

    stat_row([
        {"value": "₹30.2", "unit": "L", "label": "Annual savings", "color": COLORS["success"]},
        {"value": "5", "label": "Staff positions automated", "color": COLORS["brand"]},
        {"value": "95", "unit": "%", "label": "Response time reduction", "color": COLORS["brand"]},
        {"value": "24", "unit": "mo", "label": "Estimated breakeven", "color": COLORS["heading"]},
    ])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3: 5-Year Projection
# ══════════════════════════════════════════════════════════════════════════════
with tab_projection:
    section_tag("04", "Financial Trajectory Over 5 Years")

    st.markdown(
        "Manual operating costs grow at roughly 8% per year (salary hikes, rent increases, "
        "inflation). Cloud platform costs grow at only 3% (infrastructure scaling). This "
        "widening gap means savings compound each year."
    )

    # Calculate projections
    manual_growth = 0.08
    cloud_growth = 0.03
    investment = 60.0
    manual_base = 90.0
    cloud_base = 59.8

    rows = []
    cumulative_net = -investment
    for yr in range(6):
        manual_cost = manual_base * (1 + manual_growth) ** yr
        cloud_cost = cloud_base * (1 + cloud_growth) ** yr
        annual_saving = manual_cost - cloud_cost
        if yr == 0:
            cumulative_net = -investment
            rows.append({
                "Year": f"Year 0 (Investment)",
                "Manual Cost (₹L)": f"{manual_cost:.1f}",
                "Cloud Cost (₹L)": f"{cloud_cost:.1f}",
                "Annual Saving (₹L)": "--",
                "Cumulative (₹L)": f"{cumulative_net:.1f}",
            })
        else:
            cumulative_net += annual_saving
            rows.append({
                "Year": f"Year {yr}",
                "Manual Cost (₹L)": f"{manual_cost:.1f}",
                "Cloud Cost (₹L)": f"{cloud_cost:.1f}",
                "Annual Saving (₹L)": f"{annual_saving:.1f}",
                "Cumulative (₹L)": f"{cumulative_net:+.1f}",
            })

    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    # Chart: dual line (manual vs cloud) + cumulative bar
    years = list(range(6))
    manual_costs = [manual_base * (1 + manual_growth) ** y for y in years]
    cloud_costs = [cloud_base * (1 + cloud_growth) ** y for y in years]
    savings = [m - c for m, c in zip(manual_costs, cloud_costs)]

    cum = -investment
    cumulative = [cum]
    for s in savings[1:]:
        cum += s
        cumulative.append(cum)

    year_labels = ["Year 0", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=year_labels, y=manual_costs, mode="lines+markers", name="Manual Ops (would-be cost)",
        line=dict(color=COLORS["danger"], width=2.5, dash="dot"),
        marker=dict(size=7),
    ))

    fig.add_trace(go.Scatter(
        x=year_labels, y=cloud_costs, mode="lines+markers", name="Cloud Platform (actual cost)",
        line=dict(color=COLORS["brand"], width=2.5),
        marker=dict(size=7),
    ))

    fig.add_trace(go.Bar(
        x=year_labels[1:], y=cumulative[1:], name="Cumulative Net (after ₹60L investment)",
        marker_color=[COLORS["danger"] if v < 0 else COLORS["success"] for v in cumulative[1:]],
        opacity=0.7,
    ))

    fig.add_hline(y=0, line_dash="dash", line_color=COLORS["muted"], line_width=1)

    apply_theme(fig,
        title=dict(text="5-Year Cost Comparison and Cumulative Return"),
        xaxis_title="", yaxis_title="₹ Lakhs",
        height=420, barmode="overlay",
        legend=dict(x=0.01, y=0.99, bgcolor="rgba(255,255,255,0.85)"),
    )
    show(fig)

    # Key takeaways
    callout(
        f"By Year 5, manual operations would cost ₹{manual_costs[5]:.1f}L annually. "
        f"The cloud platform costs just ₹{cloud_costs[5]:.1f}L. The widening gap of "
        f"₹{savings[5]:.1f}L per year means cumulative net benefit reaches "
        f"₹{cumulative[5]:+.1f}L, delivering a {((cumulative[5] + investment) / investment * 100):.0f}% "
        f"total return on the original ₹60L investment.",
        icon="trend-up", variant="success",
    )

    # Revenue context
    st.markdown("")
    section_tag("05", "Revenue Context")

    st.markdown(
        "SecureNet earns approximately ₹1.74 crore annually from 50 clients across "
        "three pricing tiers (Basic at ₹17,500/mo, Standard at ₹30,000/mo, Premium at "
        "₹50,000/mo). The ₹60L investment represents 34.5% of one year's revenue."
    )

    rev_df = pd.DataFrame([
        {"Tier": "Basic", "Clients": 20, "Monthly Fee (₹)": "17,500", "Annual Revenue (₹L)": "42.0"},
        {"Tier": "Standard", "Clients": 20, "Monthly Fee (₹)": "30,000", "Annual Revenue (₹L)": "72.0"},
        {"Tier": "Premium", "Clients": 10, "Monthly Fee (₹)": "50,000", "Annual Revenue (₹L)": "60.0"},
        {"Tier": "Total", "Clients": 50, "Monthly Fee (₹)": "29,000 avg", "Annual Revenue (₹L)": "174.0"},
    ])
    st.dataframe(rev_df, use_container_width=True, hide_index=True)

    callout(
        "With reduced operating costs (₹59.8L vs ₹90L), net profit margin improves "
        "from ~48% to ~63%. The automated platform also enables scaling to 80-100 clients "
        "without proportionally adding staff, unlocking a growth path that manual operations "
        "could never support.",
        icon="chart-line-up", variant="success",
    )
