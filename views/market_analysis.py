"""Market Analysis - connecting the SecureNet case study to Business Studies theory."""

import streamlit as st

from config.constants import COMPANY_SHORT, PROPOSED_INVESTMENT, ANNUAL_OPERATIONAL_COST
from utils.formatters import fmt_lakhs


# ── Header ───────────────────────────────────────────────────────────────────
st.header("Market Analysis")

st.markdown(
    "Cybersecurity is no longer a purely technical concern. It sits at the "
    "intersection of legal compliance, economic strategy, and organisational "
    "behaviour. This section connects the investment decision facing "
    f"{COMPANY_SHORT} to established frameworks from the Business Studies "
    "curriculum, showing how theoretical concepts apply to a real commercial "
    "problem."
)

# ── Tabs ─────────────────────────────────────────────────────────────────────
tab_env, tab_plan, tab_fin, tab_behav = st.tabs([
    "Business Environment",
    "Planning and Controlling",
    "Financial Perspective",
    "Behavioral Economics",
])

# ── Tab 1: Business Environment ──────────────────────────────────────────────
with tab_env:
    st.subheader("External Forces Shaping Cybersecurity Demand")

    st.markdown(
        "The technological dimension of the business environment has shifted "
        "dramatically in the last decade. India added roughly 350 million "
        "internet users between 2018 and 2024, and small enterprises that once "
        "operated offline now depend on cloud-hosted ERP, payment gateways, and "
        "remote-access tools. Every new digital surface is a potential attack "
        "vector. According to CERT-In, reported cyber incidents in India rose "
        "from about 3.94 lakh in 2019 to over 15.9 lakh in 2023, a compounding "
        "rate that shows no sign of slowing."
    )

    st.markdown(
        "The legal environment adds further pressure. The Information Technology "
        "Act, 2000, and its 2008 amendments impose penalties for negligent handling "
        "of personal data. Companies serving European clients must also account "
        "for GDPR requirements, where non-compliance fines can reach 4% of "
        "global turnover. India's own Digital Personal Data Protection Act (2023) "
        "introduces consent-based processing rules and mandatory breach "
        "notifications. For a managed-security provider like SecureNet, these "
        "laws are not abstract; they define the minimum standard of care its "
        "clients expect."
    )

    st.markdown(
        "From an economic standpoint, the cost of data breaches in India averaged "
        "roughly 17.9 crore per incident in 2023, per the IBM Cost of a Data "
        "Breach report. The domestic cybersecurity market itself is expanding at "
        "an estimated 15.3% CAGR and is projected to cross $6.2 billion by 2027. "
        "These numbers signal that demand for monitoring services is structural, "
        "not cyclical, and that firms who invest early build a lasting cost "
        "advantage over late movers."
    )

# ── Tab 2: Planning and Controlling ──────────────────────────────────────────
with tab_plan:
    st.subheader("The Investment as a Planning Decision")

    st.markdown(
        f"In management theory, planning involves setting objectives, identifying "
        f"alternatives, and choosing a course of action. {COMPANY_SHORT}'s "
        f"proposal to spend {fmt_lakhs(PROPOSED_INVESTMENT)} on a cloud monitoring "
        f"platform is a single-use plan: a one-time budgetary commitment directed "
        f"at a specific objective (reducing incident handling costs and breach "
        f"losses). The decision follows the rational planning model. Management "
        f"identified the problem (rising costs, slow response times), evaluated "
        f"alternatives (continue manual processes, outsource, or build in-house), "
        f"and selected the option with the most favourable cost-benefit profile."
    )

    st.markdown(
        "The plan operates at both the strategic and operational levels. "
        "Strategically, it repositions the company from a reactive service "
        "provider to a proactive monitoring partner. Operationally, it replaces "
        "manual log review with automated anomaly detection and cuts the mean "
        "response window from roughly four hours to twelve minutes. The budget "
        "itself functions as a derivative plan, translating the strategic "
        "objective into concrete financial terms."
    )

    st.subheader("The Monitoring System as a Controlling Mechanism")

    st.markdown(
        "Controlling, as defined by Koontz and O'Donnell, involves measuring "
        "actual performance against standards and correcting deviations. The "
        "proposed monitoring system embeds every step of the controlling process "
        "into a technical workflow. Standards are encoded as detection rules and "
        "threshold alerts. Actual performance is continuously measured through "
        "real-time log ingestion and network traffic analysis. When a deviation "
        "occurs, say a login anomaly or an unusual data exfiltration pattern, "
        "the system raises an alert and can trigger automated containment."
    )

    st.markdown(
        "This makes the feedback loop nearly instantaneous, which is the ideal "
        "that traditional controlling frameworks aspire to but rarely achieve "
        "in manual environments. Dashboards give management a bird's-eye view "
        "of incident trends, allowing them to spot systemic weaknesses rather "
        "than reacting to individual events."
    )

