"""Cohen's d effect-size helpers for n=1 self-experiment windows.

Mirrors the shipped hackedself_tools package (PyPI: hackedself-tools):
cohens_d(intervention, baseline) and rank_interventions({name: d}).
"""
import statistics as st


def cohens_d(a, b):
    """Cohen's d between baseline (b) and intervention (a) windows."""
    if len(a) < 2 or len(b) < 2:
        raise ValueError("need >=2 points per window")
    pooled = ((len(a) - 1) * st.variance(a) + (len(b) - 1) * st.variance(b)) / (len(a) + len(b) - 2)
    if pooled == 0:
        return 0.0
    return (st.mean(a) - st.mean(b)) / (pooled ** 0.5)


def rank_interventions(scores):
    """Sort {intervention: d} by absolute effect size, descending."""
    return sorted(scores.items(), key=lambda kv: abs(kv[1]), reverse=True)
