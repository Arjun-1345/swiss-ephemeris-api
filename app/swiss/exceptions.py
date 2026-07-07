class SwissEphemerisError(Exception):
    """Base exception."""


class InvalidPlanetError(SwissEphemerisError):
    """Raised when an invalid planet is requested."""