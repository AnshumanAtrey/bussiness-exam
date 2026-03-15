"""Monte Carlo ROI simulation for the SecureNet cybersecurity investment."""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from components.metric_card import metric_row
from components.chart_builders import apply_theme, show
from config.theme import COLORS, CHART_COLORS
from data.generators.monte_carlo import run_monte_carlo
from utils.formatters import fmt_lakhs, fmt_pct


# ── Header ───────────────────────────────────────────────────────────────────
st.header("Risk Simulation")

st.markdown(
    "Monte Carlo simulation varies key assumptions across thousands of "
    "scenarios to assess the probability of achieving a positive return on "
    "investment. By randomising cost reductions, breach severity, and growth "
    "rates, the model produces a distribution of outcomes rather than a single "
    "point estimate."
)

# ── Controls ─────────────────────────────────────────────────────────────────
col_sims, col_years, col_btn = st.columns([2, 2, 1])

with col_sims:
    n_sims = st.slider("Number of simulations", 1000, 30000, 10000, step=1000)
with col_years:
    n_years = st.slider("Projection years", 1, 5, 3)
with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("Run Simulation")


# ── Cached runner ────────────────────────────────────────────────────────────
@st.cache_data(show_spinner="Simulating scenarios...")
def _run(n_simulations: int, years: int):
    return run_monte_carlo(n_simulations=n_simulations, years=years, seed=42)


# Persist results across reruns
if run_btn:
    st.session_state["mc_df"] = _run(n_sims, n_years)
    st.session_state["mc_years"] = n_years

if "mc_df" not in st.session_state:
    st.info("Adjust the parameters above and press Run Simulation to begin.")
    st.stop()

df = st.session_state["mc_df"]
years_used = st.session_state["mc_years"]

# ── Last-year slice ──────────────────────────────────────────────────────────
last_year = df[df["year"] == years_used]
positive_pct = (last_year["net_benefit"] > 0).sum() / len(last_year) * 100
median_nb = last_year["net_benefit"].median()
p5_nb = np.percentile(last_year["net_benefit"], 5)

metric_row([
    {"icon": "dice-five", "label": f"Positive ROI (Year {years_used})",
     "value": fmt_pct(positive_pct), "delta": f"{(last_year['net_benefit'] > 0).sum():,} of {len(last_year):,} runs",
     "delta_color": COLORS["success"]},
    {"icon": "chart-line-up", "label": "Median Net Benefit",
     "value": fmt_lakhs(median_nb),
     "delta": f"Year {years_used} cumulative", "delta_color": COLORS["success"]},
    {"icon": "shield-warning", "label": "5th Percentile (Worst Case)",
     "value": fmt_lakhs(p5_nb),
     "delta": "Bottom 5% of outcomes"},
])

st.divider()

# ── Histogram ────────────────────────────────────────────────────────────────
st.subheader("Net Benefit Distribution")

nb_vals = last_year["net_benefit"].values

fig = go.Figure()
fig.add_trace(go.Histogram(
    x=nb_vals[nb_vals >= 0], nbinsx=50,
    marker_color=COLORS["success"], opacity=0.85, name="Positive",
))
fig.add_trace(go.Histogram(
    x=nb_vals[nb_vals < 0], nbinsx=20,
    marker_color=COLORS["danger"], opacity=0.85, name="Negative",
))
fig.add_vline(x=0, line_width=2, line_dash="dash", line_color=COLORS["muted"])

apply_theme(fig,
    barmode="overlay",
    xaxis_title="Net Benefit (INR)",
    yaxis_title="Frequency",
    title=f"Year {years_used} Net Benefit across {len(last_year):,} Simulations",
)
show(fig)

# ── Year-by-year summary table ───────────────────────────────────────────────
st.subheader("Results by Year")

summary_rows = []
for yr in sorted(df["year"].unique()):
    slice_yr = df[df["year"] == yr]
    summary_rows.append({
        "Year": yr,
        "Positive ROI (%)": round((slice_yr["net_benefit"] > 0).sum() / len(slice_yr) * 100, 1),
        "Mean Annual Savings": fmt_lakhs(slice_yr["annual_savings"].mean()),
        "Median Net Benefit": fmt_lakhs(slice_yr["net_benefit"].median()),
    })

st.dataframe(pd.DataFrame(summary_rows), use_container_width=True, hide_index=True)

st.markdown(
    "The simulation accounts for variability in cost reduction efficiency "
    "(25% to 55% for handling, 35% to 65% for losses), annual cost growth "
    "around 5%, and attack frequency growth around 10%. These ranges reflect "
    "plausible real-world uncertainty rather than best-case assumptions."
)
