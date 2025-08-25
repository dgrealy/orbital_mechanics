import math

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


if __name__ == "__main__":
    # Example usage:
    a = 7000  # km
    e = 0.01

    print(f"Periapsis distance: {periapsis_distance(a, e):.2f} km")
    print(f"Apoapsis distance: {apoapsis_distance(a, e):.2f} km")
    print(f"Orbital period: {orbital_period(a) / 60:.2f} minutes")
