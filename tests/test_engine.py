import pytest
from engine.math_engine import (
    add, subtract, multiply, divide, power, modulo, floor_divide, root, get_drama_level
)
from engine.exceptions import OutlandishError

@pytest.mark.parametrize("op, a, b, expected", [
    (add, 10, 5, 15),
    (add, 10.5, 4.5, 15.0),
    (subtract, 20, 7, 13),
    (subtract, 20.0, 7.5, 12.5),
    (multiply, 6, 7, 42),
    (multiply, 2.5, 4.0, 10.0),
    (divide, 10, 2, 5.0),
    (divide, 7.5, 2.5, 3.0),
    (power, 2, 3, 8),
    (power, 4.0, 0.5, 2.0),
    (modulo, 10, 3, 1),
    (modulo, 10.5, 4.0, 2.5),
    (floor_divide, 10, 3, 3),
    (floor_divide, 10.5, 3.0, 3.0),
    (root, 16, 2, 4.0),
    (root, 27.0, 3.0, 3.0),
])
def test_math_operations(op, a, b, expected):
    """Verify all 8 math operations with both integer and float inputs."""
    assert op(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("op, a, b, message", [
    (divide, 10, 0, "The universe cannot handle division by the void of zero!"),
    (modulo, 10, 0, "The remainder of nothingness is a cosmic impossibility!"),
    (floor_divide, 10, 0, "Attempting to floor the infinite is a fool's errand!"),
    (root, -1, 2, "Imaginary numbers are too dramatic for this reality!"),
])
def test_outlandish_error_messages(op, a, b, message):
    """Assert that OutlandishError is raised with the correct dramatic message for invalid operations."""
    with pytest.raises(OutlandishError) as excinfo:
        op(a, b)
    assert str(excinfo.value) == message

@pytest.mark.parametrize("value, expected_level", [
    (5, 1),        # Bracket 1: < 10
    (50, 2),       # Bracket 2: 10-99
    (500, 3),      # Bracket 3: 100-999
    (5000, 4),     # Bracket 4: 1000-9999
    (50000, 5),    # Bracket 5: >= 10000
    (-5, 1),       # Negative values
    (-50000, 5),   # Large negative values
])
def test_drama_level_brackets(value, expected_level):
    """Verify that drama_level is correctly calculated for values across all five magnitude brackets."""
    assert get_drama_level(value) == expected_level