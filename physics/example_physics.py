# example_physics.py

import math

EPSILON_0 = 8.854187817e-12


def calculate_surface_area(radius: float) -> float:
    """
    Calculate the surface area of a sphere.

    Args:
        radius: Radius of the sphere (m)

    Returns:
        Surface area (m²)
    """
    return 4 * math.pi * radius**2


def calculate_electric_field(
    q_enclosed: float,
    radius: float,
) -> float:
    """
    Calculate the electric field at the surface
    of a spherical Gaussian surface.

    Args:
        q_enclosed: Enclosed charge (C)
        radius: Sphere radius (m)

    Returns:
        Electric field magnitude (N/C)
    """
    return (
        q_enclosed
        / (4 * math.pi * EPSILON_0 * radius**2)
    )


def calculate_flux_from_charge(
    q_enclosed: float,
) -> float:
    """
    Calculate electric flux using Gauss's Law.

    Args:
        q_enclosed: Enclosed charge (C)

    Returns:
        Electric flux (N·m²/C)
    """
    return q_enclosed / EPSILON_0


def calculate_flux_from_field(
    electric_field: float,
    surface_area: float,
) -> float:
    """
    Calculate electric flux from E·A.

    Args:
        electric_field: Electric field magnitude (N/C)
        surface_area: Sphere surface area (m²)

    Returns:
        Electric flux (N·m²/C)
    """
    return electric_field * surface_area