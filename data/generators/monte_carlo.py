"""Monte Carlo simulation for investment ROI analysis."""

import numpy as np
import pandas as pd

from config.constants import (
    ANNUAL_OPERATIONAL_COST,
    ESTIMATED_ANNUAL_LOSSES,
    PROPOSED_INVESTMENT,
)


def run_monte_carlo(
    n_simulations: int = 10_000,
    years: int = 3,
    seed: int | None = None,
) -> pd.DataFrame:
    """Simulate ROI under uncertainty.

    Varies per simulation:
        - Incident handling cost reduction : Uniform(25%, 55%)
        - Security loss reduction          : Uniform(35%, 65%)
        - Annual cost growth rate          : Normal(5%, 1.5%)
        - Attack frequency growth          : Normal(10%, 10%)

    Returns a long-form DataFrame with one row per (simulation, year).
    """
    rng = np.random.default_rng(seed)

    handling_red = rng.uniform(0.25, 0.55, n_simulations)
    loss_red = rng.uniform(0.35, 0.65, n_simulations)
    cost_growth = rng.normal(0.05, 0.015, n_simulations)
    attack_growth = rng.normal(0.10, 0.10, n_simulations)

    frames = []
    cumulative = np.zeros(n_simulations)

    for yr in range(1, years + 1):
        adj_op = ANNUAL_OPERATIONAL_COST * (1 + cost_growth) ** (yr - 1)
        adj_loss = ESTIMATED_ANNUAL_LOSSES * (1 + attack_growth) ** (yr - 1)

        annual_savings = adj_op * handling_red + adj_loss * loss_red
        cumulative = cumulative + annual_savings
        net_benefit = cumulative - PROPOSED_INVESTMENT

        frames.append(pd.DataFrame({
            "year": yr,
            "sim": np.arange(n_simulations),
            "handling_reduction_pct": (handling_red * 100).round(1),
            "loss_reduction_pct": (loss_red * 100).round(1),
            "annual_savings": annual_savings.round(0),
            "cumulative_savings": cumulative.round(0),
            "net_benefit": net_benefit.round(0),
        }))

    return pd.concat(frames, ignore_index=True)
