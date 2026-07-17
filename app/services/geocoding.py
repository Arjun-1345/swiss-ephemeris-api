import requests


NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"


def get_coordinates_from_location(location: str):

    response = requests.get(
        NOMINATIM_URL,
        params={
            "q": location,
            "format": "json",
            "limit": 1,
        },
        headers={
            "User-Agent": "SwissEphemerisKundaliAPI/1.0"
        },
        timeout=10,
    )

    response.raise_for_status()

    results = response.json()

    if not results:
        raise ValueError(
            f"Location not found: {location}"
        )

    return {
        "latitude": float(results[0]["lat"]),
        "longitude": float(results[0]["lon"]),
        "display_name": results[0]["display_name"],
    }