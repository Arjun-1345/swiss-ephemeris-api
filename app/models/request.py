from pydantic import BaseModel


class DateTimeRequest(BaseModel):
    date: str
    time: str


class PlanetRequest(DateTimeRequest):
    planet: str


class GeoRequest(DateTimeRequest):
    latitude: float
    longitude: float


class PlanetGeoRequest(PlanetRequest):
    latitude: float
    longitude: float


class StarRequest(DateTimeRequest):
    star: str


class RefractionRequest(BaseModel):
    altitude: float
    pressure: float = 1013.25
    temperature: float = 15


class AzAltReverseRequest(DateTimeRequest):
    azimuth: float
    true_altitude: float
    latitude: float
    longitude: float