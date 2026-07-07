from datetime import datetime
from pathlib import Path

import swisseph as swe

EPHE_PATH = str((Path(__file__).resolve().parents[2] / "ephe"))


def fixed_star(
    star: str,
    dt: datetime,
):
    # Ensure ephemeris path is set in this module
    swe.set_ephe_path(EPHE_PATH)

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

    xx, star_name, retflag = swe.fixstar2_ut(
        star.strip(),
        jd,
    )

    return {
        "star": star_name,
        "julian_day": jd,
        "position": {
            "longitude": xx[0],
            "latitude": xx[1],
            "distance": xx[2],
            "speed_longitude": xx[3],
            "speed_latitude": xx[4],
            "speed_distance": xx[5],
        },
        "retflag": retflag,
    }