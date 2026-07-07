from datetime import datetime

import swisseph as swe

from app.swiss.constants import PLANETS


def get_coordinates(
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

    pos, _ = swe.calc_ut(
        jd,
        PLANETS[planet],
        swe.FLG_SWIEPH,
    )

    geopos = (
        longitude,
        latitude,
        0.0,
    )

    azalt = swe.azalt(
        jd,
        swe.ECL2HOR,
        geopos,
        0,
        0,
        pos[:3],
    )

    return {
        "planet": planet,
        "azimuth": azalt[0],
        "true_altitude": azalt[1],
        "apparent_altitude": azalt[2],
    }