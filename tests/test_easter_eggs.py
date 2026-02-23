import math
import pytest
from outlandish_calc.easter_eggs import check_easter_egg

def test_easter_egg_exact_matches():
    """Test triggers that require exact numeric matches."""
    assert check_easter_egg(42.0) == "The answer to life, the universe, and everything."
    assert check_easter_egg(69.0) == "Nice."
    assert check_easter_egg(404.0) == "Error: Result not found (just kidding)."
    assert check_easter_egg(666.0) == "The number of the beast!"
    assert check_easter_egg(0.0) == "The void stares back."

def test_easter_egg_pi_tolerance():
    """Test pi trigger with 0.001 tolerance."""
    # Exact pi
    assert check_easter_egg(math.pi) == "Mmm... pie."
    # Within 0.001
    assert check_easter_egg(3.141) == "Mmm... pie."
    assert check_easter_egg(3.142) == "Mmm... pie."
    # Outside 0.001 (3.14159 - 3.14 = 0.00159)
    assert check_easter_egg(3.14) is None
    assert check_easter_egg(3.15) is None

def test_easter_egg_infinity():
    """Test infinity trigger for both positive and negative infinity."""
    assert check_easter_egg(float('inf')) == "To infinity and beyond!"
    assert check_easter_egg(float('-inf')) == "To infinity and beyond!"

def test_easter_egg_negative():
    """Test negative trigger for values less than zero that aren't other triggers."""
    assert check_easter_egg(-1.0) == "A bit negative, aren't we?"
    assert check_easter_egg(-404.0) == "A bit negative, aren't we?"
    assert check_easter_egg(-0.00001) == "A bit negative, aren't we?"

def test_easter_egg_no_match():
    """Test that non-magic numbers return None."""
    assert check_easter_egg(1.0) is None
    assert check_easter_egg(10.0) is None
    assert check_easter_egg(100.0) is None
    assert check_easter_egg(123.456) is None