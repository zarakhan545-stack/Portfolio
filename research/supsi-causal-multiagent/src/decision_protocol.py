"""Deterministic calculations for the proposed multi-agent decision protocol.

This module does not train models, access datasets, or simulate human review.
"""
from __future__ import annotations

import numpy as np


def _validate(probabilities: np.ndarray) -> np.ndarray:
    p = np.asarray(probabilities, dtype=float)
    if p.ndim != 2 or p.shape[1] < 2:
        raise ValueError("Expected a 2D array with at least two agents.")
    if not np.isfinite(p).all() or ((p < 0) | (p > 1)).any():
        raise ValueError("Probabilities must be finite and in [0, 1].")
    return p


def ensemble_probability(agent_probabilities: np.ndarray) -> np.ndarray:
    """Return row-wise mean probability."""
    return _validate(agent_probabilities).mean(axis=1)


def disagreement(agent_probabilities: np.ndarray) -> np.ndarray:
    """Return population standard deviation across agent probabilities."""
    return _validate(agent_probabilities).std(axis=1, ddof=0)


def binary_entropy(probability: np.ndarray) -> np.ndarray:
    """Return binary entropy in nats, safely handling probabilities 0 and 1."""
    p = np.asarray(probability, dtype=float)
    if not np.isfinite(p).all() or ((p < 0) | (p > 1)).any():
        raise ValueError("Probabilities must be finite and in [0, 1].")
    with np.errstate(divide="ignore", invalid="ignore"):
        left = np.where(p > 0, p * np.log(p), 0.0)
        right = np.where(p < 1, (1 - p) * np.log1p(-p), 0.0)
    return -(left + right)


def review_assignment(agent_probabilities: np.ndarray, lower: float,
                      upper: float, disagreement_threshold: float) -> np.ndarray:
    """Return boolean review flags using interval OR disagreement rule."""
    if not (0 <= lower <= upper <= 1):
        raise ValueError("Require 0 <= lower <= upper <= 1.")
    if disagreement_threshold < 0:
        raise ValueError("Disagreement threshold must be non-negative.")
    p = _validate(agent_probabilities)
    mean = p.mean(axis=1)
    spread = p.std(axis=1, ddof=0)
    return ((mean >= lower) & (mean <= upper)) | (spread >= disagreement_threshold)


def automated_decision(agent_probabilities: np.ndarray, threshold: float) -> np.ndarray:
    """Return binary decisions from mean ensemble probability."""
    if not 0 <= threshold <= 1:
        raise ValueError("Threshold must be in [0, 1].")
    return (ensemble_probability(agent_probabilities) >= threshold).astype(int)


def final_decision(automated: np.ndarray, review_flag: np.ndarray,
                   reviewer_output: np.ndarray) -> np.ndarray:
    """Use reviewer output for referred cases and automation otherwise."""
    a = np.asarray(automated, dtype=int)
    r = np.asarray(review_flag, dtype=bool)
    h = np.asarray(reviewer_output, dtype=int)
    if not (a.shape == r.shape == h.shape):
        raise ValueError("automated, review_flag and reviewer_output must match.")
    if not np.isin(a, [0, 1]).all() or not np.isin(h, [0, 1]).all():
        raise ValueError("Decisions must be binary.")
    return np.where(r, h, a)
