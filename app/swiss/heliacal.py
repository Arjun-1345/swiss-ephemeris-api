from datetime import datetime

import swisseph as swe


def heliacal(
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

    atmo = (
        0.0,
        0.0,
        0.0,
        0.0,
    )

    observer = (
        36.0,   # age
        1.0,    # snellen ratio
        0.0,    # monocular (0)
        1.0,    # magnification
        0.0,    # aperture
        0.0,    # transmission
    )
    return swe.heliacal_ut(
        jd,
        geopos,
        atmo,
        observer,
        planet.title(),
        swe.HELIACAL_RISING,
        swe.HELFLAG_LONG_SEARCH,
    )