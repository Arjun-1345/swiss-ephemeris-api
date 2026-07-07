from datetime import datetime

import swisseph as swe


def azalt_reverse(
    dt,
    azimuth,
    true_altitude,
    latitude,
    longitude,
):

    hour = (
        dt.hour
        + dt.minute / 60
        + dt.second / 3600
    )

    jd = swe.julday(
        dt.year,
        dt.month,
        dt.day,
        hour,
    )

    return swe.azalt_rev(
        jd,
        swe.HOR2ECL,
        (
            longitude,
            latitude,
            0,
        ),
        (
            azimuth,
            true_altitude,
        ),
    )