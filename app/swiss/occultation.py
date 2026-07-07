from datetime import datetime

import swisseph as swe

from app.swiss.constants import PLANETS


def _jd(dt: datetime):
    hour = (
        dt.hour
        + dt.minute / 60
        + dt.second / 3600
        + dt.microsecond / 3_600_000_000
    )

    return swe.julday(
        dt.year,
        dt.month,
        dt.day,
        hour,
    )


def occultation_global(
    planet: str,
    dt: datetime,
):
    jd = _jd(dt)

    retflag, tret = swe.lun_occult_when_glob(
        jd,
        PLANETS[planet],
    )

    return {
        "retflag": retflag,
        "times": list(tret),
    }


def occultation_where(
    planet: str,
    dt: datetime,
):
    jd = _jd(dt)

    retflag, geopos, attr = swe.lun_occult_where(
        jd,
        PLANETS[planet],
    )

    return {
        "retflag": retflag,
        "geopos": list(geopos),
        "attributes": list(attr),
    }


def occultation_local(
    planet: str,
    dt: datetime,
    latitude: float,
    longitude: float,
):
    jd = _jd(dt)

    retflag, tret, attr = swe.lun_occult_when_loc(
        jd,
        PLANETS[planet],
        (
            longitude,
            latitude,
            0,
        ),
    )

    return {
        "retflag": retflag,
        "times": list(tret),
    }