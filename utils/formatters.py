"""Display formatters for currency, percentages, and deltas."""


def fmt_inr(amount: float) -> str:
    """Format amount in Indian Rupee notation with commas (e.g. 12,34,567)."""
    neg = amount < 0
    n = int(abs(amount))
    s = str(n)

    if len(s) <= 3:
        result = s
    else:
        last3 = s[-3:]
        rest = s[:-3]
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.insert(0, rest)
        result = ",".join(parts) + "," + last3

    return f"-\u20b9{result}" if neg else f"\u20b9{result}"


def fmt_lakhs(amount: float) -> str:
    """Format amount in Lakhs (e.g. 46L)."""
    lakhs = amount / 1_00_000
    if abs(lakhs - round(lakhs)) < 0.05:
        return f"\u20b9{round(lakhs)}L"
    return f"\u20b9{lakhs:.1f}L"


def fmt_pct(value: float, decimals: int = 1) -> str:
    return f"{value:.{decimals}f}%"


def fmt_delta(value: float, suffix: str = "") -> str:
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.1f}{suffix}"
