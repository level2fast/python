# test_gauss_law.py

import pytest

import example_physics


def test_gauss_law_for_spherical_surface():
    """
    Verify that:

        Φ = Q/ε₀

    matches

        Φ = E x A

    for a point charge enclosed by a spherical
    Gaussian surface.
    """

    # Charge enclosed by the Gaussian surface (C)
    q_enclosed = 1e-6

    # Radius of the Gaussian sphere (m)
    sphere_radius = 1

    # Sphere surface area (m²)
    surface_area = example_physics.calculate_surface_area(
        sphere_radius
    )

    # Electric field at sphere surface (N/C)
    electric_field = example_physics.calculate_electric_field(
        q_enclosed,
        sphere_radius,
    )

    # Flux computed directly from Gauss's Law
    flux_from_charge = example_physics.calculate_flux_from_charge(
        q_enclosed
    )

    # Flux computed from E·A
    flux_from_field = example_physics.calculate_flux_from_field(
        electric_field,
        surface_area,
    )

    # Verify the two approaches produce
    # the same physical result.
    assert flux_from_charge == pytest.approx(
        flux_from_field,
        rel=1e-12,
    )