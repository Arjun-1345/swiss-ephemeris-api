from datetime import datetime

import swisseph as swe


def get_houses(
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

    houses, ascmc = swe.houses_ex(
        jd,
        latitude,
        longitude,
        b'P',
    )

    return {
        "julian_day": jd,
        "houses": list(houses),
        "ascmc": list(ascmc),
    }