from datetime import datetime

import swisseph as swe

from app.models.response import PlanetResponse
from app.swiss.constants import PLANETS, DEFAULT_FLAGS
from app.swiss.exceptions import InvalidPlanetError
from app.swiss.houses import get_houses
from app.swiss.ayanamsha import get_ayanamsha
from app.swiss.rise_set import get_rise_set
from app.swiss.time import get_time
from app.swiss.coordinates import get_coordinates
from app.swiss.eclipse import solar_eclipse, lunar_eclipse, solar_where, solar_how, lunar_how
from app.swiss.fixed_star import fixed_star
from app.swiss.occultation import occultation_global, occultation_where, occultation_local
from app.swiss.refraction import refraction, refraction_extended
from app.swiss.azalt_reverse import azalt_reverse
from app.swiss.heliacal import heliacal


class SwissEngine:

    def __init__(self, ephemeris_path: str = "ephe"):
        self.ephemeris_path = ephemeris_path
        swe.set_ephe_path(ephemeris_path)

    @staticmethod
    def julian_day(dt: datetime) -> float:
        hour = dt.hour + dt.minute/60 + dt.second/3600 + dt.microsecond/3600000000
        return float(swe.julday(dt.year, dt.month, dt.day, hour))

    def get_planet(self, planet: str, dt: datetime) -> PlanetResponse:
        planet = planet.lower()
        if planet not in PLANETS:
            raise InvalidPlanetError(f"Unknown planet: {planet}")
        jd = self.julian_day(dt)
        result, flag = swe.calc_ut(jd, PLANETS[planet], DEFAULT_FLAGS)
        return PlanetResponse(
            planet=planet.title(),
            julian_day=jd,
            longitude=result[0],
            latitude=result[1],
            distance_au=result[2],
            speed_longitude=result[3],
            speed_latitude=result[4],
            speed_distance=result[5],
            flags=flag,
        )

    def get_all_planets(self, dt):
        return {p: self.get_planet(p, dt) for p in PLANETS}

    def get_houses(self, dt, latitude, longitude): return get_houses(dt, latitude, longitude)
    def get_ayanamsha(self, dt): return get_ayanamsha(dt)
    def get_rise_set(self, planet, dt, latitude, longitude): return get_rise_set(planet, dt, latitude, longitude)
    def get_time(self, dt): return get_time(dt)
    def get_coordinates(self, planet, dt, latitude, longitude): return get_coordinates(planet, dt, latitude, longitude)


    def solar_eclipse(self, dt): return solar_eclipse(dt)
    def lunar_eclipse(self, dt): return lunar_eclipse(dt)
    def solar_where(self, dt): return solar_where(dt)
    def solar_how(self, dt, latitude, longitude): return solar_how(dt, latitude, longitude)
    def lunar_how(self, dt, latitude, longitude): return lunar_how(dt, latitude, longitude)

    def fixed_star(self, star, dt): return fixed_star(star, dt)

    def occultation_global(self, planet, dt): return occultation_global(planet, dt)
    def occultation_where(self, planet, dt): return occultation_where(planet, dt)
    def occultation_local(self, planet, dt, latitude, longitude): return occultation_local(planet, dt, latitude, longitude)

    def refraction(self, altitude, pressure, temperature): return refraction(altitude, pressure, temperature)
    def refraction_extended(self, altitude, pressure, temperature): return refraction_extended(altitude, pressure, temperature)

    def azalt_reverse(self, dt, azimuth, true_altitude, latitude, longitude):
        return azalt_reverse(dt, azimuth, true_altitude, latitude, longitude)

    def heliacal(self, planet, dt, latitude, longitude):
        return heliacal(planet, dt, latitude, longitude)
