from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.swiss.engine import SwissEngine
from app.swiss.exceptions import InvalidPlanetError
from app.llm.gemini import generate_kundali_prediction
from app.services.geocoding import get_coordinates_from_location

PLANETS = "Planets"
HOUSES = "Houses"
ASTRONOMY = "Astronomy"
TIME = "Time"
COORDINATES = "Coordinates"
ECLIPSES = "Eclipses"
STARS = "Fixed Stars"
OCCULTATIONS = "Occultations"
ATMOSPHERE = "Atmosphere"
UTILITIES = "Utilities"

router = APIRouter()

engine = SwissEngine()


@router.post("/planet", tags=[PLANETS], summary="Get Planet Position")
def planet(
    planet: str,
    date: str,
    time: str,
):
    try:
        dt = datetime.strptime(
            f"{date} {time}",
            "%Y-%m-%d %H:%M:%S",
        )

        return engine.get_planet(
            planet,
            dt,
        )

    except InvalidPlanetError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/planets", tags=[PLANETS], summary="Get All Planet Positions")
def planets(
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.get_all_planets(dt)


@router.post("/houses", tags=[HOUSES], summary="Calculate Houses")
def houses(
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.get_houses(
        dt,
        latitude,
        longitude,
    )
    
@router.post("/ayanamsha", tags=[ASTRONOMY], summary="Calculate Ayanamsha")
def ayanamsha(
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.get_ayanamsha(dt) 


@router.post("/rise-set", tags=[ASTRONOMY], summary="Calculate Rise and Set Times")
def rise_set(
    planet: str,
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.get_rise_set(
        planet,
        dt,
        latitude,
        longitude,
    )
    
    
@router.post("/astronomy", tags=[ASTRONOMY], summary="Complete Astronomy Data")
def astronomy(
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return {
        "julian_day": engine.julian_day(dt),
        "planets": engine.get_all_planets(dt),
        "houses": engine.get_houses(
            dt,
            latitude,
            longitude,
        ),
        "ayanamsha": engine.get_ayanamsha(dt),
        "sun_rise_set": engine.get_rise_set(
            "sun",
            dt,
            latitude,
            longitude,
        ),
        "moon_rise_set": engine.get_rise_set(
            "moon",
            dt,
            latitude,
            longitude,
        ),
    }
    
@router.post("/time", tags=[ASTRONOMY], summary="Time Calculations")
def time(
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.get_time(dt)

@router.post("/coordinates", tags=[ASTRONOMY], summary="Coordinate Transformations")
def coordinates(
    planet: str,
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.get_coordinates(
        planet,
        dt,
        latitude,
        longitude,
    )
    


@router.post("/solar-eclipse", tags=[ECLIPSES], summary="Find Solar Eclipse")
def solar_eclipse_route(
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.solar_eclipse(dt)


@router.post("/lunar-eclipse", tags=[ECLIPSES], summary="Find Lunar Eclipse")
def lunar_eclipse_route(
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.lunar_eclipse(dt)


@router.post("/solar-eclipse-where", tags=[ECLIPSES], summary="Solar Eclipse Visibility")
def solar_where_route(
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.solar_where(dt)


@router.post("/solar-eclipse-how", tags=[ECLIPSES], summary="Solar Eclipse Circumstances")
def solar_how_route(
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.solar_how(
        dt,
        latitude,
        longitude,
    )


@router.post("/lunar-eclipse-how", tags=[ECLIPSES], summary="Lunar Eclipse Circumstances")
def lunar_how_route(
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.lunar_how(
        dt,
        latitude,
        longitude,
    )
    
    
@router.post("/fixed-star", tags=[STARS], summary="Fixed Star Position")
def fixed_star_route(
    star: str,
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.fixed_star(
        star,
        dt,
    )
    

@router.post("/occultation/global", tags=[OCCULTATIONS], summary="Global Occultation")
def occultation_global_route(
    planet: str,
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.occultation_global(
        planet,
        dt,
    )


@router.post("/occultation/where", tags=[OCCULTATIONS], summary="Occultation Visibility")
def occultation_where_route(
    planet: str,
    date: str,
    time: str,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.occultation_where(
        planet,
        dt,
    )


@router.post("/occultation/local", tags=[OCCULTATIONS], summary="Local Occultation")
def occultation_local_route(
    planet: str,
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.occultation_local(
        planet,
        dt,
        latitude,
        longitude,
    )


@router.post("/refraction", tags=[ATMOSPHERE], summary="Calculate Atmospheric Refraction")
def refraction_route(
    altitude: float,
    pressure: float = 1013.25,
    temperature: float = 15,
):
    return engine.refraction(
        altitude,
        pressure,
        temperature,
    )


@router.post("/refraction-extended", tags=[ATMOSPHERE], summary="Calculate Extended Atmospheric Refraction")
def refraction_extended_route(
    altitude: float,
    pressure: float = 1013.25,
    temperature: float = 15,
):
    return engine.refraction_extended(
        altitude,
        pressure,
        temperature,
    )


@router.post("/azalt-reverse", tags=[UTILITIES], summary="Reverse Azimuth/Altitude Conversion")
def azalt_reverse_route(
    date: str,
    time: str,
    azimuth: float,
    true_altitude: float,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.azalt_reverse(
        dt,
        azimuth,
        true_altitude,
        latitude,
        longitude,
    )


@router.post("/heliacal", tags=[ATMOSPHERE], summary="Calculate Heliacal Event")
def heliacal_route(
    planet: str,
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.strptime(
        f"{date} {time}",
        "%Y-%m-%d %H:%M:%S",
    )

    return engine.heliacal(
        planet,
        dt,
        latitude,
        longitude,
    )
    
    
@router.post(
    "/kundali-data",
    tags=["Kundali"],
    summary="Get Kundali Data",
)
def kundali_data_route(
    date: str,
    time: str,
    latitude: float,
    longitude: float,
):
    dt = datetime.fromisoformat(
        f"{date}T{time}"
    )

    return engine.get_kundali_data(
        dt,
        latitude,
        longitude,
    )
    
@router.post(
    "/kundali-prediction",
    tags=["Kundali"],
    summary="Generate Kundali Prediction",
)
def kundali_prediction_route(
    date: str,
    time: str,
    location: str,
):
    dt = datetime.fromisoformat(
        f"{date}T{time}"
    )

    location_data = get_coordinates_from_location(location)

    latitude = location_data["latitude"]
    longitude = location_data["longitude"]

    kundali_data = engine.get_kundali_data(
        dt,
        latitude,
        longitude,
    )

    prediction = generate_kundali_prediction(
        kundali_data
    )

    return {
        "location": location_data["display_name"],
        "latitude": latitude,
        "longitude": longitude,
        "prediction": prediction,
    }