import swisseph as swe


def refraction(
    altitude,
    pressure=1013.25,
    temperature=15,
):

    return {
        "true_to_apparent": swe.refrac(
            altitude,
            pressure,
            temperature,
            swe.TRUE_TO_APP,
        ),
        "apparent_to_true": swe.refrac(
            altitude,
            pressure,
            temperature,
            swe.APP_TO_TRUE,
        ),
    }


def refraction_extended(
    altitude,
    pressure=1013.25,
    temperature=15,
):

    return swe.refrac_extended(
        altitude,
        0,
        pressure,
        temperature,
        0.0065,
        swe.TRUE_TO_APP,
    )