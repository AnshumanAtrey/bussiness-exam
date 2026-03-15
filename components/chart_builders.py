"""Plotly chart factory functions with consistent theming."""

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from config.theme import COLORS, CHART_COLORS


_LAYOUT = dict(
    font=dict(family="Plus Jakarta Sans, sans-serif", size=13, color=COLORS["primary_text"]),
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=40, r=20, t=44, b=40),
    xaxis=dict(gridcolor=COLORS["divider"], gridwidth=1, zeroline=False),
    yaxis=dict(gridcolor=COLORS["divider"], gridwidth=1, zeroline=False),
    colorway=CHART_COLORS,
    hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_family="Plus Jakarta Sans, sans-serif",
        bordercolor=COLORS["border"],
    ),
    legend=dict(font=dict(size=12), bgcolor="rgba(0,0,0,0)"),
    title=dict(font=dict(family="Space Grotesk, sans-serif", size=16, color=COLORS["heading"])),
)

_CONFIG = {"displayModeBar": False, "displaylogo": False}


def apply_theme(fig, **overrides):
    """Apply the design-system layout to any Plotly figure."""
    merged = {**_LAYOUT, **overrides}
    fig.update_layout(**merged)
    return fig


def show(fig):
    """Render a themed Plotly figure in Streamlit."""
    st.plotly_chart(fig, use_container_width=True, config=_CONFIG)


def styled_plotly(fig, **overrides):
    """Apply theme and render in one call."""
    apply_theme(fig, **overrides)
    show(fig)


# ── Convenience builders (apply theme + render) ──

def create_bar_chart(data, x, y, title="", horizontal=False, **kw):
    if horizontal:
        fig = px.bar(data, x=y, y=x, orientation="h", title=title,
                     color_discrete_sequence=CHART_COLORS, **kw)
    else:
        fig = px.bar(data, x=x, y=y, title=title,
                     color_discrete_sequence=CHART_COLORS, **kw)
    styled_plotly(fig)


def create_line_chart(data, x, y, title="", **kw):
    fig = px.line(data, x=x, y=y, title=title,
                  color_discrete_sequence=CHART_COLORS, **kw)
    fig.update_traces(line=dict(width=2.5))
    styled_plotly(fig)


def create_pie_chart(data, names, values, title="", hole=0.4, **kw):
    fig = px.pie(data, names=names, values=values, title=title,
                 color_discrete_sequence=CHART_COLORS, hole=hole, **kw)
    fig.update_traces(textposition="inside", textinfo="percent+label")
    styled_plotly(fig)


def create_area_chart(data, x, y, title="", **kw):
    fig = px.area(data, x=x, y=y, title=title,
                  color_discrete_sequence=CHART_COLORS, **kw)
    styled_plotly(fig)
