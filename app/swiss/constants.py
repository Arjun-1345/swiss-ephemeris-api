"""
Swiss Ephemeris constants and configuration.
"""

import swisseph as swe

# Planet mapping
PLANETS = {
    "sun": swe.SUN,
    "moon": swe.MOON,
    "mercury": swe.MERCURY,
    "venus": swe.VENUS,
    "mars": swe.MARS,
    "jupiter": swe.JUPITER,
    "saturn": swe.SATURN,
    "uranus": swe.URANUS,
    "neptune": swe.NEPTUNE,
    "pluto": swe.PLUTO,
    "mean_node": swe.MEAN_NODE,
    "true_node": swe.TRUE_NODE,
}

# Default calculation flags
DEFAULT_FLAGS = (
    swe.FLG_SWIEPH
    | swe.FLG_SPEED
)