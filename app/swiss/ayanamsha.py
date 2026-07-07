from datetime import datetime

import swisseph as swe


def get_ayanamsha(dt: datetime):
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

    return {
        "julian_day": jd,
        "ayanamsha": swe.get_ayanamsa_ut(jd),
    }