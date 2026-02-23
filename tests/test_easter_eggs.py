import pytest
from outlandish_calc.easter_eggs import check_easter_egg

@pytest.mark.parametrize("value, expected", [
    (42, "The answer to life, the universe, and everything."),
    (666, "The number of the beast!"),
    (69, "Nice."),
    (404, "Error: Result not found (just kidding)."),
    (0, "The void stares back."),
])
def test_easter_egg_triggers(value, expected):
    # AC: Tests MUST verify that implemented easter eggs trigger correctly with their respective values.
    assert check_easter_egg(value) == expected

def test_easter_egg_infinity():
    import math
    assert check_easter_egg(math.inf) == "To infinity and beyond!"

def test_easter_egg_pi():
    import math
    assert check_easter_egg(math.pi) == "Mmm... pie."

def test_easter_egg_negative():
    assert check_easter_egg(-5) == "A bit negative, aren't we?"

def test_no_easter_egg():
    assert check_easter_egg(123.45) is None
