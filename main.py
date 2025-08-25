import math
from flask import Flask, jsonify, request

EARTH_MU = 398600.4418  # km^3 / s^2, standard gravitational parameter for Earth


def orbital_period(semi_major_axis: float, mu: float = EARTH_MU) -> float:
    """Calculate the orbital period in seconds.

    Parameters
    ----------
    semi_major_axis : float
        Semi-major axis of the orbit in kilometers.
    mu : float, optional
        Gravitational parameter of the central body in km^3/s^2. Default is Earth's.

    Returns
    -------
    float
        Orbital period in seconds.
    """
    return 2 * math.pi * math.sqrt(semi_major_axis ** 3 / mu)


def periapsis_distance(semi_major_axis: float, eccentricity: float) -> float:
    """Calculate the distance at periapsis (closest approach).

    Parameters
    ----------
    semi_major_axis : float
        Semi-major axis of the orbit in kilometers.
    eccentricity : float
        Orbital eccentricity (0 <= e < 1 for elliptical orbits).

    Returns
    -------
    float
        Distance at periapsis in kilometers.
    """
    return semi_major_axis * (1 - eccentricity)


def apoapsis_distance(semi_major_axis: float, eccentricity: float) -> float:
    """Calculate the distance at apoapsis (farthest point).

    Parameters
    ----------
    semi_major_axis : float
        Semi-major axis of the orbit in kilometers.
    eccentricity : float
        Orbital eccentricity (0 <= e < 1 for elliptical orbits).

    Returns
    -------
    float
        Distance at apoapsis in kilometers.
    """
    return semi_major_axis * (1 + eccentricity)

app = Flask(__name__)


@app.route("/calculate", methods=["GET"])
def calculate() -> "Response":
    """Compute orbital parameters and return them as JSON.

    Query Parameters
    ----------------
    semi_major_axis : float
        Semi-major axis of the orbit in kilometers.
    eccentricity : float
        Orbital eccentricity (0 <= e < 1 for elliptical orbits).
    """
    try:
        semi_major_axis = float(request.args["semi_major_axis"])
        eccentricity = float(request.args["eccentricity"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid or missing parameters"}), 400

    return jsonify(
        {
            "periapsis": periapsis_distance(semi_major_axis, eccentricity),
            "apoapsis": apoapsis_distance(semi_major_axis, eccentricity),
            "orbital_period": orbital_period(semi_major_axis),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
