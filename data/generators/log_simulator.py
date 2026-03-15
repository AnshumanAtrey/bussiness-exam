"""Generate synthetic cybersecurity log data."""

import time
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from config.constants import (
    ATTACK_DISTRIBUTION,
    SEVERITY_LEVELS,
    SEVERITY_WEIGHTS,
    TOTAL_CLIENTS,
)

_ATTACK_TYPES = list(ATTACK_DISTRIBUTION.keys())
_ATTACK_WEIGHTS = list(ATTACK_DISTRIBUTION.values())
_STATUSES = ["Blocked", "Detected", "Investigating", "Resolved"]
_STATUS_WEIGHTS = [0.52, 0.27, 0.13, 0.08]


def _random_ip(rng):
    return f"{rng.integers(1,255)}.{rng.integers(0,255)}.{rng.integers(0,255)}.{rng.integers(1,255)}"


def generate_logs(n: int = 2000, seed: int = 42) -> pd.DataFrame:
    """Return a DataFrame with *n* synthetic security-log rows."""
    rng = np.random.default_rng(seed)

    base = datetime(2025, 4, 1)
    offsets = np.sort(rng.integers(0, 365 * 24 * 60, size=n))
    timestamps = [base + timedelta(minutes=int(m)) for m in offsets]

    df = pd.DataFrame({
        "timestamp": timestamps,
        "source_ip": [_random_ip(rng) for _ in range(n)],
        "attack_type": rng.choice(_ATTACK_TYPES, size=n, p=_ATTACK_WEIGHTS),
        "severity": rng.choice(SEVERITY_LEVELS, size=n, p=SEVERITY_WEIGHTS),
        "status": rng.choice(_STATUSES, size=n, p=_STATUS_WEIGHTS),
        "response_time_min": np.clip(
            rng.lognormal(mean=2.5, sigma=0.8, size=n), 1, 480
        ).astype(int),
    })
    return df


def stream_logs(interval: float = 0.6):
    """Yield one synthetic log dict at a time (for live demo)."""
    rng = np.random.default_rng()
    while True:
        yield {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "source_ip": _random_ip(rng),
            "attack_type": rng.choice(_ATTACK_TYPES, p=_ATTACK_WEIGHTS),
            "severity": rng.choice(SEVERITY_LEVELS, p=SEVERITY_WEIGHTS),
            "status": rng.choice(["Blocked", "Detected", "Investigating"], p=[0.58, 0.30, 0.12]),
            "response_time_min": int(np.clip(rng.lognormal(2.5, 0.8), 1, 480)),
        }
        time.sleep(interval)
