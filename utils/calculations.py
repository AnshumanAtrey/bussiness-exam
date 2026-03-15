"""Financial formulas for the cost-benefit analysis."""

from config.constants import (
    ANNUAL_OPERATIONAL_COST,
    ESTIMATED_ANNUAL_LOSSES,
    PROPOSED_INVESTMENT,
)


def calculate_annual_savings(
    handling_reduction: float = 0.40,
    loss_reduction: float = 0.50,
    op_cost: float = ANNUAL_OPERATIONAL_COST,
    losses: float = ESTIMATED_ANNUAL_LOSSES,
) -> dict:
    handling = op_cost * handling_reduction
    loss_sav = losses * loss_reduction
    return {
        "handling_savings": handling,
        "loss_savings": loss_sav,
        "total_savings": handling + loss_sav,
    }


def calculate_net_benefit(total_savings: float, investment: float = PROPOSED_INVESTMENT) -> float:
    return total_savings - investment


def calculate_breakeven_months(annual_savings: float, investment: float = PROPOSED_INVESTMENT) -> float:
    if annual_savings <= 0:
        return float("inf")
    return investment / (annual_savings / 12)


def calculate_roi_percentage(annual_savings: float, investment: float = PROPOSED_INVESTMENT) -> float:
    if investment == 0:
        return 0.0
    return ((annual_savings - investment) / investment) * 100


def calculate_cumulative_savings(
    annual_savings: float,
    years: int = 5,
    investment: float = PROPOSED_INVESTMENT,
) -> list[dict]:
    rows = []
    cumulative = 0.0
    for y in range(1, years + 1):
        cumulative += annual_savings
        net = cumulative - investment
        rows.append({
            "year": y,
            "cumulative_savings": cumulative,
            "net_benefit": net,
            "breakeven_reached": net >= 0,
        })
    return rows
