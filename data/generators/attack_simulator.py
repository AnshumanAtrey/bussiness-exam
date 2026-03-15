"""Generate client profiles and historical attack data."""

from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from config.constants import (
    ATTACK_DISTRIBUTION,
    CLIENT_INDUSTRIES,
    SEVERITY_LEVELS,
    SEVERITY_WEIGHTS,
    TOTAL_CLIENTS,
)

_NAMES = [
    "Apex Solutions", "Nova Industries", "Peak Services", "Zenith Tech",
    "Atlas Enterprises", "Vertex Global", "Prism Systems", "Orbit Corp",
    "Nexus Labs", "Pulse Infra", "Surge Solutions", "Crest Industries",
    "Flux Services", "Core Tech", "Bridge Enterprises", "Wave Global",
    "Grid Systems", "Link Corp", "Spark Labs", "Forge Infra",
    "Astra Solutions", "Veda Industries", "Disha Services", "Kavach Tech",
    "Sutra Enterprises", "Yantra Global", "Netra Systems", "Manthan Corp",
    "Pragati Labs", "Sankalp Infra", "Dhruv Solutions", "Akash Industries",
    "Vyom Services", "Taksh Tech", "Bodhi Enterprises", "Nirmaan Global",
    "Kiran Systems", "Pushp Corp", "Saral Labs", "Sthir Infra",
    "Daksh Solutions", "Agni Industries", "Veer Services", "Lakshya Tech",
    "Sakha Enterprises", "Udaan Global", "Vayu Systems", "Jyoti Corp",
    "Chintan Labs", "Sampark Infra",
]


def generate_client_profiles(seed: int = 42) -> pd.DataFrame:
    """Create profiles for 50 client companies with risk scores."""
    rng = np.random.default_rng(seed)

    industries = rng.choice(CLIENT_INDUSTRIES, size=TOTAL_CLIENTS)
    employees = rng.choice([10, 15, 20, 25, 30, 40, 50, 75, 100, 150], size=TOTAL_CLIENTS)
    sec_levels = rng.choice([1, 2, 3, 4, 5], size=TOTAL_CLIENTS, p=[0.10, 0.30, 0.35, 0.18, 0.07])
    risk = np.clip(100 - sec_levels * 15 + rng.normal(0, 8, TOTAL_CLIENTS), 12, 97).round(1)
    incidents = rng.binomial(3, np.clip((5 - sec_levels) * 0.08, 0.02, 0.35))

    df = pd.DataFrame({
        "client_name": _NAMES[:TOTAL_CLIENTS],
        "industry": industries,
        "employees": employees,
        "security_level": sec_levels,
        "risk_score": risk,
        "incidents_last_year": incidents,
    })
    return df.sort_values("risk_score", ascending=False).reset_index(drop=True)


def generate_attack_history(n_events: int = 800, seed: int = 42) -> pd.DataFrame:
    """Generate historical attack events weighted toward higher-risk clients."""
    rng = np.random.default_rng(seed)
    clients = generate_client_profiles(seed)

    weights = clients["risk_score"].values
    weights = weights / weights.sum()
    idxs = rng.choice(len(clients), size=n_events, p=weights)

    atk_types = list(ATTACK_DISTRIBUTION.keys())
    atk_weights = list(ATTACK_DISTRIBUTION.values())

    base = datetime(2025, 1, 1)
    days = np.sort(rng.integers(0, 365, size=n_events))
    dates = [base + timedelta(days=int(d)) for d in days]

    outcomes = rng.choice(
        ["Blocked", "Mitigated", "Breach", "False Positive"],
        size=n_events,
        p=[0.45, 0.30, 0.10, 0.15],
    )
    losses = np.where(
        outcomes == "Breach",
        rng.integers(50_000, 20_00_000, size=n_events),
        0,
    )

    df = pd.DataFrame({
        "date": dates,
        "client_name": clients.iloc[idxs]["client_name"].values,
        "industry": clients.iloc[idxs]["industry"].values,
        "attack_type": rng.choice(atk_types, size=n_events, p=atk_weights),
        "severity": rng.choice(SEVERITY_LEVELS, size=n_events, p=SEVERITY_WEIGHTS),
        "outcome": outcomes,
        "response_time_min": np.clip(rng.lognormal(3.5, 1.0, n_events), 5, 1200).astype(int),
        "estimated_loss_inr": losses,
    })
    return df
