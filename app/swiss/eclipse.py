from datetime import datetime

import swisseph as swe


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


def solar_eclipse(dt: datetime):

    jd = _jd(dt)

    retflag, tret = swe.sol_eclipse_when_glob(jd)

    return {
        "retflag": retflag,
        "times": list(tret),
    }


def lunar_eclipse(dt: datetime):

    jd = _jd(dt)

    retflag, tret = swe.lun_eclipse_when(jd)

    return {
        "retflag": retflag,
        "times": list(tret),
    }


def solar_where(dt: datetime):

    jd = _jd(dt)

    retflag, geopos, attr = swe.sol_eclipse_where(jd)

    return {
        "retflag": retflag,
        "geopos": list(geopos),
        "attributes": list(attr),
    }


def solar_how(
    dt: datetime,
    latitude: float,
    longitude: float,
):

    jd = _jd(dt)

    retflag, attr = swe.sol_eclipse_how(
        jd,
        (
            longitude,
            latitude,
            0,
        ),
    )

    return {
        "retflag": retflag,
        "attributes": list(attr),
    }


def lunar_how(
    dt: datetime,
    latitude: float,
    longitude: float,
):

    jd = _jd(dt)

    retflag, attr = swe.lun_eclipse_how(
        jd,
        (
            longitude,
            latitude,
            0,
        ),
    )

    return {
        "retflag": retflag,
        "attributes": list(attr),
    }