"""Live Threat Monitor - real-time simulation of cloud-based threat detection."""

import streamlit as st
import numpy as np
from datetime import datetime

from config.constants import ATTACK_DISTRIBUTION, SEVERITY_LEVELS, SEVERITY_WEIGHTS
from config.theme import COLORS

_ATTACK_TYPES = list(ATTACK_DISTRIBUTION.keys())
_ATTACK_WEIGHTS = list(ATTACK_DISTRIBUTION.values())
_SEV_COLORS = {
    "Critical": COLORS["danger"], "High": "#D84315",
    "Medium": COLORS["warning"], "Low": COLORS["muted"],
}


def _random_ip(rng):
    return f"{rng.integers(1,255)}.{rng.integers(0,255)}.{rng.integers(0,255)}.{rng.integers(1,255)}"


def _render_feed(feed, dim=False):
    """Render a list of log entries as styled HTML."""
    lines = []
    for e in feed:
        sc = _SEV_COLORS.get(e["severity"], COLORS["muted"])
        opacity = "opacity:0.7;" if dim else ""
        lines.append(
            f'<div style="font-family:JetBrains Mono,monospace;font-size:12px;'
            f'padding:3px 0;color:{sc};{opacity}">'
            f'[{e["timestamp"]}] [{e["severity"].upper()}] '
            f'{e["attack_type"]} from {e["source_ip"]} - {e["status"]}</div>'
        )
    st.markdown(
        f'<div style="background:{COLORS["secondary_bg"]};border:1px solid '
        f'{COLORS["border"]};border-radius:6px;padding:12px 16px;'
        f'max-height:420px;overflow-y:auto;">{"".join(lines)}</div>',
        unsafe_allow_html=True,
    )


# ── State ────────────────────────────────────────────────────────────────────
if "feed" not in st.session_state:
    st.session_state.feed = []

# ── Header ───────────────────────────────────────────────────────────────────
st.header("Live Threat Monitor")
st.markdown(
    "This simulation demonstrates how a cloud-based monitoring system detects "
    "and responds to threats in real time. Toggle monitoring to begin."
)

monitoring = st.toggle("Start Monitoring")

if monitoring:

    @st.fragment(run_every="1.2s")
    def _live_feed():
        rng = np.random.default_rng()
        entry = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "source_ip": _random_ip(rng),
            "attack_type": str(rng.choice(_ATTACK_TYPES, p=_ATTACK_WEIGHTS)),
            "severity": str(rng.choice(SEVERITY_LEVELS, p=SEVERITY_WEIGHTS)),
            "status": str(rng.choice(
                ["Blocked", "Detected", "Investigating"], p=[0.57, 0.31, 0.12],
            )),
            "response_time_min": int(np.clip(rng.lognormal(2.5, 0.8), 1, 480)),
        }

        st.session_state.feed.insert(0, entry)
        st.session_state.feed = st.session_state.feed[:25]
        feed = st.session_state.feed

        blocked = sum(1 for e in feed if e["status"] == "Blocked")
        detected = sum(1 for e in feed if e["status"] == "Detected")
        avg_rt = np.mean([e["response_time_min"] for e in feed])

        c1, c2, c3 = st.columns(3)
        c1.metric("Blocked", blocked)
        c2.metric("Detected", detected)
        c3.metric("Avg Response Time", f"{avg_rt:.0f} min")

        # Pulsing alert for recent critical detections
        if len(feed) >= 10:
            has_critical = any(
                e["severity"] == "Critical" and e["status"] == "Detected"
                for e in feed[:3]
            )
            if has_critical:
                st.markdown(
                    f'<div class="sn-pulse" style="background:{COLORS["danger_light"]};'
                    f'border:1px solid {COLORS["danger"]};border-radius:6px;'
                    f'padding:12px 16px;margin:8px 0 12px 0;color:{COLORS["danger"]};'
                    f'font-family:Plus Jakarta Sans,sans-serif;font-size:13px;'
                    f'font-weight:600;">Critical Threat Detected, automated response '
                    f"initiated</div>",
                    unsafe_allow_html=True,
                )

        _render_feed(feed)

    _live_feed()

else:
    if st.session_state.feed:
        st.caption("Monitoring paused")
        _render_feed(st.session_state.feed, dim=True)
    else:
        st.info("Toggle monitoring above to begin the live threat simulation.")
