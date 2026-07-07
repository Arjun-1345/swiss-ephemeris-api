from datetime import datetime

from app.swiss.engine import SwissEngine


def get_astronomy(
    dt: datetime,
    latitude: float,
    longitude: float,
):
    engine = SwissEngine()

    return {
        "julian_day": engine.julian_day(dt),
        "planets": engine.get_all_planets(dt),
        "houses": engine.get_houses(
            dt,
            latitude,
            longitude,
        ),
        "ayanamsha": engine.get_ayanamsha(dt),
        "sun_rise_set": engine.get_rise_set(
            "sun",
            dt,
            latitude,
            longitude,
        ),
        "moon_rise_set": engine.get_rise_set(
            "moon",
            dt,
            latitude,
            longitude,
        ),
    }