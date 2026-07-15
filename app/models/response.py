from pydantic import BaseModel


class PlanetResponse(BaseModel):
    planet: str

    julian_day: float

    longitude: float
    latitude: float

    distance_au: float

    speed_longitude: float
    speed_latitude: float
    speed_distance: float

    flags: int
    retrograde: bool
    motion: str