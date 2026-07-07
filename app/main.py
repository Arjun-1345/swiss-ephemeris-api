from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Swiss Ephemeris Intergration",
    description="""
Swiss Ephemeris REST API exposing astronomical calculations through HTTP endpoints.

## Features

- Planet Positions
- House Cusps
- Ayanamsha
- Rise & Set Times
- Solar & Lunar Eclipses
- Fixed Stars
- Occultations
- Refraction
- Heliacal Events
- Coordinate Conversions

Built using **pyswisseph**.
""",
    version="1.0.0",


)

app.include_router(router)