# This is the core file with the functions
"""
core.py
Utility functions for dynagamma.
"""

from __future__ import annotations

def square(x: float | int) -> float | int:
    """
    Return x².

    Parameters
    ----------
    x : int or float
        Number to square.

    Returns
    -------
    int or float
        x multiplied by itself.
    """
    return x * x


def greet(name: str = "world") -> str:        # ← keep any existing helpers
    return f"Hello, {name}!"
