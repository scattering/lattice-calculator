import math

import numpy as np
import pytest

from lattice_calculator import Lattice, angle, modvec


def _lattice(a, b, c, alpha, beta, gamma):
    lat = Lattice(
        a=np.array([float(a)]),
        b=np.array([float(b)]),
        c=np.array([float(c)]),
        alpha=np.array([float(alpha)]),
        beta=np.array([float(beta)]),
        gamma=np.array([float(gamma)]),
        orient1=np.array([[1.0, 0.0, 0.0]]),
        orient2=np.array([[0.0, 1.0, 0.0]]),
    )
    lat.star()
    return lat


def _deg(value):
    return float(np.degrees(np.asarray(value).reshape(-1)[0]))


def test_hexagonal_reciprocal_angles_are_exact():
    # Regression: an unconditional +eps denominator guard in star() biased
    # every reciprocal angle by ~0.1% (hexagonal gamma* came out 60.033 deg).
    lat = _lattice(3.209, 3.209, 5.211, 90, 90, 120)
    assert _deg(lat.gammastar_r) == pytest.approx(60.0, abs=1e-9)
    assert _deg(angle(1, 0, 0, 0, 1, 0, "latticestar", lat)) == pytest.approx(60.0, abs=1e-9)
    assert _deg(angle(1, 0, 0, 0, 0, 1, "latticestar", lat)) == pytest.approx(90.0, abs=1e-9)
    expected_astar = 4 * math.pi / (math.sqrt(3) * 3.209)
    astar = float(np.asarray(modvec(1, 0, 0, "latticestar", lat)).reshape(-1)[0])
    assert astar == pytest.approx(expected_astar, rel=1e-12)


def test_cubic_reciprocal_angles():
    lat = _lattice(2 * math.pi, 2 * math.pi, 2 * math.pi, 90, 90, 90)
    assert _deg(angle(1, 0, 0, 1, 1, 0, "latticestar", lat)) == pytest.approx(45.0, abs=1e-9)
    assert _deg(angle(1, 1, 1, 1, -1, 0, "latticestar", lat)) == pytest.approx(90.0, abs=1e-9)
