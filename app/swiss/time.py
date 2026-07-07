from datetime import datetime

import swisseph as swe


def get_time(dt: datetime):
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

    y, m, d, h = swe.revjul(jd)

    return {
        "julian_day": jd,
        "reverse_julian": {
            "year": y,
            "month": m,
            "day": d,
            "hour": h,
        },
        "delta_t": swe.deltat(jd),
        "sidereal_time": swe.sidtime(jd),
    }