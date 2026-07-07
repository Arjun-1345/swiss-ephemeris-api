from datetime import datetime

import swisseph as swe

from app.swiss.constants import PLANETS


def get_rise_set(
    planet: str,
    dt: datetime,
    latitude: float,
    longitude: float,
):
    hour = (
        dt.hour
        + dt.minute / 60
        + dt.second / 3600
        + dt.microsecond / 3_600_000_000
    )

    jd = swe.julday(
        dt.year,
        dt.month,
        dt.day,
        hour,
    )

    geopos = (
        longitude,
        latitude,
        0.0,
    )

    _, rise_time = swe.rise_trans(
        jd,
        PLANETS[planet],
        swe.CALC_RISE,
        geopos,
    )

    _, set_time = swe.rise_trans(
        jd,
        PLANETS[planet],
        swe.CALC_SET,
        geopos,
    )

    return {
        "planet": planet,
        "rise_julian_day": rise_time[0],
        "set_julian_day": set_time[0],
    }