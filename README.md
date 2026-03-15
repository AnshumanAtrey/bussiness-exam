# SecureNet Technologies - Cloud Cybersecurity Monitoring Dashboard

Streamlit web application for **Case Study 27: Cloud Cybersecurity Monitoring Service** at SecureNet Technologies Pvt. Ltd., Mumbai.

Built for the Business Studies examination (AY 2025-26).

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```
exam-bussiness/
├── app.py                              # Entry point, page routing, theme init
├── requirements.txt                    # Python dependencies
├── .streamlit/
│   └── config.toml                     # Streamlit theme (colors, fonts)
│
├── config/                             # App-wide configuration
│   ├── constants.py                    # Case study numbers (90L, 60L, 50 clients, 8%)
│   ├── theme.py                        # Design system (colors, fonts, spacing, shadows, logo SVG)
│   └── logging_config.py              # Centralized Python logging
│
├── components/                         # Reusable UI components
│   ├── css_loader.py                   # Injects custom CSS + Phosphor Icons CDN
│   ├── metric_card.py                  # Styled metric cards with Phosphor duotone icons
│   ├── chart_builders.py              # Plotly chart factories with consistent theming
│   └── sidebar.py                      # Sidebar logo and branding
│
├── data/
│   └── generators/                     # Synthetic data generation
│       ├── log_simulator.py            # Security log entries (batch + real-time streaming)
│       ├── attack_simulator.py         # 50 client profiles + 800 historical attack events
│       └── monte_carlo.py              # 10,000-scenario ROI simulation engine
│
├── utils/                              # Helper functions
│   ├── calculations.py                 # Financial formulas (savings, ROI, breakeven)
│   └── formatters.py                   # INR formatting, Lakhs, percentages
│
├── views/                              # Dashboard pages
│   ├── executive_summary.py            # Landing page with key metrics
│   ├── cost_benefit.py                 # Interactive sliders, breakeven chart (Q1, Q2)
│   ├── live_simulator.py              # Real-time threat feed with @st.fragment (Q4)
│   ├── threat_dashboard.py            # Attack analysis, client risk, system features (Q3, Q5)
│   ├── monte_carlo.py                 # Probabilistic ROI simulation
│   ├── market_analysis.py             # Business Studies theory connections
│   └── recommendation.py             # Final investment verdict + timeline
│
├── assets/
│   └── styles.css                      # Custom CSS (Space Grotesk headings, animations)
│
├── PS.txt                              # Original case study problem statement
├── Business Studies.pdf               # Course curriculum
└── BUSINESS STUDIES NOTES.pdf         # Theoretical notes reference
```