# ── Tab 3: Financial Perspective ─────────────────────────────────────────────
with tab_fin:
    st.subheader("Capital Budgeting and the Investment Decision")

    st.markdown(
        f"From a financial management standpoint, the {fmt_lakhs(PROPOSED_INVESTMENT)} "
        f"deployment is a capital budgeting decision. The firm must evaluate "
        f"whether the expected future cash inflows (cost savings and loss "
        f"reductions) justify the present outlay. Techniques such as Net Present "
        f"Value and Payback Period apply directly. The Monte Carlo analysis on "
        f"the Risk Simulation page estimates the payback at approximately 15.7 "
        f"months, well within the three-year planning horizon."
    )

    st.markdown(
        "Financing the investment is equally important. SecureNet could fund it "
        "through retained earnings (internal accrual), avoiding dilution and "
        "interest costs but reducing its liquidity buffer. Alternatively, a "
        "term loan from a commercial bank at prevailing rates of 10 to 12% "
        "would preserve cash reserves but add a fixed interest obligation. "
        "Equity financing, perhaps from a seed-stage cybersecurity fund, would "
        "bring capital and strategic connections but dilute founder control. "
        "Given the relatively modest size of the investment and the firm's "
        f"existing annual spend of {fmt_lakhs(ANNUAL_OPERATIONAL_COST)}, internal "
        "accrual supplemented by a short-term credit facility appears most "
        "practical."
    )

    st.markdown(
        "The risk-return tradeoff is asymmetric in this case. If the system "
        "works as projected, the firm saves 46 lakhs per year and hardens its "
        "competitive position. If it underperforms, the downside is limited to "
        "the sunk cost of 60 lakhs, partially recoverable through resale or "
        "repurposing of infrastructure. This asymmetry aligns with the wealth "
        "maximisation objective: the expected value of acting substantially "
        "exceeds the expected value of inaction."
    )

# ── Tab 4: Behavioral Economics ──────────────────────────────────────────────
with tab_behav:
    st.subheader("Why Small Firms Underinvest in Security")

    st.markdown(
        "Behavioral economics offers a useful lens for understanding why many "
        "of SecureNet's own clients, and firms like them, resist spending on "
        "cybersecurity until after a breach has occurred. Three cognitive biases "
        "are particularly relevant."
    )

    st.markdown(
        "Optimism bias leads decision-makers to believe that attacks happen to "
        "other companies, not theirs. A 2023 survey by DSCI found that 61.4% "
        "of Indian SME owners rated their cyber risk as 'low' or 'very low,' "
        "even though roughly one in five had experienced an incident in the "
        "prior twelve months. Present bias compounds the problem. Security "
        "spending is a cost incurred today for a benefit that may never be "
        "visible, since a prevented attack produces no dramatic evidence of "
        "its own prevention. Faced with a choice between spending 60 lakhs now "
        "or hoping nothing goes wrong, the status quo feels safer. Status quo "
        "bias itself reinforces this inertia: the current antivirus and "
        "firewall setup has 'worked so far,' so changing it feels like "
        "unnecessary disruption."
    )

    st.subheader("Nudges and Framing Strategies")

    st.markdown(
        "SecureNet can design its sales and onboarding process to counteract "
        "these biases. Offering a 30-day free trial with real-time dashboards "
        "makes the value of monitoring tangible before any payment is required, "
        "reducing the perceived risk of adoption. Presenting breach statistics "
        "specific to the client's industry, say 'healthcare firms in India "
        "faced an average breach cost of 2.1 crore in 2023,' reframes the "
        "decision from optional to urgent. Setting monitoring to default-on "
        "during onboarding exploits the default effect: clients who would not "
        "actively opt in will rarely opt out of a service already running and "
        "delivering visible alerts."
    )

    st.markdown(
        "These approaches draw on Thaler and Sunstein's nudge framework, where "
        "choice architecture steers decisions without restricting freedom. For "
        "SecureNet, applying behavioral insights is not just a marketing tactic "
        "but a way to close the gap between what clients need and what they "
        "would choose on their own."
    )
