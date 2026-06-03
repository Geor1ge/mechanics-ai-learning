"""
Basic tests for Stage 0.

Run with:

    pytest
"""


def test_python_basic_math():
    assert 1 + 1 == 2


def test_numpy_import_and_array():
    import numpy as np

    a = np.array([1, 2, 3])
    assert a.sum() == 6


def test_project_package_import():
    import mechanics_ai

    assert mechanics_ai is not None
