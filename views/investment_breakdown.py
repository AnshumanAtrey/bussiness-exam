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
# TAB 3: 5-Year Projection (with client growth)
# ══════════════════════════════════════════════════════════════════════════════
with tab_projection:
    section_tag("04", "Financial Trajectory Over 5 Years")

    st.markdown(
        "The real power of automation is not just cost savings on existing clients. "
        "With a cloud platform in place, adding a new client costs almost nothing: "
        "deploy Wazuh agents, add to Zabbix, onboard in a day. No new hires needed. "
        "In the manual model, every 12-15 new clients would require another L1 analyst."
    )

    # ── Growth assumptions ──
    investment = 60.0
    avg_revenue_per_client = 3.48  # ₹29K/mo * 12 = ₹3.48L/year

    # Client growth: improved service reputation + freed-up sales capacity
    clients_by_year = [50, 55, 62, 70, 78, 85]

    # Manual model: ₹90L base for 50 clients, grows 8%/yr for inflation,
    # PLUS need 1 new L1 analyst (₹4.68L/yr with overhead) per ~13 new clients
    manual_base = 90.0
    manual_cost_per_new_hire = 4.68  # L1 at ₹30K/mo + 30% overhead

    # Cloud model: ₹59.8L base for 50 clients, grows 3%/yr for infra,
    # PLUS ~₹0.24L per new client (hosting + onboarding amortized)
    # Hire 1 more L1 (₹5.46L/yr) only when crossing 80 clients (Year 4-5)
    cloud_base = 59.8
    cloud_cost_per_new_client = 0.24  # ₹2K/mo hosting per client
    cloud_new_hire_cost = 5.46  # L1 at ₹35K/mo + 30% overhead
    cloud_hire_threshold = 80  # need 5th person above this

    rows = []
    cumulative_net = -investment

    for yr in range(6):
        clients = clients_by_year[yr]
        new_clients = clients - 50
        revenue = clients * avg_revenue_per_client

        # Manual path: base cost with inflation + extra hires for growth
        manual_inflation = manual_base * (1.08 ** yr)
        manual_extra_hires = max(0, (new_clients // 13)) * manual_cost_per_new_hire
        manual_cost = manual_inflation + manual_extra_hires

        # Cloud path: base cost with small inflation + marginal client cost
        cloud_inflation = cloud_base * (1.03 ** yr)
        cloud_marginal = new_clients * cloud_cost_per_new_client
        cloud_extra_hire = cloud_new_hire_cost if clients > cloud_hire_threshold else 0
        cloud_cost = cloud_inflation + cloud_marginal + cloud_extra_hire

        annual_saving = manual_cost - cloud_cost
        profit_cloud = revenue - cloud_cost

        if yr == 0:
            cumulative_net = -investment
            rows.append({
                "Year": "Year 0",
                "Clients": clients,
                "Revenue (₹L)": f"{revenue:.1f}",
                "Manual Cost (₹L)": f"{manual_cost:.1f}",
                "Cloud Cost (₹L)": f"{cloud_cost:.1f}",
                "Saving (₹L)": "--",
                "Net Profit (₹L)": f"{profit_cloud:.1f}",
            })
        else:
            cumulative_net += annual_saving
            rows.append({
                "Year": f"Year {yr}",
                "Clients": clients,
                "Revenue (₹L)": f"{revenue:.1f}",
                "Manual Cost (₹L)": f"{manual_cost:.1f}",
                "Cloud Cost (₹L)": f"{cloud_cost:.1f}",
                "Saving (₹L)": f"{annual_saving:.1f}",
                "Net Profit (₹L)": f"{profit_cloud:.1f}",
            })

    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    callout(
        "In the manual model, going from 50 to 85 clients requires hiring ~3 more L1 analysts "
        "(₹14L/yr extra). In the cloud model, the same growth adds only ₹8.4L/yr in hosting "
        "plus one junior hire at ₹5.5L when crossing 80 clients. The marginal cost of a new "
        "client drops from ~₹1.8L/yr (manual) to ~₹0.24L/yr (cloud).",
        icon="buildings", variant="brand",
    )

    # ── Charts ──
    st.markdown("")

    # Recompute for charts
    revenues = [c * avg_revenue_per_client for c in clients_by_year]
    manual_costs_arr = []
    cloud_costs_arr = []
    for yr in range(6):
        nc = clients_by_year[yr] - 50
        m = manual_base * (1.08 ** yr) + max(0, nc // 13) * manual_cost_per_new_hire
        c = cloud_base * (1.03 ** yr) + nc * cloud_cost_per_new_client
        if clients_by_year[yr] > cloud_hire_threshold:
            c += cloud_new_hire_cost
        manual_costs_arr.append(m)
        cloud_costs_arr.append(c)

    profits = [r - c for r, c in zip(revenues, cloud_costs_arr)]
    year_labels = [f"Year {i}" for i in range(6)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=year_labels, y=revenues, mode="lines+markers", name="Revenue (with client growth)",
        line=dict(color=CHART_COLORS[1], width=2.5),
        marker=dict(size=7), fill="tozeroy", fillcolor="rgba(43,108,176,0.06)",
    ))

    fig.add_trace(go.Scatter(
        x=year_labels, y=manual_costs_arr, mode="lines+markers",
        name="Manual cost (would-be, with hiring)",
        line=dict(color=COLORS["danger"], width=2, dash="dot"),
        marker=dict(size=6),
    ))

    fig.add_trace(go.Scatter(
        x=year_labels, y=cloud_costs_arr, mode="lines+markers",
        name="Cloud cost (actual, scales flat)",
        line=dict(color=COLORS["brand"], width=2.5),
        marker=dict(size=7),
    ))

    apply_theme(fig,
        title=dict(text="Revenue, Manual Cost, and Cloud Cost as Clients Grow"),
        xaxis_title="", yaxis_title="₹ Lakhs", height=400,
        legend=dict(x=0.01, y=0.99, bgcolor="rgba(255,255,255,0.85)"),
    )
    show(fig)

    # Client growth + profit chart
    fig2 = go.Figure()

    fig2.add_trace(go.Bar(
        x=year_labels, y=[c for c in clients_by_year], name="Clients",
        marker_color=COLORS["brand"], opacity=0.3, yaxis="y2",
    ))

    fig2.add_trace(go.Scatter(
        x=year_labels, y=profits, mode="lines+markers+text", name="Net Profit",
        line=dict(color=COLORS["success"], width=3),
        marker=dict(size=8),
        text=[f"₹{p:.0f}L" for p in profits],
        textposition="top center",
        textfont=dict(size=11, color=COLORS["success"]),
    ))

    apply_theme(fig2,
        title=dict(text="Client Growth and Net Profit Trajectory"),
        xaxis_title="", height=360,
        yaxis=dict(title="Net Profit (₹L)", gridcolor=COLORS["divider"]),
        yaxis2=dict(title="Clients", overlaying="y", side="right",
                    showgrid=False, range=[0, 120]),
        legend=dict(x=0.01, y=0.99, bgcolor="rgba(255,255,255,0.85)"),
    )
    show(fig2)

    # Final summary stats
    stat_row([
        {"value": "50", "unit": "to 85", "label": "Client growth over 5 years", "color": COLORS["brand"]},
        {"value": f"₹{revenues[5]:.0f}", "unit": "L", "label": f"Year 5 revenue ({clients_by_year[5]} clients)", "color": COLORS["info"]},
        {"value": f"₹{profits[5]:.0f}", "unit": "L", "label": "Year 5 net profit", "color": COLORS["success"]},
        {"value": f"₹{cloud_costs_arr[5]:.0f}", "unit": "L", "label": "Year 5 operating cost", "color": COLORS["heading"]},
    ])

    callout(
        f"Revenue grows from ₹{revenues[0]:.0f}L to ₹{revenues[5]:.0f}L (+{((revenues[5]/revenues[0]-1)*100):.0f}%) "
        f"as clients increase from 50 to 85. Operating cost barely moves from ₹{cloud_costs_arr[0]:.1f}L to "
        f"₹{cloud_costs_arr[5]:.1f}L (+{((cloud_costs_arr[5]/cloud_costs_arr[0]-1)*100):.0f}%). This operating leverage "
        f"is the fundamental advantage of an automated platform over manual operations, where every "
        f"new client requires proportional headcount growth.",
        icon="trend-up", variant="success",
    )
